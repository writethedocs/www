
.. post:: May 02, 2022
   :tags: newsletter

####################################
Write the Docs Newsletter – May 2022
####################################

Hi everybody!

It's Beth here, joining you for my last email as editor. It's been a real privilege to take up space in your inbox these past few years - thank you for reading! I'll let our new editor introduce himself in the next edition, but I'm excited to see someone new taking the reins, and I'm sure he's going to do a fantastic job.

In community news, hopefully all of you going to the virtual Portland conference have seen that the `schedule </conf/portland/2022/news/announcing-schedule/>`__ is out, but sharing the link again just in case. For those of you more in my European neck of the woods, you might like to know that we've announced `dates for the virtual Prague conference </conf/prague/2022/news/welcome/>`__: 11th-13th September. And if you think you have some ideas that you might like to share - please check out the `Call for Proposals </conf/prague/2022/news/announcing-cfp/>`__, and consider giving a talk. The CFP is open til 30th June.

And with that, let's see what we've learnt on Slack during April!

-------------------
Link-checking tools
-------------------

This month, a question about useful tools for checking links in HTML output prompted several suggestions. Some have built custom link-checking tools, but there are plenty of ready-to-use open-source options too. Here's the roundup:

* `htmltest <https://github.com/wjdp/htmltest>`_ was most suggested, based on fast performance and configurability. htmltest is also especially suitable for link testing in continuous integration environments -- you can check links in HTML files in a folder, with no need to run a web server.
- `Muffet <https://github.com/raviqqe/muffet>`_ is another fast and thorough link-checking tool, with pretty-printed or JSON output. There's also a GitHub Action that uses Muffet, `My Broken Link Checker <https://github.com/ruzickap/action-my-broken-link-checker>`_, although you may have to adjust Muffet's maximum requests per second to accommodate GitHub rate limits.
- `HTMLProofer <https://github.com/gjtorikian/html-proofer>`_ validates all HTML output, including internal and external links, image references and alt tags, and scripts. You can run HTMLProofer on one file, a directory, and arrays of directories and links, and it's also highly configurable.
- `LinkChecker <https://github.com/linkchecker/linkchecker/>`_ gets the job done, and it's documented! Find detailed information and configuration options at the `LinkChecker documentation site <https://linkchecker.github.io/linkchecker/index.html>`_.

-----------------------------------
What's in a (role) name, after all?
-----------------------------------

A recent question about whether the job title "programmer writer" represents something different from a "technical writer" produced a wide-ranging conversation about job titles, software history, career paths, interviewing tips, and more. Here's how the community weighed in:

* Job titles for documentation work vary wildly between companies. In some, there might not be a difference; in others, a programmer writer might be expected to write at least sample code, and possibly entire example applications.

* Responsibility for engineering of docs tooling can be part of a programmer writer's job; it's less often associated with a technical writer's work. (Sometimes these folks are called documentation engineers.)

* Most assume that programmer writers have experience as software developers, and then move to focus on documentation (likely for other developers). API docs are more often associated with the work of programmer writers, together with associated code samples.

* A related role is "developer advocate", or "developer evangelist". These roles have the added responsibility of engaging with developer communities, through social media and online forums.

* Several people associated the title "programmer writer" with AWS/Amazon or with Microsoft. And one seasoned programmer writer let us know that this particular title was in fact coined by Microsoft many years ago, and was part of a continuum that included "consumer writer" and "technical writer". The distinctions reflected not only degrees of technical/coding expertise, but also differences in audience: programmer writers wrote for developers, technical writers for other technical audiences (eg system administrators), and consumer writers for "all of humanity". But that level of distinction belonged to the time when Microsoft employed more than 1800 writers (!!)

------------------------------------------------------
Is written content outdated - and it's time for video?
------------------------------------------------------

In the world outside technical writing, video has become hugely popular; but most documentation is still in written form. Is written content outdated? Is it time to pivot to video? Obviously, the question about it this month provoked major debate.

Those in opposition to video say the main problems are the inaccessibility of video content: they're not searchable, so users cannot quickly browse the video to find what they need. Another issue is the ineffectiveness of video interface controls, which prevents users from adjusting the video to their liking, such as by slowing down the speed or pausing in exactly the right place. Plus there are the  business problems. Efforts to create videos may be considered too labor-intensive or may be disrupted if resources are limited, as videos require specialized skills that can be costly to employ.

On the other side, proponents of video content say it can provide a lot of value - if done right. That is, videos should be brief, limit extensive hands-on engagement, apply accessibility best practices like captions and timestamps, and be professionally edited to establish credibility. Another way to ensure video content is well-received is to consider its optimal use. For example, videos are excellent when used as product demos but may not be ideal if used as the sole means of information in the product documentation.

It's crucial to recognize when video content is valuable and when it is not; it comes back to the key goals of documentation, delivering value to users and facilitating understanding. None of the participants felt that video content could completely replace written content - but it can certainly be used to supplement it.

-----------------------------------
Templates for concept documentation
-----------------------------------

Most of us have written concept or explanatory documentation at some point. But unlike procedures, which are easier to formalize, concept docs can vary hugely in form - it all depends on the ideas you're trying to explain. So is it possible to have a template for concept docs?

One community member suggested a rough outline:

- Present the context and the `learning objective <https://www.sciencedirect.com/topics/social-sciences/learning-objective>`__ for the page.
- Start with an overview of the concept and problem space - something like a Wikipedia-style `lead section <https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Lead_section>`__.
- Break down the concept into smaller pieces, and explain those in turn.
- Anchor each explanation with examples.
- Link to action oriented content - what a reader can do with their new understanding.

But it's hard to be much more prescriptive than this, because the form of an explanation article depends strongly on its scope. And figuring out the scope is a fundamental part of the challenge. It should be grounded in **who** is going to read it and **for what**. You'll need to draw the boundaries around the domain, and then explain both what's inside, but also the key relationships to the things outside.

So the answer is: we haven't yet figured out a detailed template. Sorry! But for the meantime, there are some more lightweight outlines: 

* `Concept template with guidance <https://docs.google.com/document/d/17PJ6kOazLiLSl0465sZcUbujh_g9_g6WKOv1IcxQDPs/edit#>`__ (Google doc) 
* `Concept template <https://github.com/platformsh/platformsh-docs/blob/main/docs/templates/concept.md>`__ (GitHub file)
* `Good Docs project template <https://github.com/thegooddocsproject/templates/blob/dev/explanation/template-explanation.adoc>`__, with `guidance <https://github.com/thegooddocsproject/templates/blob/dev/explanation/about-explanation.md>`__ (GitHub files)

------------------
What we’re reading
------------------

The #bipoc group’s been discussing the following materials on diversity, inclusion, and equity. Want to join the conversation? Please join us in the `#bipoc Slack channel <https://writethedocs.slack.com/archives/C016STMEWJD>`_!

A short read: Employees are calling for more salary transparency. HR Advisory shares how `being more transparent with salary increases equity <https://www.hradvisory.com/blog/increase-transparency-and-equity-with-salary-ranges>`_.

A short read: Axios reports that in the United States, `the government is making an effort to address equity <https://www.axios.com/biden-administration-equity-plan-29a81cd8-bbf7-4e61-8682-4cdb68a1c524.html>`__. You can `read more about this effort <https://www.whitehouse.gov/equity/>`__ on the official Whitehouse site.

A medium read: Having conversations about inclusion can be uncomfortable. Even anticipating conversations can cause anxiety. `Why inclusion means getting comfortable with discomfort <https://www.forbes.com/sites/ellevate/2020/12/30/why-inclusion-means-getting-comfortable-with-discomfort/?sh=932bd7975d68>`_ from Forbes names this discomfort and offers strategies to overcome it.


------------------
Featured job posts
------------------

- `Technical Communications Director <https://jobs.writethedocs.org/job/688/technical-communications-director/>`__, Fivetran (Oakland CA / Remote)
- `Senior Curriculum Editor <https://jobs.writethedocs.org/job/689/senior-curriculum-editor/>`__, MongoDB (New York NY / Remote)
- `Senior Technical Writer, Cloud <https://jobs.writethedocs.org/job/690/senior-technical-writer-cloud/>`__, MongoDB (Remote - North America)
- `Manager, Technical Documentation <https://jobs.writethedocs.org/job/691/manager-technical-documentation-remote/>`__, New Relic (Portland OR / Remote)
- `Technical Writer <https://jobs.writethedocs.org/job/649/technical-writer/>`__, Semaphore (Remote)
- `Technical Writer <https://jobs.writethedocs.org/job/692/technical-writer/>`__,  Adecco (Remote / Hybrid)
- `Technical Content Creator - Docs as Code <https://jobs.writethedocs.org/job/695/technical-content-creator-docs-as-code/>`__,  Vulnerability Research Labs (Columbia MD, USA)
- `Senior Technical Writer (DITA/XML) <https://jobs.writethedocs.org/job/658/senior-technical-writer-dita-xml-remote-european-timezones/>`__, Talarian (Remote - Europe)
- `Technical Writer <https://jobs.writethedocs.org/job/701/technical-writer/>`__, Neon, Inc. (Remote)
- `Senior Content Marketing Manager <https://jobs.writethedocs.org/job/708/senior-content-marketing-manager/>`__, Metaplane (Remote)

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

------------------------
Virtual events coming up
------------------------

- 03 May, 19:00 PST (Bay Area) - `Writing code examples for technical documentation <https://www.meetup.com/Write-the-Docs-Bay-Area/events/285255019/>`__
- 10 May, 08:30 EDT (New England) - `Morning social <https://www.meetup.com/ne-write-the-docs/events/hqvdfsydchbnb/>`__
- 10 May, 19:00 MDT (Calgary) - `Write the Docs Calgary Meetup <https://www.meetup.com/wtd-calgary/events/282708696/>`__
- 18 May, 19:00 EDT (Toronto) - `Write the Docs Toronto <https://www.meetup.com/Write-the-Docs-Toronto/events/mnpqgsydchbxb/>`__
- 22-24 May (Pacific Time zone) - `Write the Docs Portland virtual conference <https://www.writethedocs.org/conf/portland/2022/>`__
- 24 May, 08:30 EDT (New England) - `Morning social <https://www.meetup.com/ne-write-the-docs/events/hqvdfsydchbgc/>`__

