:template: 2017/na-speakers.html

Conference Speakers
===================

{% set conf = "na-2017" %}

.. contents::    :local:


Workshops
----------

{% set speakers = na_2017_speakers_workshop %}

{% include conf_py_root + "/include/conf/2017-na-speakers.jinja" %}

Talks
----------

{% set speakers = na_2017_speakers_talk %}

{% include conf_py_root + "/include/conf/2017-na-speakers.jinja" %}

Unconference sessions
----------------------

{% set speakers = na_2017_speakers_unconf %}

{% include conf_py_root + "/include/conf/2017-na-speakers.jinja" %}
