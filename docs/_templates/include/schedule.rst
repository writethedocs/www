.. raw:: html

    <table>
    {% for talk in data %}
      <tr>
        <td class=" schedule-time">{{ talk.Time }}</td>
        <td>

:ref:`{{ talk.Session }} <{{ talk.Session|slugify }}>`

.. raw:: html

        </td>
      </tr>

    {% endfor %}
    </table>