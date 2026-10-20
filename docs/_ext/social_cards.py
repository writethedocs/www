"""
Link preview cards, on top of sphinxext-opengraph's.

Leaves the description off the card, since the platform shows it under the
image anyway (sphinxext-opengraph's ``'description': False`` does nothing),
and shrinks the cards after the build: they are flat colour and text, so a
64-colour palette cuts them to a quarter of the size matplotlib writes. Same
file names, so the tags still match.
"""

from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import sphinxext.opengraph._social_cards as social_cards
from PIL import Image

render_social_card = social_cards.render_social_card


def render_without_description(path, site_title, page_title, description, siteurl, plt_objects):
    return render_social_card(path, site_title, page_title, '', siteurl, plt_objects)


def shrink_card(path):
    with Image.open(path) as im:
        im.convert('RGB').quantize(64, method=Image.Quantize.FASTOCTREE).save(path, optimize=True)


def shrink_cards(app, exception):
    if exception or app.builder.name not in ('html', 'dirhtml'):
        return
    cards = list(Path(app.outdir, '_images', 'social_previews').glob('*.png'))
    with ProcessPoolExecutor() as pool:
        list(pool.map(shrink_card, cards, chunksize=16))


def setup(app):
    social_cards.render_social_card = render_without_description
    app.connect('build-finished', shrink_cards)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
