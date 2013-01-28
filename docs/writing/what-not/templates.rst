#########
Templates
#########

Avoid the copy-paste-adapt pattern in documentation. Replace it by interactive
scripts, configuration files and templates.

Yes:

.. code-block:: rst

  Configure deployment:

  .. code-block:: sh

    make configure

Yes:

.. code-block:: rst

  Use paster to generate Buildout configuration:

  .. code-block:: sh

    bin/paster create -t buildout_configuration etc/buildout

No:

.. code-block:: rst

  Copy the following content to ``settings.py`` file somewhere in your sys.path
  then adapt it to your needs:

  .. code-block:: python

    from myproject.default_settings import *

    DEBUG = True
