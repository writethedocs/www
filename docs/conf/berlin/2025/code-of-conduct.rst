:template: {{year}}/generic.html

{% if shortcode == 'portland' %}

.. include:: ../../../code-of-conduct.rst
   :end-before: Atlantic conference Code of Conduct Team
{% else %}
.. include:: ../../../code-of-conduct.rst
   :end-before: Portland conference Code of Conduct Team
{% endif %}