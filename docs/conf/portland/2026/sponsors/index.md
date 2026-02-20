---
template: {{year}}/generic.html
og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
banner: _static/conf/images/headers/2026/sponsors.jpg
---

{%- macro conf_sponsors() -%}
{% with include_text=True %}
{%- include year|string + "/sponsors.html" ignore missing -%}
{% endwith %}
{%- endmacro -%}
{% set conf_sponsors = conf_sponsors() %}

{%- macro sponsors_in_kind() -%}
{%- include year|string + "/sponsors-in-kind.html" ignore missing -%}
{%- endmacro -%}
{% set sponsors_in_kind = sponsors_in_kind() %}

{%- macro media_sponsors() -%}
{%- include year|string + "/sponsors-media.html" ignore missing -%}
{%- endmacro -%}
{% set media_sponsors = media_sponsors() %}

# Sponsors

We are seeking corporate partners to help us create the best conference possible.
You can find more information in our [prospectus](prospectus).

{% if conf_sponsors|trim %}

## Corporate sponsors

The conference wouldn't be nearly as great as it is without our wonderful corporate sponsors.
Thanks to these folks for supporting the community.

{{ conf_sponsors|trim|replace('\n      ', '\n')|replace('\n    ', '\n')|replace('\n  ', '\n') }}
{% endif %}

{% if sponsors_in_kind|trim %}

## In Kind Sponsors

Write the Docs is also helped out by companies that give their employees time to work on the conference.

{{ sponsors_in_kind|trim|replace('\n      ', '\n')|replace('\n    ', '\n')|replace('\n  ', '\n') }}

{% endif %}

{% if media_sponsors|trim %}

## Media Sponsors

These amazing media professionals have teamed up with us to capture the Write the Docs experience.

{{ media_sponsors|trim|replace('\n      ', '\n')|replace('\n    ', '\n')|replace('\n  ', '\n') }}

{% endif %}
