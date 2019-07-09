import os


def media_photo(_file, _type):
    """
    Return a path for either a photo of the speaker/sponsor,
    or a placeholder, to prevent broken image links.
    """
    for ext in ['jpg', 'png', 'svg']:
        file_name = '_static/img/{type}/{file}.{ext}'.format(
            type=_type,
            file=_file,
            ext=ext,
        )
        if os.path.exists(file_name):
            return '/' + file_name
    return '/_static/img/speakers/missing.jpg'


def speaker_photo(file):
    return media_photo(file, 'speakers')


def sponsor_photo(file):
    return media_photo(file, 'sponsors')


def add_jinja_filters_to_app(app):
    if app.builder.format != 'html':
        return

    from .meetups import state_abbr

    app.builder.templates.environment.filters['state_abbr'] = state_abbr
    app.builder.templates.environment.filters['speaker_photo'] = speaker_photo
    app.builder.templates.environment.filters['sponsor_photo'] = sponsor_photo
