=======================
API documentation tools
=======================

Writing API documentation works best when using specialized descriptive languages. 
Some of our favorites that we find do the job the best include:

* API Blueprint
* Swagger

If you're specifying your API in a descriptive language, you'll also need tools to create engaging 
documents. Some tools that work best with the languages we use include:

* Apiary
* Aglio
* Sphinx

Apiary
~~~~~~

Hosting Apiary docs
------------

Apiary provides a service for creating and hosting API documentation described in the API Blueprint or 
Swagger format. Once the API description is complete, Apiary generates interactive documentation in a 
three column layout. Example requests and responses are shown for every endpoint in multiple 
programming languages. It also enables the user to make requests to your live API. 

.. _apiary-building-docs:

Building Apiary docs
-------------

To build Apiary style docs locally, you need to install the Apiary CLI Tools. The full instructions 
are available `here. <https://help.apiary.io/tools/apiary-cli/>`_

Once it is installed, navigate to the directory containing your ``.apib`` file and run::

  apiary preview --path="myfile.apib" --output="myfile.html"

This will validate your ``.apib`` file and create the HTML file. You can then view the document in 
your browser.

API Blueprint
~~~~~~~~~~~~~

API Blueprint is a high-level language for describing web APIs. The syntax is a combination of 
Markdown syntax and Markdown Syntax for Object Notation (MSON), and the files are saved with a 
`.apib` extension. Markdown is a lightweight text formatting syntax. 
`MSON <https://github.com/apiaryio/mson>`_ is an extension of Markdown for describing data objects.

The goal of the API Blueprint format is to support the design-first philosophy for REST APIs; 
however, the format works just as well for documenting existing APIs.

Getting started
---------------

The quickest way to get started is to use `Apiary <https://apiary.io/>`_ to edit and view your 
documentation. Apiary is a service that allows you to edit and host documentation online. Start 
by signing up for an account `on Apiary. <https://login.apiary.io/register>`_
Next, continue with the 
`API Blueprint Tutorial. <https://apiblueprint.org/documentation/tutorial.html>`_ It provides a 
good overview of how to describe a basic API.

Writing API Bluepring docs
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
  is your API name

``Resource Groups``:
  describes a collection of related API endpoints

``Resources``:
  describes a specific API endpoint

``Actions``:
  describes specific http verb actions to an endpoint

``Data Structures``:
  describes data used in your API requests/responses. By defining them in a separate section, they 
  can easily be reused.


Building API Blueprint docs
-------------

The two most popular tools for generating documents from API Blueprints are Apiary and 
`Aglio <https://github.com/danielgtaylor/aglio>`_.

* :ref:`apiary-building-docs` with Apiary.


Testing API docs
~~~~~~~~~~~~~~~~

If you're specifying your API in a descriptive language, you don't have to rely on manually 
validating your documents anymore. Below we talk about tools you can use to test your documentation 
against the live API.

* Dredd