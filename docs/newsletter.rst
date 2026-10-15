:template: community/newsletter.html
:banner: _static/conf/images/photos/notebooks-53653663881.jpg

Newsletter and mailing lists
============================

Once a month, our newsletter team rounds up the best conversations from the
Write the Docs Slack: questions, debates, and tips from documentarians around
the world. Over {{ newsletter_subs }} people read it.

Sign up
-------

Choose what you'd like to hear about. You can unsubscribe from any email.

.. raw:: html

   <form class="newsletter-signup" action="{{ community.mailing_list.action|e }}" method="post" target="_blank">
     <label for="newsletter-email">Email address</label>
     <div class="community-signup__form">
       <input id="newsletter-email" class="uk-input" type="email" name="EMAIL" autocomplete="email" required>
       <button class="uk-button" type="submit">Subscribe</button>
     </div>
     <fieldset>
       <legend>Send me</legend>
       <label><input type="checkbox" name="group[14633][1]" value="1" checked> The monthly community newsletter</label>
       <label><input type="checkbox" name="group[14633][2]" value="2" data-timezones="America/ US/ Canada/ Pacific/Honolulu"> North American conference announcements</label>
       <label><input type="checkbox" name="group[14633][4]" value="4" data-timezones="Europe/ Africa/ Atlantic/"> European conference announcements</label>
       <label><input type="checkbox" name="group[14633][8]" value="8" data-timezones="Australia/ Pacific/Auckland Pacific/Chatham"> Australian conference announcements</label>
       <label><input type="checkbox" name="group[14633][32]" value=""> Salary survey announcements</label>
     </fieldset>
     <!-- Bot trap from Mailchimp's embed code: people never fill it in. -->
     <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="{{ community.mailing_list.bot_field }}" tabindex="-1" value=""></div>
   </form>

Latest issues
-------------

.. raw:: html

   <!-- newsletter-issues -->

Past issues
-----------

.. raw:: html

   <!-- newsletter-archive -->

Looking for a subject? The :doc:`content by topic </topics>` gathers
newsletter articles and conference talks.

Sponsor the newsletter
----------------------

To reach our readers as a sponsor of an issue, see
:doc:`sponsor the newsletter </sponsorship/newsletter>`.

Get in touch
------------

Questions, or want to help write the newsletter? Email us at
`newsletter@writethedocs.org <mailto:newsletter@writethedocs.org>`_.
