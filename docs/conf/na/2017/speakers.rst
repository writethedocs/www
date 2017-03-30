:template: 2017/na-speakers.html

Conference Speakers
===================

{% set conf = "na-2017" %}

.. contents::    :local:
   :class:  section
   :backlinks: none

Workshops
----------

This year's pre-conference Writing Day will feature two guided workshops, to help get your documentation neurons firing.

{% set speakers = na_2017_speakers_workshop %}

{% include conf_py_root + "/include/conf/2017-na-speakers.jinja" %}

Main Stage Talks
-------------------

The talks below form the main track of the conference and cover a vast range of subjects, points of view, and real-world case studies.

{% set speakers = na_2017_speakers_talk %}

{% include conf_py_root + "/include/conf/2017-na-speakers.jinja" %}

Unconference sessions
----------------------

Although you can still sign up to lead unconf sessions at the event, we're trying something new this year by including a few pre-billed anchor sessions to give folks an idea of what to expect from the unconf experience.


{% set speakers = na_2017_speakers_unconf %}

{% include conf_py_root + "/include/conf/2017-na-speakers.jinja" %}
