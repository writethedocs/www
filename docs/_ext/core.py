from __future__ import print_function

import re

import pytz
from jinja2 import TemplateError
from yaml import YAMLError
from .utils import load_yaml

import logging
import sys
from datetime import datetime, time, timedelta

try:
    from pathlib import PurePath
except ImportError:
    from pathlib2 import PurePath

log = logging.getLogger(__name__)

if sys.platform.startswith('win'):
    TIME_FORMATS = {
        '24h': '%H:%M',
        '12h': '%-H:%M %p',
    }
else:
    TIME_FORMATS = {
        '24h': '%H:%M',
        '12h': '%-I:%M %p',
    }

# Some DST timezones aren't "real" timezones.
TIMEZONE_TRANSLATION_PYTZ = {
    'CEST': 'CET',
    'EDT': 'US/Eastern',
}

def load_conference_page_context(app, page):
    """
    Check whether this is a conference page, and if so, have the
    conference specific YAML data loaded.
    Conference data is cached, so only loaded once.

    Returns an empty dict if it isn't run on a proper conference page.
    """
    if page.startswith('conf'):
        p = PurePath(page)
        try:
            year = int(p.parts[2])
        except (ValueError, IndexError):
            # If the second part is not the year, this is a document
            # about sponsorship or similar generic pages, that need
            # no conference-specific context.
            return {}
        if year >= 2018:
            shortcode = p.parts[1]
            year_str = str(year)
            cache_key = 'conference-context-cache-' + shortcode + year_str
            if cache_key in app.config.wtd_cache:
                return app.config.wtd_cache[cache_key]
            context = load_conference_context_from_yaml(shortcode, year, year_str, page)
            context['year_str'] = year_str
            app.config.wtd_cache[cache_key] = context
            return context
    return {}


def load_conference_context_from_yaml(shortcode, year, year_str, page):
    """
    Perform the actual loading of conference-related context.

    For pre-2020, this means loading the config. For 2020 and later,
    the schedule is also loaded, enriched with context from the speakers data.
    """
    data = {}
    if year < 2020:
        yaml_file = '_data/config-' + shortcode + '-' + year_str + '.yaml'
    else:
        yaml_file = '_data/' + shortcode + '-' + year_str + '-config.yaml'
    data.update(load_yaml_log_error(page, yaml_file))

    if year < 2020 or not data['flagspeakersannounced']:
        return data

    session_data = load_yaml_log_error(
        page, '_data/' + shortcode + '-' + year_str + '-sessions.yaml')

    if not data['flaghasschedule']:
        return data

    sessions_by_slug = {speaker['slug']: speaker for speaker in session_data}
    schedule_yaml_file = '_data/' + shortcode + '-' + year_str + '-schedule.yaml'
    schedule = load_yaml_log_error(page, schedule_yaml_file)

    # Do some additional contextual validation that can't be done by a YAML schema validator.
    # This aims to produce clear warnings rather than unexplained empty schedule output.
    if data['flaghaswritingday'] and 'writing_day' not in schedule and shortcode != 'australia':
        raise Exception('ERROR Missing key "writing_day" while reading schedule from %s' %
                        schedule_yaml_file)
    for day in range(1, data['date']['total_talk_days'] + 1):
        key = 'talks_day' + str(day)
        if key not in schedule:
            raise Exception('ERROR Missing key "%s" while reading schedule from %s' %
                            (key, schedule_yaml_file))

    # The schedule contains a time and a slug or title for each session.
    # Slugs reference the speakers/talk info (abstract, name, etc.), and that
    # info is added to the session info in the context.
    slugs_in_schedule = set()
    conf_date = None
    conf_timezone = None
    display_timezones = []
    if data.get('tz_header'):
        # If tz_header is present, this is assumed to be a multi-tz conference.
        # This expects the short date to be e.g. "Sep 10-12, 2023"
        # Does not need to be exact, hence we use first day - just for determining DST.
        conf_date = datetime.strptime(re.sub('-\d+', '', data['date']['short']), "%b %d, %Y")
        conf_timezone = pytz.timezone(data['tz'])
        display_timezone_names = re.split('[&,]', data['tz_header'])
        display_timezones = [(data['tz'], conf_timezone)] + [
            (n.strip(), pytz.timezone(TIMEZONE_TRANSLATION_PYTZ.get(n.strip(), n.strip())))
            for n in display_timezone_names
        ]
    for day_schedule in schedule.values():
        # "naive" refers to: datetime without timezone info
        naive_next_item_default_start = None
        for schedule_item in day_schedule:
            if data.get('time_format'):
                duration = timedelta()
                if 'duration' in schedule_item:
                    datetime_duration = datetime.strptime(schedule_item['duration'], '%H:%M')
                    duration = timedelta(hours=datetime_duration.hour, minutes=datetime_duration.minute)

                if 'time' in schedule_item:
                    naive_item_start = datetime.strptime(schedule_item['time'], '%H:%M')
                elif naive_next_item_default_start:
                    naive_item_start = naive_next_item_default_start
                else:
                    raise Exception('ERROR: found entry "%s" in schedule for %s with duration, but no previous entry with time' %
                        (schedule_item.get('slug', schedule_item.get('title')), page)
                    )
                if not display_timezones:
                    # In a single-tz schedule, render just naive time, first schedule item with TZ
                    schedule_item['time'] = naive_item_start.strftime(TIME_FORMATS[data['time_format']])
                    if not naive_next_item_default_start and not data.get('flaghasfood'):
                        schedule_item['time'] += ' ' + data['tz']
                if display_timezones:
                    # In multi-timezone, first convert to aware, then format for each timezone.
                    # Note that we need to combine with conf date to know whether there is DST.
                    aware_item_start = datetime.combine(conf_date, naive_item_start.time()).replace(tzinfo=conf_timezone)
                    schedule_item['time'] = '<br>'.join([
                        aware_item_start.astimezone(tz).strftime(TIME_FORMATS[data['time_format']]) + ' ' + tz_name
                        for tz_name, tz in display_timezones
                    ])
                naive_next_item_default_start = naive_item_start + duration

            if 'slug' in schedule_item:
                slug = schedule_item['slug']
                try:
                    session_data = sessions_by_slug[slug]
                    schedule_item['data'] = session_data
                    schedule_item['speaker_names'] = speaker_names_display(session_data['speakers'])
                    slugs_in_schedule.add(slug)
                except KeyError:
                    if data.get('flagscheduleincomplete'):
                        schedule_item['title'] = slug + ' (incomplete slug)'
                    else:
                        raise Exception(
                            'ERROR: Unable to find details for session %s while rendering page %s' % (slug, page))
            elif 'title' not in schedule_item:
                raise Exception(
                    'ERROR: Item %s in schedule rendered for %s has neither a slug nor title' % (schedule_item, page))

    missing_slugs_from_schedule = set(sessions_by_slug.keys()) - slugs_in_schedule
    if missing_slugs_from_schedule and not data.get('flagscheduleincomplete'):
        raise Exception('ERROR: Session slugs were found in the speakers YAML, '
                        'that are missing from the schedule: %s' % missing_slugs_from_schedule)

    data['schedule'] = schedule
    return data


def load_yaml_log_error(page, yaml_file):
    """
    Attempt to load a YAML file to render a conference page,
    logging an error if it fails.
    """
    try:
        yaml_config = load_yaml(yaml_file)
        return yaml_config
    except (YAMLError, OSError) as error:
        log.error('Unable to process conference YAML file %s while rendering %s: %s',
                  yaml_file, page, error)
        return {}


def speaker_names_display(speakers):
    """
    Flatten the names of one or more speakers into a single
    human-friendly string. Display for 3 speakers or more could
    be nicer, but this is a simple solution and we never have
    more than two so far.
    """
    names = [s['name'] for s in speakers]
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return '%s and %s' % (names[0], names[1])
    return ', '.join(names)


def render_rst_with_jinja(app, docname, source):
    """
    Pass our RST files through the jinja parser.
    This allows us to use all jinja features in all RST templates
    """
    if app.builder.format != 'html':
        return

    final_context = app.config.html_context.copy()
    conf_context = load_conference_page_context(app, docname)
    final_context.update(conf_context)
    src = source[0]
    try:
        rendered = app.builder.templates.render_string(src, final_context)
        source[0] = rendered
    except TemplateError as exc:
        message = exc.message + f' - while rendering {docname}'
        raise TemplateError(message=message)
    
def override_template_load_context(app, pagename, templatename, context, doctree):
    """
    Set the template to use when rendering the page.

    If a string is returned from this function,
    it will be the template used to render this page.
    Example::

        :template: 2018/conf.html

        Page title
        ==========

        Content
    """
    page_context = load_conference_page_context(app, pagename)
    context.update(page_context)

    # Markdown
    if (context and
            'page_source_suffix' in context and
            context['page_source_suffix'] == '.md'):
        txt = doctree[0].astext()
        if txt.startswith(':template:'):
            context['body'] = context['body'].replace(txt, '')
            return txt.split(':')[2].strip()
    # rst
    try:  # Sphinx was throwing a weird error here, and this is a workaround
        if (context and
                'meta' in context and
                'template' in context.get('meta', {})):
            return context['meta']['template']
    except TypeError:
        pass


def set_html_context(app, docname, source):
    # Store old context
    page_context = load_conference_page_context(app, docname)
    if page_context:
        app.config.old_html_context = app.config.html_context.copy()
        app.config.html_context.update(page_context)


def unset_html_context(app, doctree):
    if hasattr(app.config, 'old_html_context'):
        app.config.html_context = app.config.old_html_context.copy()
        del app.config.old_html_context
