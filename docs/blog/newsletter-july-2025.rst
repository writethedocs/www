:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: July 03, 2025
  :tags: newsletter

#####################################
Write the Docs Newsletter – July 2025
#####################################

Ahoy, documentatarians! As the weather here heats up, I'm seeing more warnings for people to protect themselves from the heat. I hope wherever you are, you're taking measures to protect yourselves, whether that's to stay cool, stay warm, or just keep a clear head.

In community news, we have Calls for Proposals and ticket sales open for two (2!) more conferences this year: `Berlin </conf/berlin/2025/news/announcing-cfp-tickets/>`__ and `Australia </conf/australia/2025/news/announcing-cfp-tickets/>`__. Check them both out and see which works best for you. They both have virtual options (Australia is only virtual), so consider attending however you can or even submitting an interesting idea.

This month's newsletter has thoughts from the community on: autoplaying GIFs, running audits of your documentation, learning to use Agile, and how documentarians are using AI and LLMs.

The newsletter team is taking a break next month to keep our heads clear and ready for more interesting ideas, which will come again in September. For August, you'll get the usual community update.

--------------------------------
To autoplay animated GIFs or not
--------------------------------

A recent question was asked about having animated GIFs play automatically in documentation. The majority of respondents were opposed to autoplaying and looping GIFs. People mentioned usability, accessibility, and user control issues.

* **Usability**: Some people were fine with animated GIFs that only had short, one-time playbacks. Several mentioned that looping GIFs can be confusing because it’s difficult to know when the animation actually starts.
* **Accessibility**: A major accessibility concern is about having flashing elements on screen (especially with no user controls). So if the animated GIFs stop after 5 seconds and they don’t have blinking or flashing elements, they *may* be okay. Definitely include comprehensive alt text for people who can’t see the animation. For more information about accessibility issues, see `Are animated gifs okay to have? <https://accessibleweb.com/question-answer/animated-gifs-okay/>`__.
* **User control**: By default, animated GIFs play and loop automatically. In eLearning environments, `Richard Mayer’s research <https://ctl.risepoint.com/principles-of-multimedia-learning/>`__ emphasizes using multimedia strategically, but indicates that users want to control the pace of their learning. A documentation platform *may* provide a way to disable autoplay or provide user controls for animated GIFs. You (or a developer) may be able to add controls to the documentation (perhaps with CSS or JavaScript). See `Animated GIFs Pause and Play <https://www.docslikecode.com/articles/balsamiq-case-study-part-2/>`__. If animated GIFs aren’t adjusted by the provider, readers may be able to control autoplay using a browser plugin. 

Several people suggested some best practices to consider. In general, instead of using animated GIFs, use short videos (MP4 or WebM files) with user controls. (Note: You can convert animated GIFs to such files.) If you *must* use animated GIFs with no controls, limit them to very short and purposeful animations. Also consider showing a static GIF with instructions that the user can click to view the animated version.

See more Write the Docs resources about `media </topics/#other-media>`__.

----------------------------------------------
Strategies for successful documentation audits
----------------------------------------------

The next time you're considering auditing your documentation, consider these ideas from the WTD community to help make sure that it's a success.

Start by clarifying your goals. You might only want to map your content, or you might want to improve it. You might know specific issues you need to fix, or you might be trying to uncover them. Think about how ambitious your audit should be and how much time you can dedicate.

Consider who else to include in the audit: a technical writer who is familiar with the style guide, subject matter experts, someone who represents users' interests? If you need to improve docs that are new to you, check out the talk `Where do I start? The art and practice of documentation triage <https://www.youtube.com/watch?v=2EzIe-3LBwQ>`_. A more general resource that goes well beyond documentation is `Content Audits and Inventories: A Handbook for Content Analysis <https://xmlpress.net/content-strategy/audits-and-inventories/>`_.

If it fits your goals, establish a checklist that lists the quality standards and required features to evaluate each page of documentation against, such as grammar, formatting, and accuracy. Select a doc that's already in great shape to represent the ideal and give you a point of comparison. A previous newsletter item, `Measuring Docs Quality </blog/newsletter-november-2023/#measuring-docs-quality>`_, may help you shape the checklist.

Create a spreadsheet that lists information for every page such as the title, URL, last edit date, metrics, and expertise level. Use this spreadsheet to prioritize reviews, identify redundant content, and track findings and actions taken for each page. As a bonus, this spreadsheet can become the hub for ongoing documentation maintenance. You might find a useful starting point among these `content strategy templates <https://kevinpnichols.com/content-strategy-templates/>`_. If your audit addresses findability, consider this `search term analysis <https://lizargall.github.io/blog/search-term-analysis/>`_ guide and spreadsheet.

If the documentation is maintained in a Git repository, consider automating the data collection aspect of the audit. For example, you could use a script to fill a spreadsheet with metadata for each file, such as the file path, date and author for the last commit, and presence or absence of formatting elements or front matter. From there, you could develop additional scripts to find and fix common errors or apply documentation templates.

See more Write the Docs resources about `docs maintenance </topics/#maintenance>`__.

-----------------------------------
Navigating Agile for documentarians
-----------------------------------

Integrating into an Agile software development team presents unique challenges for many documentarians. A recent Write the Docs Slack discussion highlighted this common experience, offering valuable advice for documentarians aiming to thrive in Agile settings.

1. **Agile isn't one-size-fits-all**: Agile isn't a rigid methodology; it's a flexible philosophy with diverse implementations. It varies tremendously among companies and even teams. You'll encounter different frameworks such as Scrum, Kanban, or SAFe. Be prepared for common "gotchas," such as overly technical "user stories" or ever-expanding "backlogs." Recognizing these nuances helps you adapt.

2. **Key learning and skills**: To navigate this landscape, focus on core Agile principles. Good starting points include `Atlassian's Agile documentation <https://www.atlassian.com/agile>`__ and the Agile Alliance's `"Agile Essentials." <https://www.agilealliance.org/agile-essentials/>`__

   For those new to software development, focus first on basic technical concepts (such as front-end and back-end), software development lifecycle (SDLC) models, and developer roles.

   As you progress, align your documentation tasks with team "sprints" and ensure documentation is recognized as an integral part of development. Precise timing and coordination are essential for success.

3. **Embrace adaptability for impact**: The message from the discussion was clear: be prepared for variation, master the fundamentals, and cultivate adaptability. By understanding your team's Agile rhythm and advocating for documentation, you'll become an indispensable contributor. This ensures your docs are as responsive and influential as the products they support.

See more Write the Docs resources about `Agile and workflows </topics/#agile-and-workflows>`__.

-----------------------------------
How documentarians use AI (or LLMs)
-----------------------------------

With the availability of generative AI, many documentarians are wondering how to incorporate it into their work. Some are being asked to use AI to draft new content. 

Documentarians don’t necessarily want to avoid AI altogether, but rather want to use it when it adds value and doesn’t compromise quality. AI may have problems creating new content because it can only work with content and patterns it's already seen. It may not be suited for original content about new products and could fabricate content, causing legal issues. If asked about using it to create new content, say “NO”.

BUT, using AI can bring value. Specific tasks for AI use can include generating templates for others to use to provide new content, transforming existing content into other forms (such as tables, graphs, or troubleshooting procedures), reviewing content against a provided style guide, summarizing existing content (such as for introductory text or to make sense of a long email or Slack discussion), and performing repetitive, well-defined editing tasks. 

The `#ai channel <https://writethedocs.slack.com/archives/C1NEAD7D4>`__ included a report from a WTD Portland 2025 unconference session with some reported real-life usage, including:

* Make release notes based on file diffs from Git.
* For existing content, provide suggestions for structuring content, provide SEO descriptions and meta tags, and suggest edits based on feedback or GitHub issues. 
* Generate alt text for images based on file names or interpreting the images.
* Read the source code, explain what it does, and provide examples of its use.
* Target notifications to appropriate SMEs for reviews.
* Generate a syllabus or course outline for onboarding customers or employees.

To get useful responses from an AI tool, be specific with your `prompts <https://www.huit.harvard.edu/news/ai-prompts>`__. Consider asking the same or similar prompts several times — perhaps with different personas — to get pertinent responses. The AI does NOT replace you; you still need to review and evaluate any responses before using them.

Several people suggested developing an AI/LLM strategy to sell to stakeholders. This could include two lists: where AI could help and where AI should NOT be used. As part of the strategy, consider whether to expose any company information to a public LLM.

See more Write the Docs resources about `AI and LLMs </topics/#ai-and-llms>`__.



*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------
Featured job posts
------------------

`Developer Documentation & DevRel Engineer <https://celiumcompute.ai/jobs>`__, Datura AI - *Full-Time, Remote*, Compensation: USD 150k base + meaningful equity

*Interested in promoting your open position? See our* `job posting sponsorship </sponsorship/jobs/>`__ *for more details.*

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>`__ in one of the many `channels </slack/#channel-guide>`__.

----------------
Events coming up
----------------

- 11 Jul, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/306334002/>`__
- 24 Jul, 18:30 BST (London, United Kingdom): `Building with Words: Scaling enterprise docs and community <https://www.meetup.com/write-the-docs-london/events/308437038/>`__
- 25 Jul, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/306334003/>`__
- 7 Aug, 18:00 PDT (San Francisco, USA): `Call for Speakers: 5-Minute Talks on Tech Writing Tools <https://www.meetup.com/write-the-docs-bay-area/events/308417050/>`__
- 8 Aug, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/307540179/>`__
- 22 Aug, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/307540180/>`__
- 5 Sep, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/307540181/>`__
- 9 Sep, 19:00 MDT (Calgary, Canada): `Write the Docs Calgary September 2025 Meetup <https://www.meetup.com/wtd-calgary/events/304868570/>`__
