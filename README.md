## Write the Docs website

This is the code that powers [www.writethedocs.org](http://www.writethedocs.org). It contains information about the Write the Docs group, as well as information about writing documentation.

To contribute to the Write the Docs website, it's helpful to familiarize yourself with the [Sphinx site generator](https://www.sphinx-doc.org/) and [reStructuredText markup syntax](https://www.sphinx-doc.org/en/stable/rest.html).

### Code Architecture

All of the generated website lives inside the `docs` directory, but many files outside the `conf/` directory are just static RST like any other Sphinx project.

All RST files are rendered with [Jinja](https://jinja.palletsprojects.com/), which allows the use of Jinja tags in all of them. A few custom Jinja filters are available for things like generating photo paths for speakers.

### Conference pages

For conferences, see [the conference site documentation](https://www.writethedocs.org/organizer-guide/confs/website/).

### Videos

An even more fragile process that needs documenting and fixing. Note specifically `if year > 2023:` around line 134 of `docs/_ext/videos.py`.

WIP (Work In Progress) Docs on how to do this:

1. In `_data/<year>.<city>.speakers.yaml`, add a `youtubeId: 12345678901` key value pair to each talk. See also `_scripts/insert-video-ids.py`.

2. Make sure the directory `videos/<city>/<year>` is included in the Video Archive `toctree` in `docs/videos/index.rst`.

3. In the [virtual environment](#prerequisites-for-generating-the-docs-locally), switch to the `docs` directory and run `BUILD_VIDEOS=True make html`.

4. Commit the *relevant* changed files:

   * `docs/videos/index.rst`
   * `_data/<year>.<city>.speakers.yaml`
   * `docs/videos/<city>/<year>/*`

5. If you want to preview locally:

    1. Run `BUILD_VIDEOS=True make livehtml` and browse the new video pages at `http://127.0.0.1:8888`.

#### Troubleshooting

If you run into trouble with broken links to video files, have a look at `_ext/fix_video_yaml.py`:

1. Add a line at the end with the relevant places and dates.

2. Change to the `_ext` directory and run it:

   `python fix_video_yaml.py`

3. Commit the fixed `_data/<year>.<city>.speakers.yaml` file.

### Prerequisites for generating the docs locally

1. Install `python 3.9.x` using your package manager, if not installed already. You'll probably need `root` privileges to do this.

2. Generate a virtual environment for the WTD repo in the `venv` directory:

    `virtualenv --python=/usr/bin/python3.9 venv`

### Installing the project requirements

1. Activate the virtual environment as per your operating system:

    * On Linux-based systems, run `source venv/bin/activate`.
    * On Windows using the Command Prompt, run `venv\Scripts\activate.bat`.
    * On Windows using PowerShell, run `. venv\Scripts\activate.ps1`.
    * On Windows using Git Bash, run `source venv\Scripts\activate`.

    You'll need to do this every time you come back to the project.

2. In the repository root directory (`www` by default), run `pip install -r requirements.txt` to install sphinx and other requirements.

### Previewing the docs locally

> Remember to activate the virtual environment using the appropriate command for your OS and Shell before running the following commands.

1. In the `docs` directory, run `make livehtml` to view the docs on <http://127.0.0.1:8888/>.

If you're not seeing new content in the local preview, run `make clean` to delete the generated files, then `make livehtml` to regenerate them.

The Write the Docs website is hosted on [Read the Docs](https://readthedocs.org/projects/writethedocs-www).

### Updating the CSS

Styling is maintained in `docs/_static/conf/css/` as SASS. Convert SASS to minified CSS by installing SASS

```
npm install -g sass
```

 and then running (using a 2022 example):

```
sass --style=compressed docs/_static/conf/scss/main-2022.scss docs/_static/conf/css/main-2022.min.css
```

### Deactivating venv

After your work is complete, you can save resources by deactivating the
virtual Python environment with the following command on Linux:

`deactivate`

If you have verified this command on Windows, we invite you to submit a PR to include that information here.

[![Greenkeeper badge](https://badges.greenkeeper.io/writethedocs/www.svg)](https://greenkeeper.io/)

### Using devcontainer

In addition to local development with Python `venv`, it is also possible to use the devcontainer found in the root of the project.

### Requirements

Make sure all of the following is installed.

- [Docker](https://docs.docker.com/get-started/get-docker/)
- [Supported IDE](https://containers.dev/supporting#editors)

Follow the steps below to open the development environment.

1. Open a [supported IDE](https://containers.dev/supporting#editors)
2. Click the "Open in devcontainer" popup
3. The development environment starts in an containerized environment
