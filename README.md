## Write the Docs website

This is the code that powers [www.writethedocs.org](http://www.writethedocs.org). It contains information
about the Write the Docs group, as well as information about writing documentation.

The repo is still in its early stages; feel free to contribute information that you might want to share with the community. To contribute to the Write the Docs website, famililarize yourself with the [Sphinx site generator](http://sphinx.pocoo.org/index.html).

To generate the docs locally:

1. Install `python 2.7.x` using your package manager.

2. If your version of Python as shown by `python -V` is <= 2.7.9, download and install  [pip](https://pip.pypa.io/en/stable/installing/) .

3. In the repository root directory (`www` by default), as the root user, run `pip install -r requirements.txt` to install sphinx and other requirements.

4. In the `docs` directory, run `make livehtml` to view the docs on [http://127.0.0.1:8888/](http://127.0.0.1:8888/).

The Write the Docs website is hosted on [Read the Docs](https://readthedocs.org/projects/writethedocs-www).
