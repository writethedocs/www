import io
import re

import yaml


def slugify(slug):
    """
    Create a URL-appropriate slug of a string.
    Installed as a Jinja filter.
    """
    slug = slug.encode('utf-8', 'ignore').lower().decode('utf-8')
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug
# The C loader parses the same YAML about ten times faster than the pure
# Python one, and the build reads the conference data files hundreds of times.
_YAML_LOADER = getattr(yaml, 'CSafeLoader', yaml.SafeLoader)


def load_yaml(path):
    with io.open(path, encoding='utf-8') as fp:
        return yaml.load(fp, Loader=_YAML_LOADER)
