:template: {{year}}/generic.html

Opportunity grants
==================

The grant program for Write the Docs {{ name }} {{ year }} supports people who would not be able to attend the conference by covering ticket and/or attendance costs. Applications are open to anyone who wants to attend Write the Docs.

{% if grants and grants.url %}
To apply, fill in the form below.
{% else %}

Who is Eligible
----------------

We encourage anyone to apply who would otherwise have difficulties attending the conference.

You are welcome to apply, even if you have received a grant before from our conferences or any others.

You are welcome to apply regardless of your experience level, background or reason making it difficult for you to cover the cost.

We prioritize applications based on the overall impact that granting an application will have on the applicant, the Write the Docs community, and the applicant's wider community and country, compared to others. However, there are no requirements for you to meet. **In other words, if you're not sure, feel free to apply.**

Grant applicants, like all other participants in the Write the Documents community, are required to follow the Code of Conduct: https://www.writethedocs.org/code-of-conduct/.

*Please note: Grant applications will be seen only by the conference team, and we will never publish grant applications or publicly name grant recipients.*


Schedule
----------------
**Now - February 1:** Grant applications open
**February 14:** Grant recipients notified 

What is covered
----------------

**All grants include a free conference ticket for the conference.** Note that this year, the conference ticket does not include meals.

We can cover typical costs like travel and accommodation,
but you may include other costs you need covered to be able to attend. 

This list can include, but is not limited to:
- Travel (flights, gas, rideshare, etc.)
- Accommodations
- Meals
- Other costs (childcare, loss of wages, etc.)

The application form will ask for an estimate of your costs.

Are you part of a marginalized or underrepresented group in tech?
------------------------------------------------------------------

Our grant program is open to anyone who wants to attend Write the Docs.
However, we may prioritise applications from people who are part of a marginalized or underrepresented group in tech. If you are not part of any of these groups, you are still welcome to apply.

These groups include, but are not limited to:

* women and other gender minorities of all expressions and identities;  for example trans, agender and non-binary people
* people of color
* sexuality minorities, including asexual people
* people with disabilities, both visible and invisible
* neurodivergent people
* people with chronic illnesses or diseases
* religious and ethnic minorities
* age minorities (under ~21, over ~50)
* people experiencing poverty
* homeless and home/food insecure people
* caregivers of children or other dependents
* people who have experienced trauma and its aftermath (PTSD, anxiety, etc)
* people living with or recovering from substance abuse

You do not have to tell us which underrepresented group(s) you belong to.

{% if grants and grants.url %}

Grant Amounts
----------------

The total amount of grant funds to be distributed is based upon sponsors and number of tickets sold. We will not know the full amount until we near the deadline. In 2023, $4,000 was distributed in grant funds. There is no limit on the amount you request but please note, we do not award partial grants. Free conference tickets are the most possible for us to grant. 

Submit your application
--------------------------

.. raw:: html

	<iframe src="{{ grants.url }}?embedded=true" width="760" height="850" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>

You can also view `the application form <{{ grants.url }}>`_ in its own page.

{% endif %}
