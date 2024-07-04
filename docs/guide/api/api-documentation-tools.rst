=======================
API documentation tools
=======================

Specialized descriptive languages help when writing API documentation. 
Some of our favorite descriptive languages include:

* :ref:`API Blueprint`
* Swagger

When specifying a descriptive language for your API, you'll also need tools to create engaging 
documents. Several tools work best with our favorite descriptive languages:

* :ref:`Apiary`
* Aglio
* :ref:`Sphinx`

Apiary
~~~~~~

Apiary is a service that allows you to edit and host documentation online.

Hosting Apiary docs
------------

Apiary provides a service for creating and hosting API documentation described in the :ref:`API Blueprint`
or Swagger format. Once the API description is complete, Apiary generates interactive documentation in a 
three column layout. Example requests and responses are shown for every endpoint in multiple 
programming languages. It also enables the user to make requests to your live API. 

.. _apiary-building-docs:

Building Apiary docs
-------------

To build Apiary docs locally, follow these steps:

1. `Install the Apiary CLI Tools. <https://help.apiary.io/tools/apiary-cli/>`_
2. Navigate to the directory containing your ``.apib`` file.
3. Run the following to validate your ``.apib`` file and create the HTML file::

  apiary preview --path="myfile.apib" --output="myfile.html"

4. View the document in your browser.

API Blueprint
~~~~~~~~~~~~~

API Blueprint is a high-level language for describing web APIs. The goal of the API Blueprint format 
is to support the design-first philosophy for REST APIs; however, the format also works for 
documenting existing APIs. The files are saved with a `.apib` extension.

The syntax combines Markdown syntax and Markdown Syntax for Object Notation (MSON). Markdown is a 
lightweight text formatting syntax and `MSON <https://github.com/apiaryio/mson>`_ is an extension 
of Markdown for describing data objects.

Getting started with API Blueprint
---------------

The quickest way to get started with API Blueprint is to use `Apiary <https://apiary.io/>`_ to edit and view your 
documentation by following these steps: 

1. Sign up for an account `on Apiary. <https://login.apiary.io/register>`_
2. Follow the `API Blueprint Tutorial. <https://apiblueprint.org/documentation/tutorial.html>`_ to describe 
a basic API.

Writing API Blueprint docs
------------

The structure for an ``.apib`` file is::

  Metadata
  API Name
  Resource Group
    Resource
      Action
      Action
    Resource
  Resource Group
  Data Structures

``Metadata``:
  describes the API Blueprint version

``API Name``:
  your API name

``Resource Groups``:
  describes a collection of related API endpoints

``Resources``:
  describes a specific API endpoint

``Actions``:
  describes specific HTTP verb actions to an endpoint

``Data Structures``:
  describes data used in your API requests/responses. By defining them in a separate section, they 
  can easily be reused.

Building API Blueprint docs
-------------

The two most popular tools for generating documents from API Blueprints are :ref:`Apiary <apiary-building-docs>` and 
`Aglio <https://github.com/danielgtaylor/aglio>`_.

Testing API docs
~~~~~~~~~~~~~~~~

When specifying an API in a descriptive language, you don't have to manually 
validate your documents. Tools like Dredd can test your documentation against the live API.
