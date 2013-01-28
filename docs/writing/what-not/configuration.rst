#############
Configuration
#############

Documentation is not intended to contain configuration. Configuration is
meant to be consumed by scripts or similar tools.

As code, configuration should be readable.
As code, effective (production) configuration is the reference. Documentation
may be generated from it, but not the opposite.

As an example, consider system architecture. In some "Architecture" document,
you describe relationships between servers and clients:

* you may put some schemas or diagrams in the documentation, so that you give
  users an overview of the architecture.
* you shouldn't write server names in the documentation. You'd better reference
  the configuration of your environments.
* utilities you use for deployment, network management or monitoring should
  provide comprehensive views, or at least entry points so that you could
  generate comprehensive views.

Yes:

.. code-block:: rst

  Here is an overview of the architecture:

  .. image:: /_static/architecture-diagram.svg

  Architecture configuration is consumed by deployment tools:

  * `Production <https://example.com/deployment>`_
  * `Staging <https://staging.example.com/deployment>`_

  Monitoring gives you information about servers:

  * `Production <https://example.com/monitoring>`_
  * `Staging <https://staging.example.com/monitoring>`_

No:

.. code-block:: rst

  In production environment:

  * ``www.example.com`` is a Debian Squeeze server with, 4Go RAM and 20Go HDD.
    It serves:

    * the frontend, with Django 1.2
    * PostgreSQL server, version 8.4
    * Memcache

  * ``static.example.com`` is a FreeBSD server with 256Mo RAM and 500Go HDD.
    It serves static files with Nginx.

Configuration will not be maintained in documentation. Thus it is to become
obsolete, wrong and could lead to errors, misunderstanding... i.e. it has
negative impact.
