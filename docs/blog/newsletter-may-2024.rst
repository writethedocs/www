:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: May 06, 2024
    :tags: newsletter

#########################################
Write the Docs Newsletter – May 2024
#########################################

Hello once again, fellow documentarians. I hope all is well with you and yours.

Our online Atlantic conference is planned for September and there's still time to get your proposal in to speak. Check out the `Call for Proposals </conf/atlantic/2024/cfp/>`__ and get your ideas in by May 15. The Atlantic conference welcomes speakers from around the world and you don't even have to travel to give the talk. So if you've ever considered giving a talk before, send in your proposal and give it a try.

If you'd like some inspiration from past speakers, the Portland conference wrapped up since our last newsletter. See the `conference recap </conf/portland/2024/news/thanks-recap/>`__ and see `videos of all the talks <https://www.youtube.com/playlist?list=PLZAeFn6dfHpm4FboYSTD1Bs8Yp8k_JvAL>`__ to get a taste of what the conference was like. And then get inspired and `submit a talk for Atlantic 2024 </conf/atlantic/2024/cfp/>`__!

In other exciting news... the 2023 Documentation Salary Survey results are out! Thanks to a record number of submissions and finer-grained location data, we are able to publish median salaries for many more regions that we have been able to cover previously. And it's possible, we're also showing more data on salaries, such as the 25th and 75th percentile values. For all the numbers, head over to the `2023 salary survey results </surveys/salary-survey/2023/>`__.

In the newsletter this month, we have great topics for you about announcing deprecations, how technical communications can gain prestige, tracking metrics about your docs, and whether a docs-as-code approach is worth it. Enjoy!

------------------------------
Announcing Feature Deprecation
------------------------------

This month's Slack discussions included best practices for announcing feature deprecation in documentation. Before you update your docs, it's important to note that deprecation is not the same as removal. Deprecation means that a feature will be unsupported at some point and possibly removed in the future, even though it's currently supported.

The most important element of announcing deprecation is an abundance of communication with as much notice as possible. Most writers said they cover feature deprecation in the release notes, often in a dedicated section. Others mentioned a wider strategy that includes the release notes as well as special flags for docs pages that cover the feature, direct customer emails, and announcements in the product itself. Some even have a dedicated page in the docs for deprecated features. Deprecation that involves a change in how a feature behaves, especially if the change will happen automatically, requires especially careful, emphatic communication.

In terms of the content of deprecation notices, you should cover what's being deprecated, how it will affect customers, required actions, mitigation options, and recommended replacements. You might also include the reasoning for deprecation (or a link to the reasoning, if it's explained elsewhere). Opinions are split on whether to mention dates associated with deprecation. Some feel that it's important to provide a good-until date or release number to reassure customers that the feature isn't going to disappear. Others point out that it's best to give customers as much notice as possible without committing to a specific timeline for removal -- once a feature is deprecated, customers should no longer rely on it.

-----------------------------------------------------
Should Technical Communication Be Its Own Department?
-----------------------------------------------------

Many documentarians believe that, due to the lack of visibility among company officers, documentation efforts tend to be underfunded and understaffed. A recent exchange discussed whether a company-level documentation department (for example, VP of Technical Communications) would promote effective technical documentation and aid in recognition of the value that documentarians contribute. 

One person did report working once under a documentation executive, but it didn’t work out well because the VP lacked the necessary resources (including budget and personnel). So for any documentation VP, the company must commit resources needed for the department to be effective. 

One persistent reason resources aren't committed to documentation efforts is that marketing-related content has a direct relationship to the bottom line (usually through sales-oriented metrics), but technical documentation is often considered a cost center. Poor documentation may not be a factor when deciding on a product because purchases and subscriptions are not necessarily handled by the people that use them. So the people that use a product sometimes have to figure out how to work with it.

Military and aerospace contracts include provisions for support and support costs get minimized with effective documentation. Therefore, documentarians may be seen as necessary team members if support is considered part of the bottom line.

Some people indicated that they, as documentarians, are under Technology, Product, Engineering, Support, or even Marketing VPs and that they have been in effective documentation departments. They don’t see a need for an a documentation VP.

Could it make sense to have one high-level department for both technical documentation and marketing-related content, such as VP of Communications? The benefit of having one department for both may be consistent usage and branding, but in many companies this is achieved by having style guides (and other related job aids) and branding guidelines. But, of course, these are only effective for company-wide consistency when actually used.

---------------------
Docs Metrics To Track
---------------------

When tracking documentation metrics, the goal is to discover essential insights regarding its efficacy and user engagement. However, deciding which metrics to track and if they are useful requires considerable analysis. An Unconference session at the Portland conference sparked a recent discussion in the `#analytics channel <https://writethedocs.slack.com/archives/C5WF43X6G>`__ on this analysis.

One important indicator is customer satisfaction, which can be analyzed using surveys or feedback methods. Understanding whether documentation fits user demands and whether users would suggest it to others can help determine its utility and quality. Also, tracking support requests for documentation might indicate areas that need improvement and typical customer pain points.

Page views, time spent on pages, and scroll depth are examples of content-use metrics that give information about user behavior and engagement. Knowing which themes are most popular and how much people interact with the content helps you prioritize updates and changes.

Another significant statistic is how documentation affects product uptake and retention. Tracking user journeys from documentation to product features and comparing documentation consumption with customer retention rates may illustrate its worth in increasing product utilization and customer satisfaction.

However, it is critical to understand the limitations of measurements. While quantitative data might give valuable insights, it may only capture some of the user experience or the underlying causes for user behavior. Any metrics should be combined with qualitative input, such as user interviews and usability testing. You want to know how users are using your docs.

Relying solely on metrics without context or interpretation can lead to misunderstanding or misaligned goals. Metrics should be part of a comprehensive strategy that aligns with company goals and prioritizes delivering an exceptional user experience. It is critical to select metrics carefully, augment quantitative data with qualitative insights, and interpret metrics in light of larger corporate goals and user demands.

-------------------------
Is Docs-as-Code Worth It?
-------------------------

The busiest topic in the WtD Slack this past month began in the `#docs-as-code channel <https://writethedocs.slack.com/archives/C72NZ18FR>`__ with a question about what bugs people about a docs-as-code approach. It set off a series of conversations touching on issues with docs-as-code as well as what people hope to gain from such an approach and what the next steps in its evolution could be.

Many of the main problems people discussed had to do with barriers to contributing to docs. For example, Git was universally acknowledged as something that seems complicated and might scare people away from suggesting improvements. Few people want to learn Git, they just want to get things done. Also, any syntax used to add features to docs, such as content reuse, adds another thing people have to learn before they can contribute.

While docs-as-code can bring testing and other process improvements to the docs, those also require the investment of significant resources. Using free and open-source software means your initial monetary investment is low, but they require a lot of maintenance. One reader brought up the idea from an article on `The pros and cons of using Markdown <https://passo.uno/pros-cons-markdown/>`__ that you want the docs to be the product, but that product shouldn't be your processes or docs website.

Some of the issues people encountered are outlined in the post `Docs as code is a broken promise <https://thisisimportant.net/posts/docs-as-code-broken-promise/>`__.

On the other side, people noted that it can be hard getting people to contribute even in systems that don't require you to learn Git, such as Confluence or even Google Docs. Some suggested that Git GUIs can accomplish most of what people want, leaving them free to focus on the actual docs themselves.

In the end, the conversation came back to the idea that docs-as-code isn't for everyone or every situation. But everyone involved was very interested in ideas about how to make writing good docs a more efficient process. Sharing our approaches in the `#docs-as-code channel <https://writethedocs.slack.com/archives/C72NZ18FR>`__ can help us learn from others' setbacks and build a communal approach.

----------------
From Our Sponsor
----------------

This month’s newsletter is sponsored by `Zoomin <https://www.zoominsoftware.com/>`__.

------

.. image:: /_static/img/sponsors/zoomin-apr-2024.jpg
  :align: center
  :width: 75%
  :target: https://go.zoominsoftware.com/l/1018802/2024-04-04/2brkz
  :alt: 2024 Technical Content Benchmark Report

**Measure your content performance against industry benchmarks**

Zoomin's 2024 Technical Content Benchmark report analyzes content interactions of over 97 million user sessions to provide a detailed overview of what good looks like in techcomm and the KPIs you should be looking at. Download the report to learn more about:

* How your peers are faring in deflecting cases through documentation
* The search KPIs you should be benchmarking
* The data you need to measure content efficiency

`Access the report here <https://go.zoominsoftware.com/l/1018802/2024-04-04/2brkz>`_.

------

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

----------------
Events Coming Up
----------------

- 8 May, 17:30 MDT (Boulder/Denver, USA): `Happy hour chat (virtual) <https://www.meetup.com/write-the-docs-boulder-denver/events/300330893/>`__
- 11 May, 10:30 EAT (Nairobi, Kenya): `Effective Collaboration & Communication in Documentation <https://www.meetup.com/write-the-docs-kenya/events/300777015/>`__
- 14 May, 18:30 EDT (Washington, USA): `2024 WTD DC Meet and Greet Happy Hour <https://www.meetup.com/write-the-docs-dc/events/299759367/>`__
- 14 May, 19:00 MDT (Calgary, Canada): `Bridging the Gap: Leveraging Technical Writing Skills in Learning Design <https://www.meetup.com/wtd-calgary/events/297725786/>`__
- 15 May, 19:00 EDT (Toronto, Canada): `Write the Docs Toronto  <https://www.meetup.com/write-the-docs-toronto/events/300645337/>`__
- 17 May, 08:30 EDT (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/boston-write-the-docs/events/299045884/>`__
- 23 May, 17:30 AEST (Australia): `Melbourne (Onsite): Helping Engineers Develop Technical Writing Skills <https://www.meetup.com/write-the-docs-australia/events/299130229/>`__
- 25 May, 08:00 EAT (Nairobi, Kenya): `Write the Docs Kenya Conference <https://www.meetup.com/write-the-docs-kenya/events/299526798/>`__
- 31 May, 08:30 EDT (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/boston-write-the-docs/events/xzpxdtygchbpc/>`__
