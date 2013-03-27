Write the Docs 2013 Presentations
=================================

.. contents:: Presentations
   :local:

.. note:: If these talks look interesting, you should `get a ticket`_


.. _get a ticket: http://conf.writethedocs.org/tickets.html

.. _adam-duvander:

Adam DuVander - Docs as Marketing: Make Your API Irresistible   
-----------------------------------------------------------------------------------------

    **20 minutes**

    Docs share knowledge, docs teach concepts, but docs done right can also bring in new customers. While developers might not like to admit it, documentation is now a form of marketing. Companies are building businesses on APIs, so how the technical details are communicated becomes as important as a product feature matrix. To succeed in this new reality, approach documentation with the same attention to detail and polish as other marketing. This talk shares lessons learned from observing the good and bad from hundreds of API providers and shares the ways the best are making their APIs irresistible.

.. _ana-nelson:

Ana Nelson - Integrating Development, Documentation and Reporting    
-----------------------------------------------------------------------------------------

    **40 minutes**

    Let's explore the amazing things that happen when you combine reporting with documentation. We'll start with a retro-chic command-line task management tool named 'ado', and create a beautifully modern D3-based interactive task explorer (no server necessary). Learn how powerful documentation-driven development can be, and the benefits of freeing documentation and reporting from their usual separate silos. 

    In this talk we will simultaneously document Bash, Python, SQL, CSS, HTML and JavaScript using HTML, PDF, epub, Excel and .docx formats (with just a single command!). You'll learn about Dexy, the document and data automation tool that makes this possible by working alongside the documentation tools you already know and love.

.. _andrew-kuchling:

Andrew Kuchling - Why Projects Should Have "What's New" Documents
----------------------------------------------------------------------------------------

    **20 minutes**

    Describes the speaker’s experience writing What’s New documents
    covering the new features in each Python 2.x release. The editorial
    policies will be summarized, and the speaker argues that large
    projects should include a “What’s New” as part of their standard
    documentation set.

.. _ann-goliak:

Ann Goliak - Helping out customers help themselves
----------------------------------------------------------------------------------------

    **20 minutes**

    37signals had help pages that weren't very helpful. That all changed with a new help section for the new Basecamp. Learn how the new help pages were developed & written and the effect they've had on support case load. Spoiler: it's much lighter!

.. _ashleigh-rentz:

Ashleigh Rentz - The technical challenges of serving docs at Google’s scale 
----------------------------------------------------------------------------------------

    **40 minutes**

    Google Code launched in 2005, hosting documentation for Google’s public APIs and Open Source software. Five years later, massive growth in the company’s developer offerings had pushed the site’s infrastructure to the max. What sorts of problems can sneak up when you go from 11 APIs to over a hundred? Or when many of those docs rapidly expand from hundreds to thousands of pages? And how can you build a serving infrastructure that won’t leave a room of execs holding their collective breath when new products launch at your annual showpiece conference?  

    Join Google Developer Programs’ Ashleigh Rentz for a behind-the-scenes retrospective: learn what it took to migrate a massive documentation library to a new home at Google Developers (developers.google.com) without freezing the existing site and how the new backend leverages both Open Source and Google technology to provide a CMS that truly scales.

.. _brandon-philips:

Brandon Philips - Single Page Docs: Stop the Click Insanity
----------------------------------------------------------------------------------------

    **20 minutes**

    Multi-page docs are the norm in most documentation framework. However, they aren't the best tool for the job of creating usable docs.

    Take for example the docs found on readthedocs.org for `Django Fluent Contents`_. This is a very normal looking sphinx project. Now lets try to find example code for the `announcementblock` plugin:

    - Ctrl+F "announcementblock". Darn, ok, no results.
    - Ctrl+F "plugins", Nope, Enter, Nope, Enter, Enter, Enter, Enter
    - Click on the link for example code, there it is! Woo!

    This style of code docs forces users to guess, click around, or simply leave your docs and use a Google `site:` search.

    A better alternative is single page docs like those for `Express JS`_. In this talk I will explore the best patterns and tools for single page documentation. And also explore the features and niceties that take single page docs from good to great.

.. _Django Fluent Contents: https://django-fluent-contents.readthedocs.org/en/latest/
.. _Express JS: http://expressjs.com/api.html

.. _daniel-lindsley:

Daniel Lindsley - The Unenviable Tutorial 
----------------------------------------------------------------------------------------

    **20 minutes**

    It's the first thing every new user looks for, the raison d'être of every project, almost always will completely divide the people evaluating your software & is the leading cause of liver cancer in the American pub... wait, no. Forget that last part. What I'm talking about is the Tutorial.

    Frequently the first bit of documentation written, the first one to fall hopelessly out of date & the one *everyone* sees, the Tutorial bears the brunt of getting people started. Its job is to pull people in. It teaches them not only what the software is about, but *how* it should be used. It sets the stage, the standard & the lowest bar of entry. It's unenviable because it must do so many things & do them well to be a success.

.. _daniya-kamran:

Daniya Kamran - Translating Science into Poetry 
----------------------------------------------------------------------------------------

    **40 minutes**

    Whether you're writing a grant, putting together a speech, giving a lecture, or conducting any sort of expression through a document, you're asking the reader to respond to a narrative. Especially when you're dealing with subjects like science, technology, education, or business, developing a compelling narrative can be increasingly difficult. Technical writers deviate from risky narratives because too much of their readership is focused on professionalism. What is unnecessary? What is "flowery"? What makes you comes across as less of a scientist? This talk demonstrates how to extract narratives from technical documents by utilizing lessons learned from poetry, and especially focus on using these narratives to create compelling supplementary documents from scientific data, such as infographics, talks, or impact assessments

.. _erin-robbins-obrien:

Erin Robbins O'Brien - Beautiful Documents - A Language Love Story
----------------------------------------------------------------------------------------

   **20 minutes**

    Technical writing, content marketing, and all other forms of documentation are a love story between writer and document. Carefully walking the balance between attractive, desirable content and the stability and comfort of getting the information needed. This talk will poetically address how to re-kindle your document love if it has been lost, and some strategies to keep the fires burning so that each document you write is as exciting as the first.  

.. _heidi-waterhouse:

Heidi Waterhouse - Search-first documentation: tags and keywords for frustrated users
----------------------------------------------------------------------------------------

   **20 minutes**

    The days of linear documentation are over, or at least numbered. Users are much more likely to come to documentation through searches. 

    As writers, we need to be aware that folksonomies and search terms are the present and future, and we need to write with tags and keywords as our first step. This presentation is a quick overview of how to write technical documentation ""search-first"", with an updated understanding of indexing and keywords.

.. _james-socol:

James Socol - UX and IA at Mozilla Support, and Helping 7.2 Million More People   
----------------------------------------------------------------------------------------

    **40 minutes**

    `Mozilla Support`_ has gone through a number of usability and information architecture evaluations over the past year and a half, the biggest of which helps us help 7.2 million additional people every year find the answers they need.

    I'll talk about some of the techniques and tools we've used (like heuristic evaluation, card sorts, treejack) and how to play along at home and apply these techniques to your own docs.

.. _Mozilla Support: http://support.mozilla.org

.. _james-tauber:

James Tauber  - Versioned Literate Programming for Tutorials    
----------------------------------------------------------------------------------------

    **20 minutes**

    This talk will explore the authoring of programming tutorials where each step of the tutorial involves code snippets that build on the code presented in earlier steps.

    Because such tutorials are primarily exposition in human language, but contain code snippets that should be executable if extracted, the approach has a lot in common with Literate Programming.

    At the same time, because the tutorials effectively guide the reader through the construction of the code, step-by-step, there is also a lot in common with Version Control.

    Hence I describe this approach as "Versioned Literate Programming".

    I don't (yet) have a good toolkit for this sort of tutorial authoring and so the talk will mostly focus on the ideas and challenges involved as well as some of the different approaches I've attempted over the years of thinking about this.

.. _jennifer-hartnett-henderson: 

Jennifer Hartnett-Henderson - Sketchnotes: Communicate Complex Ideas Quickly
----------------------------------------------------------------------------------------

    **20 minutes**

    Pick any two of the Visual, Auditory, Kinesthetic or Reading/Writing channels to communicate ideas faster and increase retention. In this 20 minute talk, I'll show how sketchnotes help communicate complex ideas quickly. For examples, check out the Sketchnote Army blog, The Sketchnote Handbook on Flickr, and these two entries on my blog: Getting All Your Photos in One Place and Ten Years of Photos in One Hand.

    Jennifer Hartnett-Henderson is a strategist, program manager and fine artist with an MFA in Digital Media.  She recently returned from the Mobile Photography Awards show in NYC where she was recognized with three Honorable Mentions in two categories.  Since 2000 she’s had many shows in the US and Europe and writes about photography on her blog Jennifer Hartnett Henderson. Sketchnoting helps integrate her right brain creative side with her left brain strategy work as she communicates complex ideas quickly.

    We’ll cover:

    * What are sketchnotes?  How are they different from art? 
    * Challenge: draw one sketchnote during this talk.
    * What is hand lettering? How is it different from typography?
    * What are examples of sketchnotes in use?
    * Why does it work? Dual coding theory, brain research
    * Simple ways to get started (basic tools, easily available resources including books, videos, Flickr groups, websites)
    * Share your sketchnote from this talk: Twitter, Flickr #sketchnotewtd

.. _jennifer-hodgdon:

Jennifer Hodgdon - Motivating developers to write API documentation
----------------------------------------------------------------------------------------

    **20 minutes**

    Everyone attending this conference probably agrees that it's a benefit in any software project to have good API documentation. But how do you get it written? There are three possible strategies: (a) Developers write the API documentation, (b) Technical writers write the API documentation, and (c) No one writes the API documentation. Option (c) is obviously undesirable, and option (b) is only viable in a corporate setting, so in open-source, the question becomes: how to motivate developers to write good API documentation.

    In the Drupal open-source project, API documentation has become one of the "Core Gates" that (in theory anyway) all patches must pass through to get committed to Drupal Core, which has taken API documentation from being an afterthought to being a requirement. This talk will go over:

    * The "Core Gates" concept and how it came about
    * The requirements for the Documentation "gate"
    * The Drupal project's documentation standards
    * How it's working in practice

.. _jim-wilson:

Jim R. Wilson - Describe, Defend, Differentiate and Deliver 
----------------------------------------------------------------------------------------

    **20 minutes**

    Many of us work for companies that fancy themselves software companies.
    Nominally though, what we produce is functionality, not software.
    And functionality is only worth while if people can use it.

    In this talk, I'll advocate for a wholistic approach to software development which incorporates documentation thinking at many levels.
    Documentation in its many forms can achieve diverse and sometimes accidental goals.
    With battle scars from real situations, I'll show how you can use documentation not only to describe, but to defend, differentiate and deliver.

.. _johnathan-mukai-heidt:

Jonathan Mukai-Heidt - Play and Pragmatism: Recapturing the Beginner's Mind    
----------------------------------------------------------------------------------------

    **20 minutes**

    Code helps to achieve concrete goals, but it also gives us room to play in the sandbox. Recent experiences teaching programming have taught me that these two facets of writing code need to be taken into account when teaching or writing documentation. Students come in two broad flavors. Some have an overly specific goal ("I want to make a social app for cat owners to share pictures") that they pursue to the detriment of their overall learning ("I don't understand how printing 'hello world' in this black box gets me any closer to uploading a photo of Dr.Mittens.") Others come to the table with the very general goal "learn to program." I believe that we can play these two mutually beneficial but frequently opposed attitudes about programming off of each other in order to teach programming, learn new technology ourselves, and write better documentation. A firm understanding of this interplay in code (pragmatic construction vs. playful exploration) can help us not just teach, but also become better developers.

.. _kenneth-reitz:

Kenneth Reitz - Documentation is King
----------------------------------------------------------------------------------------

    **40 minutes**

    Documentation leads to better code.

    Every design decision should be documented. Imagine not having to have tap your coworkers on the shoulder when you're working on an unfamiliar part of the codebase, or on-boarding a new employee. Imagine being able to make the change, run the tests, and push to production without questioning yourself, because the process was documented — or better yet, automated.

.. _kevin-hale:

Kevin Hale - Getting Developers and Engineers to Write the Docs  
----------------------------------------------------------------------------------------

    **40 minutes**

    At Wufoo, everyone has to wear multiple hats in our company and that includes manning the inbox and doing customer support every single week. One of the interesting side effects of having a company where designers, developers and even the accountant writing documentation and  answering support emails, is that everyone has a stake in making sure the application is as easy to use as possible.  

    We've called this approach to creating software Support Driven Development and in this talk Kevin Hale, one of the founders of Wufoo, will share how this model transformed every member of their company to be dedicated to the principles of clarity and simplicity.

.. _lauren-rother:

Lauren Rother - Build a Bakery: Making cake, eating it and planning for future cake too
----------------------------------------------------------------------------------------

    **20 minutes**

    Most of our work as technical writers is geared toward persons external to the company (users, customers, consumers, etc.), so our first concern is creating something engaging and useful for them. Some of our tasks and projects, however, require us to consider a more complex audience.

    At Puppet Labs, the documentation team curates, evaluates and edits internal documents (both inter-team and intra-team) and  develops documentation meant to be used by internal employees, with the knowledge that these documents may one day need to become external documents.  The team also develops documentation guidelines that are meant to be followed by internal employees and external users. 

    Lauren Rother and Fred Lifton of Puppet Labs will discuss the way in which these tasks complicate the usual notion of audience, and the way in which they approach and manage working on projects that require an eye on the future as well as the present.

.. _leah-cutter:

Leah Cutter - Generating a Culture of Doc
----------------------------------------------------------------------------------------

    **40 minutes**

    How do you encourage engineers to do the write thing?  (Not a typo.) 

    At Salesforce.com, we now have a team called, "Core Documentation." We are primarily focused on documenting our internal systems and architecture. Many of us on the team don't create content: We generate framework, best practices, and training for engineer-created content. (Content can include and is not limited to: code comments, run lists, specs, team web pages, wikis, white papers, architectural diagrams, presentations, etc.) 

    But that goes back to the first question--how do you get someone to write, when the word "writer" isn't part of their title? 

    We've been successful using several different venues:
    - Documentation "hack" day -- where engineers spend a day improving their internal doc
    - Events where posters of different aspects of the architecture are displayed (think art walk, only for engineers)
    - VERY easy to use templates for readme files, etc.
    - Lunch meetings/presentations/training/networking 
    - Flattery, appeals to logic (bus factor) and bribes

    Plus I would also present some of the things that haven't worked.

.. _matthew-butterick:

Matthew Butterick - Typography for Docs 
-----------------------------------------------------------------------------------------

    **40 minutes**

    Should writers of documentation care about typography? As someone who reads a lot of documentation, I can see that many don't. But good typography can reinforce your meaning, conserve reader attention, and make your docs more inviting and useful. And it's easier than you might think. In this session I'll explain the four rules of typography that every writer of docs needs to know. I'll also cover some typographic issues specific to web-based docs, and critique a few real-world examples. 

.. _marcia-riefer-johnston: 

Marcia Riefer Johnston - Write Tight(er) 
----------------------------------------------------------------------------------------

    **40 minutes**

    This presentation helps technical writers transform text into specimens of conciseness. With small screens squeezing the "page"—and with translations costing around $0.25 per word per language—this timeless skill gets more and more timely. Attendees will learn: 

    - How flabby writing hurts business. 
    - Why "concise" does not equal "short."
    - Why they don't need a double-standard to write for small screens. 
    - How to tighten and energize their writing.

.. _michael-verdi:

Michael Verdi - How Mozilla supports users all over the world
----------------------------------------------------------------------------------------

    **40 minutes**

    The Mozilla support platform is built around a fully localizable wiki and an awesome community of volunteers. Together we're able to support nearly half a billion users in dozens of languages. This talk will focus on how we support the 50% of Firefox users who use it a language other than English.

.. _noirin-plunkett:

Noirin Plunkett - Text Lacks Empathy
----------------------------------------------------------------------------------------

    **40 minutes**

    Have you ever written a nice friendly email and gotten a reply that seems like they read a whole different email?

    In Open Source communities we write to each other all the time, but we’re not really writing, we’re speaking with our fingers. Text is our primary way to communicate, but text has problems. Speaking conveys subtle emotional cues that as social animals we rely on; text strips them out. A thoughtful correspondent can put those emotions back, but we’re often not thoughtful.

    This talk is about the special problems of textual communication: mitigating them; ensuring that what you mean to say is what is understood; interpreting messages that seem totally out of whack; and increasing empathic bandwidth.

.. _nisha-george:

Nisha George & Elaine Tsai - Translating Customer Interactions to Documentation  
----------------------------------------------------------------------------------------

    **20 minutes**

    If customers have problems they can’t find answers to or need to report an issue then they contact your Customer Support team. Support is first line of defense to keeping your customers happy. But, customers are happiest when they can find answers on their own without having to wait for a response from Support. When Support owns a portion of the docs: customers are empowered to find solutions on their own, the incoming volume of tickets reduces and companies can better scale their internal teams in relation to their growing customer base.  

    This presentation will cover the types of documentation that your company’s Support team should own along side the documentation maintained by Engineering. We will give examples of how your Support team can:

    - Turn incoming tickets into FAQs to prevent future tickets
    - Provide answers for all types of customers, from beginners to experts
    - Create positive experiences for customers and internal teams

.. _sarah-grant:

Sarah Grant - Evolution of the English Language from Text to Texting  
----------------------------------------------------------------------------------------

    **20 minutes**

    Or, Why the Oxford English Dictionary is My Favorite Book, and Why I Love the Chicago Manual of Style

    The Oxford English Dictionary holds the key to every word in the English language, starting with the language from which it was borrowed/stolen, following its history to current times, and giving examples of usage from the beginning. New words are introduced into common usage every year, and some make it into an official dictionary. Some words are practical (i.e., Internet), while others are superfluous (i.e., ironical) and many are just plain wrong (i.e., orientated). 

    The "correct" use of words and language seems to be more and more fluid these days. Will commonly used acronyms, seen mainly in texting and instant messaging, become part of the standard usage? How fluid SHOULD the English language be? What types of grammatical and punctuation changes are acceptable, and what types  are not? Where do we draw the line?

    This talk will present these questions and others, and begin to formulate possible answers to benefit the potential audience of writers.

.. _teresa-talbot:

Teresa Talbot - Technically Communicating Internationally   
----------------------------------------------------------------------------------------

    **20 minutes**

    Ever dreamed of working abroad? Often overlooked as an international career, technical documentation has taken me to nine countries and allowed me to work with many of the world's cultures. Truth is, if you're translating it's best to start with English. More people speak English as a second language than any other and, as you want translators to translate into their first language, it's easier and cheaper to translate from English. Come hear and share international experiences. Learn why and how I managed it legally. Gain tips and tricks for getting what you need from subject matter experts in a foreign (to you) culture and writing with translation in mind. Cultural shocks and embarrassing moments? I've got them and can help you avoid them.

    Countries where I've lived and worked:

    * USA
    * United Kingdom
    * New Zealand
    * Netherlands
    * Japan
    * Bulgaria
    * Spain
    * Switzerland
    * France

.. _tim-daly:

Tim Daly  - Literate Programming in the Large   
----------------------------------------------------------------------------------------

    **40 minutes**

    Axiom is an open source computer algebra system written mostly in Common Lisp. As one of the original authors at IBM Research I wrote a fair amount of code. Later Axiom was sold commercially as a competitor to Mathematica and Maple. When it was later withdrawn from the market I was given the code. It was soon apparent that, while what the code did was clear, why it did what it did was not. Being unable to understand my own code was a shock. Eventually I decided to reshape the code base using Knuth's Literate Programming technology. The idea is that one should be able to read Axiom like a book directed at human understanding, a book which incidently contains the actual source code of the system. This talk is a description of the first 10 years of that effort with insights into the challenges of writing a million-line literate program.

