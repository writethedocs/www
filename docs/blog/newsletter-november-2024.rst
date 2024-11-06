:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: November 05, 2024
  :tags: newsletter

#########################################
Write the Docs Newsletter – November 2024
#########################################

Greetings, documentarians. In these bustling days of news and planning, I hope you are able to find moments of calm for yourselves to appreciate what is going well.

If you have enough calm and want some inspiration, good news: The Write the Docs Australia conference is coming soon! Tickets close on Saturday 16 November, so `get your tickets <https://www.writethedocs.org/conf/australia/2024/tickets/>`__ while you still can.

The `WTD Salary Survey for 2024 <https://salary-survey.writethedocs.org/>`__ is now open! New this year: you can fill the survey out as both an employee and contractor if you've worked as both during the past year; answers can be edited before the final submission; and for privacy, salary/rate fields are masked by default. Head on over and share your insights – each contribution helps build a clearer picture of what fair, equitable, and transparent compensation looks like in our industry. Full-time or part-time, permanent or contract, working or currently between jobs – we want your input!

And in the newsletter this month, we have insights into whether to use emoji in docs, whether you need to know a tool before applying to work with it, and dealing with assets with docs-as-code. Enjoy!

----------------------------------------------
Emoji in documentation: :yes-please: or :yuk:?
----------------------------------------------

Emoji seem to find their way into documentation more and more often these days... but is that a good or a bad idea? Well, like everything else, it depends! A sprinkling of emoji can work well in some cases and cause more problems than they're worth in others.

Emoji can help achieve an inviting and approachable tone for certain types of documentation, such as quick start guides. Because emoji can make content feel less dense and more engaging, they may be especially appropriate for contexts such as presales documentation, where a whiff of marketing-speak is acceptable. Emoji may also be used to differentiate a new product from existing enterprise offerings. And emoji in tables can make the information easier for readers to scan, although icons used as inline images can achieve the same thing.

On the other hand, emoji can cause accessibility issues because they aren't necessarily interpretable by assistive technology. (For details, read `Do emoji and accessibility work together? <https://www.tiny.cloud/blog/emoji-and-accessibility/#accessible-emoji>`_ by Di Mace.) The meanings of emoji may be interpreted differently across cultures, so you risk sending a different message than you intended when you use emoji. Emoji can be distracting or even inconsiderate to a confused reader. Documentarians may also spend a lot of time trying to use emoji to affect a chatty tone instead of writing clearly and end up with content that doesn't actually explain anything. It's best to carefully consider your audience and approach emoji use with caution.

----------------------------------------
Are tool experience requirements a myth?
----------------------------------------

Job postings often request experience with specific tools. Recently, in the `#career-advice channel <https://app.slack.com/client/T0299N2DL/C6ADX1YVA>`__, a job seeker asked how important this is for experienced documentarians.

The general consensus was that lack of experience with a specific tool shouldn’t prevent someone from applying for a position. Documentation managers want people who can understand and write clearly and concisely about technical concepts and related procedures. Possibly, experience with a specific audience (or domain) may be important. In fact, many mentioned that throughout their careers their various employers (or even the same company) used different tools.

A hiring manager focused on how quickly the person can get up to speed with the team. If you’re a quick learner, have experience with other relevant tools, and are self-motivated enough to self-study (if necessary), lack of specific tooling experience isn’t a problem. If you don’t have experience with a specific tool, use an interview to relate how you learned other tools.

Several concerns included:

* **If your resume doesn’t mention ANY tool specified in a job posting, the application may get rejected automatically.** This is particularly true if you’re going through a recruiter. It may be worthwhile to gain at least a novice-level exposure to include on your resume. (Don’t lie about your experience.) Many tools are either free or have free trials available.
* **There may be some basic tool-related knowledge that’s expected with certain types of documentation.** If you’re transitioning to another domain, consider getting at least minimal exposure to relevant knowledge (such as Markdown, Git, or HTML). 
* **Some "tools" are actually concepts.** You may want to research what certain items (such as DITA, distributed systems, or version control) involve so you can discuss them.

Some companies do expect to train new hires. If nothing else, new hires need to learn the way the team uses a particular tool. If hired, be prepared to learn from others even if you have experience with their tools.

----------------------------------------------------
Dealing with images and other assets in docs-as-code
----------------------------------------------------

A couple of recent questions regarding `#docs-as-code <https://writethedocs.slack.com/archives/C72NZ18FR>`__ touched on how to handle binary files such as images in a docs-as-code setup, which is primarily built to track text files. One concern was the size of the binary files, which can make a Git repository balloon up to gigabytes in size. Another issue was whether to store images next to the file they're used in or in a separate directory only for images.

Unsurprisingly, the answers on what to do varied based on what was required. For example, if you only need simple diagrams, you can create them using a diagrams-as-code tool such as `Mermaid <https://mermaid.js.org/>`__ or `PlantUML <https://plantuml.com/>`__ and track them like any other text file. If you need large files, such as computer-aided design (CAD) files or videos, you might want to look into `Git Large File Storage <https://git-lfs.com/>`__ to point to the files in a separate location.

If you land somewhere in between, your organizational options may depend on your build tool. Some require images to be stored in specific places to take advantage of their workflows. If your tool is more flexible, consider whether you're likely to reuse the images across docs. If not, consider storing the images in a subdirectory with the doc. For example, `src/get-started/intro.md` could have images like `src/get-started/img/flow.png`. Doing this keeps files organized by topic.

If you will reuse images, consider storing all images within a single directory, which you can separate into subdirectories by topic or product. When images are separate from the docs, see if you can use a helper tool like a `path autocomplete extension for your IDE <https://marketplace.visualstudio.com/items?itemName=ionutvmi.path-autocomplete>`__ to make writing the locations easier.

------------------
Featured job posts
------------------

`Technical Documentation Lead <https://nutrient.bamboohr.com/careers/161>`__, Nutrient (Remote)

Interested in promoting your open position? See our `job posting sponsorship <https://www.writethedocs.org/sponsorship/jobs/>`__ for more details.
----------------
Events coming up
----------------

- 12 Nov, 19:00 MST (Calgary, Canada): `How a Technical Writer can Drive a Successful QMS Implementation <https://www.meetup.com/wtd-calgary/events/297725838/>`__
- 15 Nov, 08:30 EST (East Coast Quorum, USA): `Social Hour for Documentarians <https://www.meetup.com/boston-write-the-docs/events/304215988/>`__
- 19 Nov, 18:45 EST (Washington, USA): `2024 WTD DC End of Year Happy Hour <https://www.meetup.com/write-the-docs-dc/events/304260278/>`__
- 20 Nov, 18:00 CET (Berlin, Germany): `WTD Berlin @ JetBrains - Svetlana Novikova - Beyond static docs <https://www.meetup.com/write-the-docs-berlin/events/303511106/>`__
- 20 Nov, 18:00 CET (Stockholm, Sweden): `Let's talk about tools and processes, AI or not <https://www.meetup.com/write-the-docs-stockholm/events/304197266/>`__
- 21 Nov, 17:00 PST (Portland, USA): `AI for Documentarians: Write the Docs PDX + PSU Annual Supermeetup <https://www.meetup.com/write-the-docs-pdx/events/304352066/>`__
