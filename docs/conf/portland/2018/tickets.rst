:template: 2018/na/generic.html
:banner: _static/2018/assets/headers/venue.png

Tickets
=======

{% if not flagticketsonsale %}

Tickets will officially go on sale in **January 2018**.

{% endif %}

Each ticket includes:

* Entry to all conference events and activities
* Breakfast, snacks, and lunch on all conference days
* Welcome Reception and Social Event that will have light snacks and free drinks.
* Wifi throughout the event
* Meeting lots of fantastic people in a spacious, inviting venue.

.. class:: ticket

**Corporate Tickets** *${{ tickets.corporate.price }}*
------------------------------

Purchase this ticket if a company is paying for your attendance. Companies interested in sponsorship can also receive tickets to the conference with a sponsorship package.

{% if flagticketsonsale %}

`Buy ticket <{{tickets.corporate.url}}>`__

{% endif %}

.. class:: ticket

**Independent Tickets** *${{ tickets.independent.price }}*
--------------------------------

Purchase this ticket if you are paying for yourself, or if you work at a non-profit, a government, or a company with less than 10 employees.

{% if flagticketsonsale %}

`Buy ticket <{{tickets.independent.url}}>`__

{% endif %}

.. class:: ticket

**Student or Unemployed** *${{ tickets.student.price }}*
---------------------------------

Purchase this ticket if you are currently enrolled as a student, or don't currently have a source of income.

{% if flagticketsonsale %}

`Buy ticket <{{tickets.student.url}}>`__

{% endif %}

.. class:: ticket

**None of the above**
-------------------------------

If you can't afford these prices and still wish to attend, please email us at portland@writethedocs.org. Being a community event that keeps prices low, we can only offer discounted ticket prices, and not travel or hotel assistance.
