:template: 2017/na-content.html

Write the Docs Portland 2017 Speakers
=====================================

.. raw:: html

        <style>
        div.row.row-speaker img.speaker-image {
            width: 100%;
            margin-bottom: 1em;
            margin-right: 0em;
            border-radius: 5px;
            -moz-border-radius: 5px;
            -webkit-border-radius: 5px;
        }

        @media (max-width: 768px), (max-device-width: 768px) {
            div.row.row-speaker img.speaker-image {
                width: 120px;
                margin-right: 1em;
            }
        }
        div.row.row-speaker span.speaker-details {
            display: block;
            margin: .3em 0em;
            font-size: .7em;
            text-transform: initial;
        }

        div.row.row-speakers {
            margin-top: 1em;
            margin-bottom: 1em;
        }

        div.row.row-speakers dl > dt {
            margin-top: .65em;
            font-size: 1.2em;
        }

        div.row.row-speakers dl > dd {
            font-style: italic;
            padding: .3em 1em;
        }
        </style>

Presentations
-------------

{% set conf = "na-2017" %}
{% set speakers = na_2017_speakers %}

{% include conf_py_root + "/include/conf/speakers.jinja" %}
