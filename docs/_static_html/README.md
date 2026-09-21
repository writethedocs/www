# Frozen conference sites

Everything here is pre-rendered HTML, copied into the built site as-is by
`html_extra_path`. Sphinx does not rebuild these pages, so there are no sources
to edit and nothing here picks up template, CSS, or footer changes. They look
the way the site looked on the day they were frozen.

Two generations live side by side:

- `conf/{na,eu,au}/2013`-`2017` predate the Sphinx site and keep their own
  stylesheets under `_static/conf-legacy/`.
- `conf/<city>/2018`-`2024` were rendered by this Sphinx site and then frozen,
  so they carry the site chrome from that day.

Conferences from 2025 onwards are still built from source in `docs/conf/`.

The 2013-2017 sites keep the `na`/`eu`/`au` URLs they were published under, so
a guessed city-style URL like `/conf/portland/2016/` would 404. Read the Docs
redirects cover those. They are configured on the project rather than in this
repository, so `docs/_scripts/create-rtd-conf-redirects.py` is the record of
what should exist and applies it through the API.

## Editing and linking

To change a frozen page, edit the HTML here directly. There is no other copy.

Link to a frozen conference with a plain URL, never `:doc:`, because these pages
are not Sphinx documents:

```rst
`Portland 2022 </conf/portland/2022/>`__
```

The `docs/_data/` YAML for these conferences is kept as the historical record
even though the build no longer reads it.

## Images

Frozen pages load images from `_frozen-images/`, not from Sphinx's generated
`_images/`. Sphinx numbers `_images/` filenames per build, so `photo.jpg` and
`photo1.jpg` can swap places when unrelated content changes. A frozen page
pointing there would eventually show the wrong picture, and nothing would catch
it because the link still resolves.

## Freezing another year

1. Build the site.
2. Copy `_build/html/conf/<city>/<year>/` to `conf/<city>/<year>/` here.
3. Copy every `_images/` file those pages reference into `_frozen-images/`, then
   rewrite their `_images/` references to `_frozen-images/`.
4. Delete the sources from `docs/conf/<city>/<year>/`.
5. Convert inbound `:doc:` references to plain URLs. Building with `-W` finds
   them all.
6. Widen the `--ignore-files` year range in `.github/workflows/ubuntu.yml`, so
   htmlproofer skips the frozen pages.
7. Remove any now-dead conference tags from `TAGS` in
   `docs/_ext/atom_absolute.py`.

Verify with `READTHEDOCS=True` set, not just a plain build. The atom feed
rewrite only runs on Read the Docs and fails the build when asked for a feed
that no longer exists, so a freeze that looks clean locally can still break
there.

Freezing a year removes its pages from the site search index and drops its blog
tag archive, since the news posts stop being ablog posts.
