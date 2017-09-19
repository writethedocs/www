import collections
import glob

from docutils import nodes
from docutils.parsers import rst
from docutils.statemachine import ViewList
from sphinx.errors import ExtensionError
from sphinx.util.nodes import nested_parse_with_titles

from .core import load_yaml


STATE_ABBREVIATIONS = {
    'Canada': {
        'Ontario': 'ON',
    },
    'USA': {
        'California': 'CA',
        'Colorado': 'CO',
        'Idaho': 'ID',
        'Massachusetts': 'MA',
        'New York': 'NY',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Texas': 'TX',
        'Washington': 'WA',
    }
}


def state_abbr(meetup):
    states = STATE_ABBREVIATIONS.get(meetup['country'])
    if not states:
        return meetup['state']
    return states.get(meetup['state'], meetup['state'])


def load_meetups_by_region():
    result = collections.defaultdict(list)
    for yaml_file in glob.glob('_data/meetups/*.yaml'):
        meetup = load_yaml(yaml_file)
        if 'website' not in meetup:
            raise ExtensionError('Meetup needs a website')
        result[meetup['region']].append(meetup)
    for _, meetups in result.items():
        meetups.sort(key=lambda m: m.get('city', m['country']))
    return result


class MeetupListing(rst.Directive):
    option_spec = {
        'region': rst.directives.unchanged,
    }
    has_content = False

    def run(self):
        env = self.state.document.settings.env
        app = env.app
        builder = app.builder

        meetups_by_region = load_meetups_by_region()

        templates = getattr(builder, 'templates', None)
        if not templates:
            return []

        region_name = self.options['region']
        output = ViewList()
        template_name = 'include/meetups/listing.jinja'
        rendered = builder.templates.render(template_name, {
            'meetups': meetups_by_region[region_name],
        })
        for line in rendered.splitlines():
            output.append(line, 'meetup-data')
        node = nodes.section()
        node.document = self.state.document
        nested_parse_with_titles(self.state, output, node)
        return node.children
