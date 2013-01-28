#######
Scripts
#######

Documentation should not contain list of commands. Scripts are made for that
purpose.

As an example, installation procedures are usually written in documentation.
But, when they become quite long, they should be simplified with scripts.

It doesn't means that you can't write some INSTALL document. It means that
INSTALL document should be easy to read and use.

Yes:

.. code-block:: rst

  .. code-block:: sh

    make install

No:

.. code-block:: rst

  .. code-block:: sh

    # Install system dependencies.
    # If you are on Debian and have sudo installed:
    sudo aptitude --without-recommends python python-dev virtualenv
    # Get the source.
    git clone git://demo@example.com
    # Create a virtual environment.
    virtualenv demo
    source demo/bin/activate
    cd demo/
    # Install Python packages.
    pip install -r requirements.txt

As any piece of code, scripts have to be self-documented, readable, put in the
right place...

Some documentation may be generated from scripts, but not the opposite.
Documentation is not the place where to maintain scripts.
