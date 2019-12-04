## Write the Docs website

This is the code that powers [www.writethedocs.org](http://www.writethedocs.org). It contains information
about the Write the Docs group, as well as information about writing documentation.

To contribute to the Write the Docs website, it's helpful to familiarize yourself with the [Sphinx site generator](https://www.sphinx-doc.org/), as well as [reStructuredText markup syntax](https://www.sphinx-doc.org/en/stable/rest.html).

### Code Architecture

All of the generated website lives inside the `docs` directory, but many files outside the `conf/` directory are just static RST, as in any other Sphinx project.

All RST files are rendered with [Jinja](http://jinja.pocoo.org/) which allows the use of Jinja tags in all of them. A few custom Jinja filters are available for things like generating photo paths for speakers.

### Conference pages

For conference pages, a configuration per conference is automatically loaded into the Jinja context. This allows the use of things like `{{ year }}` in RST files, and have it rendered correctly.

The important locations of files are:

* `_data/config-portland-2019.yaml` - This file contains the data for rendering a specific conference.
* `_templates/2019/` - Contains the HTML templates for all conferences that year, including common pages and separate navigation menus.
* `conf/portland/2019/` - Contains the RST files that we use for rendering the conference. Copy these over from the *previous* conference chronologically, not the previous conference in the same location.
* `include/conf/` Contains the text snippets which are *mostly* the same between all conferences, mostly describing what our events are (eg. lightning talks and unconference). They are included via the RST files for each event. Now we've merged #738 we can add content that is conditional to each conference using Jinja.
* `_ext/core.py` Contains the Sphinx extensions that manage injecting custom variables into our RST and Jinja templates. Specifically the `render_rst_with_jinja` and `load_conference_page_context` functions do a lot of the work.

The YAML config file's name must match the year and shortcode of the conference, i.e. for `conf/portland/2019`, the YAML loaded is `_data/config-portland-2019`.

Each conference also has YAML files for the schedule and speakers, in the format of `_data/2019.portland.speakers.yaml` and `_data/portland-2019-day-1.yaml`. These are rendered using Sphinx datatemplates, and also used in processes like generating video pages (a manual task, not done every time while building).

### Videos

An even more fragile process which needs documenting and fixing.

WIP Docs on how to do this:

1. In `_data/<year>.<city>.speakers.yaml`, add a `youtubeId: 12345678901` key value pair to each talk.

2. Make sure the directory `videos/<city>/<year>` is included in the Video Archive `toctree` in `docs/videos/index.rst`.

3. In the [venv](#prerequisites-for-generating-the-docs-locally) switch to the `docs` directory and run `BUILD_VIDEOS=True make html`.

4. Commit the the *relevant* changed files:

   * `docs/videos/index.rst`
   * `_data/<year>.<city>.speakers.yaml`
   * `docs/videos/<city>/<year>/*`

5. If you want to preview locally:

    1. Run `BUILD_VIDEOS=True make livehtml` and browse the new video pages at `http://127.0.0.1:8888`.

#### Troubleshooting

If you run into trouble with broken links to video files, have a look at `_ext/fix_video_yaml.py`:

1. Add a line at the end with the relevant places and dates

2. Change to the `_ext` directory and run it:

   `python fix_video_yaml.py`

3. Commit the fixed `_data/<year>.<city>.speakers.yaml` file.

### Prerequisites for generating the docs locally

1. Install `python 3.5.x` using your package manager, if not installed already.
   You'll probably need `root` privileges to do this.

2. Generate a virtual environment for the WTD repo in the `venv` directory:

    `virtualenv --python=/usr/bin/python3.5 venv`

### Installing the project requirements

1. Activate the virtual environment according to your operating system:

    * On Linux-based systems, run `source venv/bin/activate`.
    * On Windows using the Command Prompt, run `venv\Scripts\activate.bat`.
    * On Windows using PowerShell, run `. venv\Scripts\activate.ps1`.
    * On Windows using Git Bash, run `source venv\Scripts\activate`.

    You'll need to do this every time you come back to the project.

2. In the repository root directory (`www` by default), run `pip install -r requirements.txt` to install sphinx and other requirements.

### Previewing the docs locally

> Remember to activate the virtual environment using the appropriate command for your OS and Shell before running the following commands.

1. In the `docs` directory, run `make livehtml` to view the docs on [http://127.0.0.1:8888/](http://127.0.0.1:8888/).

If you're not seeing new content in the local preview, run `make clean` to delete the generated files, then `make livehtml` to regenerate them.

The Write the Docs website is hosted on [Read the Docs](https://readthedocs.org/projects/writethedocs-www).

### Previewing changes on Netlify

You can preview changes you've made on a pull request by clicking "Show all checks" at the bottom of the pull request page, and then clicking "Details" on the Netflify line, and navigating to the page you're making changes to.

### Updating the theme or css

If you need to update the theme, the original source is in

https://github.com/writethedocs/website-theme/

and instructions on how to update it are in the [`README.md`](https://github.com/writethedocs/website-theme/pull/3)

### Updating CSS for the 2018 Theme

The website for 2018 uses SASS to compile all the assets it has. To modify the theme, you must first install the dependencies of
`gulp`. In the main directory, run:

```
npm install
```

With that you will install all the requirements to minify your CSS;
after that you only need to run:

```
# Generate everything and serve site
gulp

# Only generate assets
gulp styles
```

This has to be used alongside the sphinx server and it will
automatically minify all the content in your `.scss` files to the
`main.min.css` file. Also, `gulp` will be running browserify, allowing you
to see the CSS changes immediately in the browser.

### Generating new conf pages

#### Copy and Create

There are a few places you need to copy files from when spinning up a new conference site:

1. The *YAML config file*. For example, copy `docs/_data/config-portland-2018.yaml` to `docs/_data/config-prague-2018.yaml`.
   Edit the file as necessary.
2. The *conference directory*. For example `docs/conf/portland/2018` to `docs/conf/prague/2018`.
3. The *templates*. For example `docs/_templates/2018/base_na.html` **and** `docs/_templates/2018/na` to `docs/_templates/2018/base_eu.html` **and** `docs/_templates/2018/eu`.
4. You might need some local content in `docs/includes/conf` and `_static`. Sphinx will probably warn you if you do.

#### Search and replace

Search and replace any year specific stuff (CAREFUL)
```
portland/2018
```

Manually update any FIXME comments
```
.. FIXME
```

For this whole thing to work we still need to implement these

```
.. TODO
```

[![Greenkeeper badge](https://badges.greenkeeper.io/writethedocs/www.svg)](https://greenkeeper.io/)
