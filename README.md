## Write the Docs website

This is the code that powers [www.writethedocs.org](http://www.writethedocs.org). It contains information
about the Write the Docs group, as well as information about writing documentation.

The repo is still in its early stages; feel free to contribute information that you might want to share with the community. To contribute to the Write the Docs website, it's helpful to familiarize yourself with the [Sphinx site generator](http://sphinx.pocoo.org/index.html), as well as [reStructuredText markup syntax](http://www.sphinx-doc.org/en/stable/rest.html).

### Prerequisites for previewing the docs locally

You'll probably need `root` privileges to install the prerequisites.

1. Install `python 2.7.x` using your package manager.

2. If your version of Python as shown by `python -V` is <= `2.7.9`:
   1. download and install [pip](https://pip.pypa.io/en/stable/installing/).
   2. install `virtualenv` using your package manager.

3. If you have already been using `virtualenv` with a different version of Python, you may need to run `virtualenv --python=/usr/bin/python2.7 <path/to/new/virtualenv>` to have `virtualenv` use the 2.7 interpreter.

### Installing the project requirements

1. In the repository root directory (`www` by default), create a virtual environment for the project requirements by running `virtualenv venv`. More info on `virtualenv` can be found [here](https://virtualenv.pypa.io/en/stable/).

2. On Linux-based systems, activate the virtual environment by running `source venv/bin/activate`. On Windows using the Command Prompt, run `venv\Scripts\activate.bat`. On Windows using PowerShell, run `. venv\Scripts\activate.ps1`. On Windows using Git Bash, run `source venv\Scripts\activate`. You'll need to do this every time you come back to the project.

2. In the repository root directory (`www` by default), run `pip install -r requirements.txt` to install sphinx and other requirements.

### Previewing the docs locally

> Remember to activate the virtual environment using the appropriate command for your OS and Shell before running the following commands.

1. In the `docs` directory, run `make livehtml` to view the docs on [http://127.0.0.1:8888/](http://127.0.0.1:8888/).

If you're not seeing new content in the local preview, run `make clean` to delete the generated files, then `make livehtml` to regenerate them.

The Write the Docs website is hosted on [Read the Docs](https://readthedocs.org/projects/writethedocs-www).

### Viewing changes on staging

If you you can't run `make livehtml` locally, or don't want to, you can preview
changes by merging them into the `staging` branch and pushing that to GitHub.

If your feature branch is `changes-to-test` you would do something like:

```
git checkout staging
git pull
git merge changes-to-test
git push
```

Unless there are merge conflicts you need to resolve, when you push those
changes a build is triggered on Read the Docs and when it is finished you can
preview your changes on:

http://writethedocs-staging.readthedocs.io/en/staging/

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
gulp
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
