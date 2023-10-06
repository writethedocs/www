.. post:: October 06, 2023
  :tags: newsletter

#########################################
Write the Docs Newsletter – October 2023
#########################################

Ave, documentarians. Halloween may be approaching, but there's nothing scary about this month's batch of stories from the world of Write the Docs.

The Write the Docs `Documentarian Salary Survey for 2023 <https://salary-survey.writethedocs.org/>`__ is open and accepting submissions! This is the survey's fifth year and, in addition to our regular salary and job-related questions, we're exploring our community's thoughts on "back to the office" mandates, feelings about job security in a volatile market, and attitudes towards pay transparency.

So whether you're an employee, contractor, freelancer, or currently unemployed, `head on over <https://salary-survey.writethedocs.org/>`_ and help us make this year's survey the most useful yet.

In conference news, `tickets for the in-person Australia conference </conf/australia/2023/tickets/>`__ are still open. If you'd like to apply for an `opportunity grant </conf/australia/2023/opportunity-grants/>`__, you have until 15 October.

The newsletter this month covers how to include links within your docs, whether you can show some of your personality in your docs, how to handle docs in the same repository as product source code, and how much (or little) to capitalize feature names. Hope you enjoy!

--------------
Hyperlink Text
--------------

How to deal with links is a recurring question for documentarians. To answer it, some people suggested guidelines from the `W3C <https://www.w3.org/WAI/tips/writing/#make-link-text-meaningful>`__, `Microsoft <https://learn.microsoft.com/en-us/style-guide/urls-web-addresses>`__, and `Google <https://developers.google.com/style/link-text>`__.

The general consensus was to include text that's relevant — not just ‘click here’. Suggestions included using the linked page’s title, turning the title into relevant text, and creating descriptive text based on the context. Non-writers (such as developers) may prefer using the title for simplicity. More experienced documentarians may want to craft the text.

There are several issues involved:

- If there are inadequate guidelines for cross-referencing content, new or updated guidelines may be needed.
- The page title may be too long or unhelpful. If so, either edit the title or summarize the content in a few words.
- Some documentation systems focus on short, succinct topics. This may require many links to cross-reference content adequately.

A related issue concerns *where* to put the links: throughout the content or at the end of the content in a separate list? The main arguments against putting links at the end: the link may have lost its context or the reader may never scroll that far. In either case, it’s important to use relevant text. Having the link within the content may disrupt the reader by triggering cognitive overload and making them wonder: "Should I click or not? Should I click as I come to the link or wait until I finish reading?"

If you put links within the content, `one reference suggested <https://readabilityguidelines.co.uk/content-design/links/#2-avoid-mid-sentence-links>`__ always putting the link at the end of the sentence to minimize distraction. Accessibility was an additional concern, but exact solutions were unclear because interpretation depends upon the screen reader. 

--------------------------------
Personality in Technical Writing
--------------------------------

There are still different views among documentarians on the issue of the importance of personality, customization, and tone in technical writing.

Some people said that strict accuracy was the most important consideration in technical writing, while others said that there was room for creativity and humor as long as precision wasn’t compromised. In particular, they said that adding a bit of personality can make such writing more interesting, especially if the readers can handle it.

Context also came up as an essential factor, with people agreeing that different kinds of technical material need different levels of formality. For example, troubleshooting guides should always be very clear, while onboarding tutorials might benefit from a more friendly tone.

Also, many people stressed the importance of knowing the audience and suggested that the amount of personalization should match what they want and expect. Some even pushed for tech writing that changes the language by using broader terms and more open methods to improve users' experience.

Most people agreed that the audience’s needs should always come first. Individuality, personalization, and tone can improve technical writing in some situations, but isn't appropriate everywhere. Finding the best mix between readability, accuracy, and interest is important for making technical documentation that users can relate to and use to reach their goals.

-----------------------------------
Docs *with* Code Or Just *as* Code?
-----------------------------------

Someone who switched jobs recently asked in `#docs-as-code <https://writethedocs.slack.com/archives/C72NZ18FR>`__ about the benefits and drawbacks of keeping docs in the same repository as app code. They moved from having docs in a separate repository to docs in the same repository as the product source code and were feeling frustrated.

Some of the perceived drawbacks to keeping docs with app code included changes feeling slower and less flexible, requiring PRs for everything, even small typos. Each change also required reviews from developers and lots of linting when app code wasn't touched. Also, collaboration seemed more difficult than in tools like Google Docs and Notion. In short, it felt like there were roadblocks everywhere.

People noted some potential benefits, including increased accountability for changes with PRs. Some also felt safer knowing any mistakes weren't theirs alone and that the CI checks and reviews helped keep entire pages from breaking. Someone also noted that with docs in the same repository as code, it was easier to enforce docs changes when code is updated, including potentially automating some changes.

People had some suggestions to help overcome some roadblocks. Opening PRs early in the process lets reviewers check out changes locally to see the effects. Someone also suggested using the principle of pair programming in pair reviews for easier collaboration: run the docs locally and walk through the changes on a video call. Another idea was keeping PRs small and therefore manageable, but batching really small things like typos together if each PR takes too long. And encouraging improvements to the CI to catch typos earlier and also only running when needed (not linting untouched code).

Either setup can work and each works for some situations. As someone pointed out, if you're going to use docs-as-code, it's best to optimize for the code tools and processes available to you.

--------------------------
Capitalizing Feature Names
--------------------------

How much is too much when it comes to capitalizing the names of features in the docs? The limit may be lower than you think! This month, most documentarians recommended using capitalization only sparingly in your documentation.

Unnecessary capitalization is distracting for readers. It looks odd in English, especially when the words aren't proper nouns. Capitalizing generic terms like "dashboard" or "alert" makes it more difficult for readers to understand whether you're talking about the general meaning of the word or a specialized concept.

In addition, many writing systems do not used mixed case, and capitalization norms vary among languages, so excessive capitalization can make it more difficult to translate your documentation. It's also difficult to remove over-capitalization programmatically, particularly when certain words should retain capitalization in a specific context.

If you want to establish a precedent, it can be helpful to take a look at other companies' docs. Also, capitalization and naming is often covered in style guides -- check out these examples:

* `Shopify Polaris <https://polaris.shopify.com/content/naming#does-it-need-a-branded-name->`_
* `Splunk <https://docs.splunk.com/Documentation/StyleGuide/current/StyleGuide/UIGuidelines>`_
* `IBM Carbon Design System <https://carbondesignsystem.com/guidelines/content/writing-style/#capitalization>`_

For a designer's take on the subject, read `Fighting Feature Names <https://kubie.co/blog/fighting-feature-names/>`_ by Scott Kubie.

----------------
From Our Sponsor
----------------

This month’s newsletter is sponsored by Heretto:

.. raw:: html

    <hr>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
      <tbody>
        <tr>
          <td width="75%">
              <p>
                At Heretto, we’re thrilled to unveil a game-changing feature for tech writers and developers alike:  <a href="https://heretto.com/interactive-api-docs-product-and-api-documentation-in-one-place/">Interactive API Docs</a>. 
              </p>
              <p>
                API Docs empowers companies to consolidate their product and API documentation into a single-source repository for a seamless user experience. 
              </p>
              <p>
                Unify your docs on one branded site, test APIs in seconds, and drive API adoptions with search-ready documentation.
              </p>
              <p>
                Want to learn more? <a href="https://go.heretto.com/api-docs?utm_medium=3rd-party&utm_source=writethedocs&utm_campaign=q323-apidocs&utm_content=&utm_term=">Meet with our team to see API Docs in action</a>.
              </p>
          </td>
          <td width="25%">
            <a href="https://go.heretto.com/api-docs?utm_medium=3rd-party&utm_source=writethedocs&utm_campaign=q323-apidocs&utm_content=&utm_term=">
              <img style="margin-left: 15px;" alt="Heretto" src="/_static/img/sponsors/Heretto_Square__For_Non_White_Backgrounds.png">
            </a>
          </td>
        </tr>
      </tbody>
    </table>
    <hr>

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

----------------
Events Coming Up
----------------

- 6 Oct, 08:30 EDT (New England and Florida, USA): `Focused conversation: Document types and templates <https://www.meetup.com/boston-write-the-docs/events/295963820/>`__
- 7 Oct, 19:30  EAT (Nairobi, Kenya): `Documentation Localization in Open Source <https://www.meetup.com/write-the-docs-kenya/events/296445236/>`__
- 12 Oct, 18:30  EDT (Pittsburgh, USA): `UX writing for the rest of us <https://www.meetup.com/write-the-docs-pittsburgh/events/295832422/>`__
- 18 Oct, 08:00  PDT (Seattle, USA): `Write the Docs Seattle: Casual Caffeine Hour <https://www.meetup.com/write-the-docs-seattle/events/296381865/>`__
- 19 Oct, 17:30  CDT (Austin, USA): `Write the Docs ATX Happy Hour Meetup: October 19th <https://www.meetup.com/writethedocs-atx-meetup/events/295309096/>`__
- 20 Oct, 08:30 EDT (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/boston-write-the-docs/events/295963821/>`__
- 3 Nov, 08:30 EDT (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/boston-write-the-docs/events/xzpxdtyfcpbfb/>`__
