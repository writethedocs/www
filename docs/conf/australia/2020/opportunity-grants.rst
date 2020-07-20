:template: {{year}}/generic.html

Opportunity grants
==================

The grant program for WTD {{ name }} 2020 supports people who would otherwise not be able to attend the conference by covering attendance costs. Applications are open to anyone who wants to attend Write the Docs.

{% if grants.url %}
To apply, fill in the form below.
{% else %}
We expect to open the grant program around the same time as ticket sales.
{% endif %}
As the conference is virtual this year, the grant offers you a single free ticket to the conference.

Depending on the number of applications, we may not be able to provide every applicant with a free ticket. We prioritize applications based on the overall impact that granting an application will have on the applicant, the Write the Docs community, and the applicant's wider community and country, compared to others.

Grant applicants, like all other participants in the Write the Documents community, are required to conform to the Code of Conduct: https://www.writethedocs.org/code-of-conduct/.

{% if grants.ends %}
**Grant applications are open until {{ grants.ends }}, Midnight {{ tz }}.**
{% endif %}

.. contents::
    :local:
    :depth: 1
    :backlinks: none

What is covered
----------------

All grants include a free conference ticket for the virtual conference.

Are you part of a marginalized or underrepresented group in tech?
------------------------------------------------------------------

This includes, but is not limited to:

* women and other gender minorities of all expressions and identities;  for example trans, agender and non-binary people
* people of color
* sexuality minorities, including asexual people
* people with disabilities, both visible and invisible
* neurodivergent people* people with chronic illnesses or diseases
* religious and ethnic minorities
* age minorities (under ~21, over ~50)
* people experiencing poverty* homeless and home/food insecure people
* caregivers of children or other dependents
* people who have experienced trauma and its aftermath (PTSD, anxiety, etc)
* people living with or recovering from substance abuse

You do not have to tell us which underrepresented group(s) you are a part of.

{% if grants.url %}

Submit your application
--------------------------

.. raw:: html

	<iframe src="{{ grants.url }}?embedded=true" width="760" height="850" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>

You can also view `the application form <{{ grants.url }}>`_ in its own page.

{% endif %}
