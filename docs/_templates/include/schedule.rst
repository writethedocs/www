.. raw:: html

{% for talk in data %}

      <div class="row">
        <div class="col-xs-2">
          <p>{{ talk.Time }}</p>
        </div>
        <div class="col-xs-10>
          <p class=">

:ref:`{{ talk.Session }} <{{ talk.Session|slugify }}>`

.. raw:: html

          </p>
        </div>
      </div>

{% endfor %}
