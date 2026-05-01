## Write the Docs website

This is the code that powers [www.writethedocs.org](http://www.writethedocs.org). It contains information about the Write the Docs group, as well as information about writing documentation.

To contribute to the Write the Docs website, it's helpful to familiarize yourself with the [Sphinx site generator](https://www.sphinx-doc.org/) and [reStructuredText markup syntax](https://www.sphinx-doc.org/en/stable/rest.html).

### Code Architecture

All of the generated website lives inside the `docs` directory, but many files outside the `conf/` directory are just static RST like any other Sphinx project.

All RST files are rendered with [Jinja](https://jinja.palletsprojects.com/), which allows the use of Jinja tags in all of them. A few custom Jinja filters are available for things like generating photo paths for speakers.

### Conference pages

For conferences, see [the conference site documentation](https://www.writethedocs.org/organizer-guide/confs/website/).

### Prerequisites for generating the docs locally

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python package manager).

2. In the repository root directory (`www` by default), run `uv sync` to install Python 3.12 and all dependencies.

### Previewing the docs locally

> Remember to activate the virtual environment using the appropriate command for your OS and Shell before running the following commands.

1. In the `docs` directory, run `uv run make livehtml` to view the docs on <http://127.0.0.1:8888/>.

If you're not seeing new content in the local preview, run `make clean` to delete the generated files, then `uv run make livehtml` to regenerate them.

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

[![Greenkeeper badge](https://badges.greenkeeper.io/writethedocs/www.svg)](https://greenkeeper.io/)

### Using devcontainer

In addition to local development with Python `venv`, it is also possible to use the devcontainer found in the root of the project.

### Using Docker

A barebones [dockerfile](./dockerfile) is supplied to run the site within a local Docker Container through [Docker Desktop](https://docs.docker.com/desktop/) - a simple, free, way to easily setup Docker and Python without leaving beyond installations, modifying your underlying Operating System, and changing Environment Variables.

1. Make sure Docker Desktop is running and started
1. Build the Docker Image from the root directory with the command: `docker build -t wtd .`
2. Run the Docker Image Container using that Image ID: `docker run -p 8888:8888 wtd`
3. Access the live site on <http://localhost:8888> through your web browser
4. Both the Docker Container and Image will be present in Docker Desktop

### Requirements

Make sure all of the following is installed.

- [Docker](https://docs.docker.com/get-started/get-docker/)
- [Supported IDE](https://containers.dev/supporting#editors)

Follow the steps below to open the development environment.

1. Open a [supported IDE](https://containers.dev/supporting#editors)
2. Click the "Open in devcontainer" popup
3. The development environment starts in an containerized environment
