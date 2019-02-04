.. post:: February 4, 2019
   :tags: newsletter

#########################################
Write the Docs Newsletter – February 2019
#########################################

Hello, Write the Docs people! Beth here, wishing you all a happy 2019. Is it too late in the year for that? Oh well, never mind. I'm doing it anyway.

We've got a little something for you this month. There's tons of useful stuff hidden away in the `newsletter archive </blog/archive/tag/newsletter/>`_, and it's a shame that it's not very discoverable. So, in an appropriately documentarian fashion, we've had a go at fixing that by creating an `index of all the topics </newsletter/#index-of-newsletter-topics>`_ covered by the newsletter over the last few years. We hope you like it!

In other news, on the conference front: we now have `dates for the 2019 Prague conference </conf/prague/2019/news/prague-19-dates/>`_! It'll be 15th-17th September, back in the gorgeous Auto Klub. Ticket sales and call for proposals should open in March - keep your eyes peeled.

Onto our stories! What has the community been talking about on Slack recently?

--------------------------------------
Agile delivery and continuous releases
--------------------------------------

How do you successfully deliver documentation when features roll out continuously... as in every two weeks?

It turns out that plenty of documentarians have been in this situation, and most agreed it's a challenge. But there are upsides: shorter intervals between releases lower the stakes of any one release and give you a chance to fix problems more quickly. Here are some of the approaches that the community offered up:

* If you can, automate release notes. For example, if you make sure that the folks writing Jira issue descriptions know they are user-facing, you can make issue descriptions into release notes. You can also use Jira fields to sort issues into categories like "Fixed" and "Known Issue".
* Participate in dev and product meetings, especially requirements discussions. Use your notes as a starting point to revise as things get added, changed, or removed.
* Keep an eye on future documentation needs. Join backlog refinement meetings and get the product roadmap so you know what's coming up.
* Keep release notes brief. Capture feature details in a separate document that you can develop into full documentation when the time is right.
* Communicate documentation status to users. If code has shipped but docs are in progress, make it clear that documentation is being updated. Be explicit when a feature is released but still in testing.
* One suggestion was to follow the `Azure DevOps release notes process <https://channel9.msdn.com/Blogs/DevOps-Interviews/Interview-with-Aaron-Bjork-Release-Notes>`_.

---------------------------------------------
Personal development goals for documentarians
---------------------------------------------

A recent question about personal, work-related development goals produced quite a thread, and brought many common interests to the fore. Here are some of the areas that members of the community want to develop in 2019 - we are evidently a group driven to expand our horizons!

* **UI/UX**. Several people wanted either to move in this direction in their careers, or to polish their skills in their present positions.

* **Public speaking**. This one really resonated, with some folks pursuing Toastmasters, others looking to give presentations on specific topics, and still others committing to submit proposals for conferences.

* **New languages**. Not just programming languages, but human languages too! We're an international community with contributors who work for international companies, and language skills can really help bridge communication gaps.

* Other ideas included working on graphics and illustration skills, contributing to tech communities (new meetups, new conferences, new outreach groups), and working more deeply with the products you document - especially if they're for developers or sysadmins.

-------------------------------------------
Tips for lone writers starting from scratch
-------------------------------------------

We have so many people who are the only writer in their company that there's a channel for it: `#lone-writer <https://writethedocs.slack.com/messages/lone-writer>`_. If you're in that position for the first time, here's some advice from the channel:

* Start small. You might want to raze all the content to the ground and start again, but taking it one step at a time is more realistic.
* Be open to change. Your processes should evolve over time, especially when you're first starting - some things you try will work, and some things just won't.
* Rather than crafting a style guide from scratch, save time by adopting an existing public style guide. 
* Help others understand what you're there for. Give a presentation explaining what you're here to do, what your plans are, and what you need from others.
* Help others to help you. Consider writing docs using a tool that allows developers to contribute.
* Don't be hard on yourself when things move slowly. Making things better takes a long time; don't strive so hard for perfection that you lose heart.

Some useful resources:

* `Bootstrapping Docs at a Startup </videos/na/2017/bootstrapping-docs-at-a-startup-jesse-seldess/>`_ - Jesse Seldess, Write the Docs Portland 2017
* `Where Do I Start: The Art and Practice of Documentation Triage </videos/portland/2018/where-do-i-start-the-art-and-practice-of-documentation-triage-neal-kaplan/>`_ - Neal Kaplan, Write the Docs Portland 2018
* `The Lone Writers Guide <https://github.com/San-Francisco-Write-The-Docs/lone-writers-guide>`_ - GitHub project. It's a work in progress, and they welcome contributions!

--------------------------------------------------
Documenting APIs with "interesting" design choices
--------------------------------------------------

Recently, a documentarian asked about documenting APIs, which led to a larger conversation about API design. The original question was: how to document how to use an endpoint that deletes all objects by default - unless you pass in a filter to control what gets deleted.

The unanimous response was that this is not a good design. Bulk deletions themselves are a reasonable feature. But having an API endpoint that *defaults* to deleting everything is a problem, because it makes it too easy for users to accidentally do irreversible damage.

We did discuss a few ways that you could approach writing that documentation: 

* "By default, deletes all objects. Optionally, ..."
* ":exclamation: Warning :exclamation: Be careful here!"
* All caps and bold to draw attention.

But really, the design needs to be improved. There are safer approaches to bulk deletion: for example, the endpoint could require a filter parameter, and allow a wildcard value that allows bulk deletion. Users can still bulk delete, but this makes it a more deliberate action. 

The takeaway is that you cannot save a bad design with documentation. Not even by documenting the bad design in bold and all caps.

-----------------------
Job board: your ad here
-----------------------

The `Write the Docs job board <https://jobs.writethedocs.org/>`_ is a great way to get your open positions in front of thousands of docs folk all around the world. Any jobs posted as a ‘featured’ listing will be included in the next newsletter.

--------------------------
Community events coming up
--------------------------

- 6 February - Brisbane, Australia - `Technical writing in a global, remote-first, blockchain startup <https://www.meetup.com/Write-the-Docs-Australia/events/257010961/>`_
- 9 February - Bengaluru, India - `Analytics in documentation, and updates from KubeCon <https://www.meetup.com/Write-the-Docs-India/events/258435186/>`_
- 12 February - Seattle, IL, USA - `Seattle morning social <https://www.meetup.com/Write-The-Docs-Seattle/events/258146549/>`_
- 12 February - Portland, OR, USA - `Lightning talks <https://www.meetup.com/Write-The-Docs-PDX/events/258360351/>`_
- 12 February - Barcelona, Spain - `Agile for documentarians <https://www.meetup.com/Write-the-Docs-Barcelona/events/258493254/>`_
- 13 February - Manchester, UK - `Introduction to Open API specification <https://www.meetup.com/Write-the-Docs-North/events/256937446/>`_
- 20 February - Chicago, IL, USA - `Writing API documentation <https://www.meetup.com/Write-the-Docs-Chicago/events/257760901/>`_
- 20 February - Toronto, Canada - `Hiring technical writers <https://www.meetup.com/Write-the-Docs-Toronto/events/pcqbmqyzdbbc/>`_
- 21 February - Sydney, Australia - `First meetup of 2019 <https://www.meetup.com/Write-the-Docs-Australia/events/258194900/>`_
- 21 February - Pasadena, CA, USA - `Food, drinks, docs! <https://www.meetup.com/Write-the-Docs-LA/events/258597898/>`_
- 26 February - Ottawa, Canada - `Structured authoring unconference <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqyzdbqb/>`_
- 18 March - Berlin, Germany - `Docs hack <https://www.meetup.com/Write-The-Docs-Berlin/events/bkgmpqyzfbxb/>`_
- 20 March - Manchester, UK - `Genesis of a specialist marketing agency <https://www.meetup.com/Write-the-Docs-North/events/256937497/>`_
