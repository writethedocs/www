:template: {{year}}/generic.html

News
====

Updates from the team.
More here as it happens!

.. postlist:: 100
   :date: %A, %B %d, %Y
   :format: {date}{title}
   :list-style: none
   :tags: {{ shortcode }}-{{ year }}

Join our mailing list
---------------------

Stay connected with the Write the Docs community! Our mailing lists send out messages 1-2 times a month, and your email won't be shared or used for any other purpose.

.. raw:: html

{% filter indent(4, first=True) %}{% include "conf/mailing-list.html" %}{% endfilter %}
