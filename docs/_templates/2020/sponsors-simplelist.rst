{% for key in ('keystone', 'patron', 'publisher', 'second', 'first') %}
    {% if key in data.sponsors and data.sponsors[key] %}

      {% for sponsor in data.sponsors[key] %}
        * `{{ sponsor.name | capitalize() }} <{{ sponsor.link }}>`__
      {% endfor %}

    {% endif %}
{% endfor %}
