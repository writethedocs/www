
.. post:: February 03, 2021
   :tags: newsletter

#########################################
Write the Docs Newsletter – February 2021
#########################################

Hey everyone! It's a month into 2021 already and the newsletter team is back in business. We've got a packed issue for you today, with topics ranging from screenshots to embedded code snippets to showing your value, so I'll get right on with it.

Just a couple of announcements today: the East Coast Quorum meetup is holding its first virtual event this month! It's on "Lessons learned open-sourcing GitHub Docs", and it'll be on Monday 22nd February at 19:30 Eastern Time. If you're interested, `sign up to attend <https://www.meetup.com/virtual-write-the-docs-east-coast-quorum/events/276054186/>`__. We also have a proposed Write the Docs Enhancement Proposal (WEP) focused on Slack moderation. There is an `open pull request <https://github.com/writethedocs/weps/pull/4>`__ with the proposal for ``WEP2``, and the community feedback period lasts until March 5.  

So what's been happening on Slack?

------------------------------------------
Getting the balance right with screenshots
------------------------------------------

In December, documentarians had a lively discussion about how many screenshots to include in docs. As you might imagine, perspectives ranged from "absolutely no screenshots ever" to "as many screenshots as possible," but the most common opinion was "it depends" (surprise!). Most said they try to help both users who like a visual walkthrough _and_ users who prefer to follow text instructions. One writer approached the problem by presenting text explanations as the default, with an optional collapsible version that includes screenshots.

Fewer screenshots means less maintenance work. If the product changes, the screenshots must change too, to remain helpful and prevent confusion. Lots of screenshots plus frequent product changes can cost a lot of time: keeping the docs in sync with the product can become unmanageable.

A middle-ground approach is using text descriptions of UI elements, like "Click the START button", as it's easier to keep text descriptions matching the UI. And well-designed user interfaces and UI microcopy often mean that users don't need screenshots to find their way through the product.

What about a video walkthrough or GIFs? Again, documentarians were split: it's helpful to watch a process through before trying it yourself, but videos and GIFs are inaccessible for people with visual impairments, distracting for people with attention issues, and unusable for people who don't have dependable broadband service. And following video instructions can be frustrating if you have to repeatedly press pause, or feel like the pace of spoken instructions is too slow.

For more on screenshots in documentation, check out Steve Stegelin's `Graphic Content Warning: The Pros, Cons, and Alternatives to Screenshots <https://www.writethedocs.org/videos/portland/2018/graphic-content-warning-the-pros-cons-and-alternatives-to-screenshots-steve-stegelin/>`_ from Write the Docs Portland 2018 and Swapnil Ogale's `When bad screenshots happen to good writers <https://www.writethedocs.org/videos/eu/2016/when-bad-screenshots-happen-to-good-writers-swapnil-ogale/>`_ from WTD EU 2016.

--------------------------------------
Report from the book club: managing up
--------------------------------------

This winter, the `Write the Docs book club <https://app.slack.com/client/T0299N2DL/C7YJR1N02>`__ is reading and discussing their way through  Managing Writers by Richard Hamilton. The book covers a broad range of topics on the overall subject of managing docs projects and teams (both big and small). There’s been some fab discussion every week, so here’s a sample on the theme of showing your value and finding your place in the org.
 
It seems that it’s often part of a tech writer’s job to manage up, teaching both your peers and higher-ups about the value that both you and docs bring. Not easy, but the book club has some tips!

First up, behave like other, more-established roles. If they document their processes in a wiki, do the same. Announce big docs changes just as you’d announce product changes.

Also, look at the interpersonal dynamics. Tech writing often needs a lot of input from other roles - if this is seen as a zero-sum exchange that doesn’t benefit the other person, it’s not gonna work. You can mitigate this by doing your research up front to show you respect their time; by seeking out opportunities to help them with other things, so you’re giving back; and by emphasising your common goals, so it’s not us vs them.

Several people saw this as a question of proving your value. Gathering data about the impact of docs programs makes a difference - yes, analytics, but also customer feedback (especially praise). It can take many years to establish your role as valuable, but one good sign you’ve gotten there is if you start to get overloaded. If you’re turning down work, you’ve probably proven value!

------------------------------------------
Where is the best home for documentarians?
------------------------------------------

On a very related theme: when you're trying to establish docs in an organisation, where you sit in the org makes a big difference. You’ll find docs folks reporting to a huge variety of areas, all with their pros and cons - as per a discussion in #general this month.

Lots of contributors felt that engineering was a “natural” place to report into. It makes it easy to know what product changes are coming, and often helps with getting support for the tooling you need. A downside is not being that close to customers, and sometimes the user perspective can be lacking.

It’s also common to report into product management. If PMs call the shots in the company, this can be great! Their job is to know customer needs really well, so they’ll often see clearly how docs provide value. On the flip side, because product management is a lot about prioritisation, it can be hard to get support for low priority projects. And PMs are often a cycle ahead, looking to the future rather than the work you have to get done now.

Some others report into support. The deep customer connection here can be awesome, as can the fact that your job in writing documentation helps reduce the load on your coworkers. Be wary, though: it's an uphill struggle if docs work is seen as an afterthought to day-to-day customer support.

One final thought is that the best place is so dependent on you personally. Writers with strong engineering or UX skills may be happiest in product development teams, but that’s not all of us. And as one documentarian pointed out: there’s rarely one place in the org that ticks all the boxes. You’ll probably need strong communication lines across several orgs, no matter which one of them you call home.

------------------------------------------
The many paths to code samples from GitHub
------------------------------------------

Many of us struggle with managing code snippets in the docs. Do you embed them inline, or do you host them elsewhere? and if the latter, how do you connect them? A question about how to embed code samples from GitHub produced a range of options:

* Link to specific lines of code in GitHub. To keep the link stable you can specify a file version, or a pull request too.
* Write code to directly embed the snippets you need. Some WTDers have written custom solutions for this, or there's a `small OSS project <https://github.com/finom/github-embed>`__ hosted (where else?) on GitHub.
* Work with GitHub gists, which enjoy many of the version tracking advantages of a GH code repository. And GitHub Actions let you automate pulling code from a repository into a gist.

Some of the conversation also turned to the larger context for the original question: how do you keep your code snippets not only up-to-date but tested? Folks seemed to strongly prefer either solutions that focused on testing the code without worrying about the docs context, or tools such as Katacoda that let you provide interactive tutorials.

------------------
Featured job posts
------------------

- `Developer advocate with documentation skills <https://jobs.writethedocs.org/job/270/developer-advocate-with-documentation-skills/>`__, Read the Docs (remote: UTC-8 to +2)
- `Senior Technical Writer <https://jobs.writethedocs.org/job/271/senior-technical-writer/>`__, ChartHop (remote: North America)
- `Technical Editor <https://jobs.writethedocs.org/job/273/technical-editor/>`__, Semaphore (remote)
- `Technical Writer - Developer Docs <https://jobs.writethedocs.org/job/276/technical-writer-developer-docs/>`__, Uber (remote now, California in the future)

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

------------------------
Virtual events coming up
------------------------

- 15 February, 7pm GMT+1 (Europe) - `What skills and competencies do documentarians need? <https://www.meetup.com/Write-The-Docs-Berlin/events/276123636>`__
- 17 February, 7pm PST (Toronto) - `Write the Docs Toronto <https://www.meetup.com/Write-the-Docs-Toronto/events/rwphwryccdbwb/>`__
- 22 February, 7:30pm EST (East Coast US) - `Lessons learned open-sourcing GitHub Docs <https://www.meetup.com/virtual-write-the-docs-east-coast-quorum/events/276054186/>`__
- 23 February, 6pm EST (Ottawa) - `WTD Ottawa Shopify Meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqyccdbmb/>`__
- 9 March, 7pm MST (Calgary) - `March 2021 Write the Docs Calgary Meetup <https://www.meetup.com/wtd-calgary/events/275761130/>`__
- 10 March, 12pm AEDT (Australia) - `GitHub Open Source docs | Doc Product Ownership <https://www.meetup.com/Write-the-Docs-Australia/events/276122418/>`__
