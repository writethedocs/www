# Style Guides

A style guide contains a set of standards for writing and designing content. It helps maintain a consistent style, voice, and tone across your documentation, whether you're a lone writer or part of a huge docs team. A style guide saves documentarians time and trouble by providing a single reference for writing about common topics, features, and more. It can provide guidelines for different documentation deliverables, such as API reference manuals, tutorials, release notes, or overviews of complex technical concepts.

A consistent tone and style makes your content easier to read, reducing your users' [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) and increasing their confidence in the content's authority.

Some content that used to live on this page has moved. See:

- [Accessibility guidelines](https://www.writethedocs.org/guide/writing/accessibility)
- [Reducing bias in your writing](https://www.writethedocs.org/guide/writing/reducing-bias)

## Write your own style guide?

A style guide can be something as simple as a list of decisions you've made about how to refer to different items you frequently write about. Or it can be as complicated as the mighty tomes of major publication houses.

You can certainly create a style guide of your own. For the sake of simplicity, this approach might work if you're a lone writer or just starting a small docs group. But neither software nor its documentation operates in a vacuum, so it's a good idea to consult other resources as well. Working from an existing style guide can also help you figure out which things matter in your style guide.

## Style guide resources

Style guides have been around for as long as people have been publishing in any format. Traditional style guides originally intended for specific forms of print publication have become basic standards for many others to refer to, including documentarians:

- The [AP Stylebook](https://www.apstylebook.com/)
- The [Chicago Manual of Style](http://www.chicagomanualofstyle.org/book/ed17/frontmatter/toc.html)

Classic style guides for software documentation include:

- [Apple Style Guide](https://help.apple.com/applestyleguide/)
- [Microsoft Writing Style Guide](https://docs.microsoft.com/en-us/style-guide/welcome/)

Other useful resources:

- [18F US Government Content Guide](https://content-guide.18f.gov)
- [DigitalOcean Documentation Style Guide](https://docs.digitalocean.com/style/)
- [Google developer documentation style guide](https://developers.google.com/style)
- [gnome Documentation Style Guide](https://developer.gnome.org/gdp-style-guide/2.32/gdp-style-guide.html)
- [MongoDB Style Guide](https://docs.mongodb.com/meta/style-guide/)
- [Rackspace Style Guide for Technical Content](https://docs.rackspace.com/docs/style-guide/)
- [Salesforce Style Guide for Documentation and User Interface Text](https://developer.salesforce.com/docs/atlas.en-us.salesforce_pubs_style_guide.meta/salesforce_pubs_style_guide/overview.htm)
- [SUSE Documentation Style Guide](https://documentation.suse.com/style/current/single-html/docu_styleguide/)
- [The Red Hat Style Guide](http://stylepedia.net/style/)
- [Voice and Tone guidelines -- Mailchimp](https://styleguide.mailchimp.com/voice-and-tone/)

Relevant talk from Write the Docs:

- [What They Don't Tell You About Creating New Style Guides](https://www.writethedocs.org/videos/portland/2018/what-they-don-t-tell-you-about-creating-new-style-guides-thursday-bram/) at WTD Portland 2018

## Developer documentation and APIs

Style guide and guidelines for code samples:

- [API reference code comments -- Google developer documentation style guide](https://developers.google.com/style/api-reference-comments)
- [API Documentation Guidelines -- Ruby on Rails](http://guides.rubyonrails.org/api_documentation_guidelines.html)
- [REST API Documentation Best Practices -- bocoup](https://bocoup.com/blog/documenting-your-api)

## Command line resources

A command-line interface (CLI) processes commands to a computer program in the form of lines of text. Style guide standards for [command line interface](https://en.wikipedia.org/wiki/Command-line_interface) docs and text include these useful CLI resources:

- [10 design principles for delightful CLIs -- Atlassian](https://blog.developer.atlassian.com/10-design-principles-for-delightful-clis/)
- [CLI Style Guide -- Heroku Dev Center](https://devcenter.heroku.com/articles/cli-style-guide)
- [Command Line Interface Guidelines -- CLIG](https://clig.dev/#guidelines)
- [Conventions for writing Linux man pages -- die.net](https://linux.die.net/man/7/man-pages)
- [Documenting command-line syntax -- Google developer documentation style guide](https://developers.google.com/style/code-syntax)
- [CLI Docs to Improve DevX video series](https://www.youtube.com/playlist?list=PLQiULOUzZJ5hKZGdbC939GKBTLOtPaAyq)
- [gnome Documentation Style Guide](https://developer.gnome.org/gdp-style-guide/2.32/gdp-style-guide.html)

Relevant talk from Write the Docs:

- [How I learned to stop worrying and love the CLI](https://www.writethedocs.org/videos/portland/2019/how-i-learned-to-stop-worrying-and-love-the-command-line-mike-jang/) at WTD Portland 2019

### API documentation

Clear, well-formatted, and detailed API documentation is the key for developers to quickly consume and implement your API. It is also key to helping developers understand what happens when an API call is made, and in the case of failure, understand what went wrong and how to fix it.

From the perspective of a user:

- If a feature is not documented, it does not exist. If a feature is documented incorrectly, then it is broken.

The best API documentation is often the result of a well [designed API](#documentation-driven-design). Documentation cannot fix a poorly designed API. It is best to work on developing the API and the documentation concurrently.

If your API already exists, automated reference documentation can be useful to document the API in its current state. If your API is still being implemented, API documentation can perform a vital function in the design process.

#### Documentation-driven design

If your API isn't built yet, you can create API documentation to help with the design process. The documentation-driven design philosophy comes down to this:

- Documentation changes are cheap. Code changes are expensive.

By designing your API through documentation, you can easily get feedback and iterate your design before development begins.

Some API documentation formats have the added benefit of being machine-readable. These formats open the door to a multitude of additional tools that can help during the entire lifecycle of your API:

- Create a mock server to help during the initial API design
- Test your API before deployment to ensure that the API and the documentation matches
- Create interactive documentation that allows developers to perform demo requests to your API

#### Test-driven documentation

Test-driven documentation aims to improve upon the typical approaches to automated documentation. It allows you to write the bulk of the documentation by hand while also ensuring its accuracy by using your API's tests to generate some content.

Projects such as [Spring REST Docs](https://spring.io/projects/spring-restdocs) use API tests to generate small snippets of documentation that you can include in the hand-written API documentation. The accuracy of the documentation is ensured by the tests – if the API's documentation becomes inconsistent with its implementation, the tests that generate the snippets will fail.

#### API resources

- [Documenting APIs: a guide for technical writers and engineers -- Tom Johnson I'd rather be writing](https://idratherbewriting.com/learnapidoc/)
- [REST API Guidelines -- Microsoft](https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md)
- [API Design Guidelines -- PayPal](https://github.com/paypal/api-standards/blob/master/api-style-guide.md)
- [The Ten Essentials for Good API Documentation -- A List Apart](https://alistapart.com/article/the-ten-essentials-for-good-api-documentation/)

## Content guidelines

It's important to create consistency in your content types to manage expectations for what users learn on a given page.

### FAQs

Frequently Asked Questions (FAQs) exist to educate and guide users through need-to-know information while pointing them to additional resources when necessary. FAQs are short and limited.

Effective FAQ pages accomplish the following:

- Reflects the audience's needs. This requirement may be derived from understanding search results that lead to the website or documentation.
- Regularly updated to reflect the changes in user behavior and data.
- Drives users to different parts of the website to deliver more detailed information.
- Cover a broader range of topics that may not otherwise warrant individual pages or pieces of content.

Caveat: Be sure to follow a maintenance plan for FAQs, since many content gets parked here and becomes outdated. Consider finding a relevant content structure for the content outside of the FAQ scope.

### Release notes

Release notes exist to provide users with vital information required to continue to use and benefit from a product. Release notes content is related to new or updated feature releases. Release notes should be brief, linking out to more details as necessary.

Consider the following when creating an entry for your release notes:

1. What is the specific change?

2. Why did we make this change? Why is it important to our users?

  - Improvement in workflow or UI
  - Consistency and feature parity
  - Policy and legal changes
  - Security

3. What is the goal for our users who use this feature?

4. Do our users have all the information they need to move forward?

5. Is there an additional article for users to read and to learn more? Yes? Link to those resources.

6. Would an image be beneficial to help users understand this release?

7. What stakeholders have to approve this content? Does it require the legal team's approval?

Release Notes Style Guide Resources:

- [5 excellent product release note examples and how to write your own -- Appcues](https://www.appcues.com/blog/release-notes-examples)
- [How to make release notes count -- Opensource](https://opensource.com/article/17/3/how-to-improve-release-notes)
- [How to Write Release Notes Your Users Will Actually Read -- ProductPlan](https://www.productplan.com/learn/release-notes-best-practices/)
- [Release notes guidelines -- Rackspace](https://docs.rackspace.com/docs/style-guide/release-notes-guidelines/)
- [Release notes and changelogs -- Unity Docs Style Guide](https://unity-docs.gitbook.io/style-guide/style/release-notes)
- [The Importance of Writing Release Notes -- Testlodge](https://blog.testlodge.com/importance-of-writing-release-notes/)
- [Transforming Your Release Notes into Product Announcements -- Parlor](https://www.parlor.io/blog/transforming-your-release-notes-into-product-announcements/)
- [The art of writing great release notes -- UX Collective](https://uxdesign.cc/the-art-of-writing-great-release-notes-6607e22efae1)
- [The art of writing Release Notes A guide, examples & template -- Slite](https://slite.com/learn/release-notes)
- [The best and the worst app release notes that will inspire you -- announcekit](https://announcekit.app/blog/the-best-and-the-worst-app-release-notes-that-will-inspire-you)

Examples of great release notes:

- [DataStax DSE](https://docs.datastax.com/en/dse/6.8/dse-admin/datastax_enterprise/releaseNotes/releaseNotes.html)
- [Digital Ocean](https://docs.digitalocean.com/release-notes/)
- [Firefox](https://www.mozilla.org/en-US/firefox/releases/)
- [Google Ad Manager](https://support.google.com/admanager/answer/10290437)
- [Jira](https://confluence.atlassian.com/adminjiraserver/upgrade-matrix-966063322.html)
- [MadCap Flare 2021](https://kb.madcapsoftware.com/Content/Flare/General/GEN1066F_-_Flare_2021_Release_Notes.htm)
- [Slack](https://slack.com/release-notes/mac)
- [teamwork.](https://www.teamwork.com/roadmap)
- [Unreal Engine](https://docs.unrealengine.com/en-US/WhatsNew/Builds/index.html)

What to avoid:

<!-- vale off -->

- [App Release Notes Are Getting Stupid -- TechCrunch](https://techcrunch.com/2015/09/04/app-release-notes-are-getting-stupid/)
- [Release Notes: 13 Mistakes to Avoid When Writing Bugs and Enhancements -- klariti.com](https://www.klariti.com/technical-writing/2015/05/08/release-notes-mistakes-to-avoid/) Related talks:
- [Learning to love release notes](http://www.writethedocs.org/videos/prague/2018/learning-to-love-release-notes-anne-edwards/) at Write the Docs Prague 2018
- [Rethinking Release Notes](https://www.youtube.com/watch?v=SWduFnDPjYg) at Write the Docs Australia 2019

<!-- vale on -->

### Error messages

Errors in software are unavoidable. Users might click a link that turns out to be broken or they might perform an action only to be met with an unexpected outcome. When a user encounters a problem, it's important to write error messages in a way that doesn't alienate the user.

Here are a few tips on what makes a good error message:

- Provide explicit indication that something has gone wrong.
- Write like a human, not a robot.
- Don't blame the user – be humble.
- Make the message short and meaningful.
- Include precise descriptions of exact problems.
- Offer constructive advice on how to fix the problem.

Related resources:

- [Error Message Guidelines -- Microsoft](https://docs.microsoft.com/en-us/windows/win32/debug/error-message-guidelines)
- [Error Message Guidelines –- NN Group](https://www.nngroup.com/articles/error-message-guidelines/)
- [How to Write Good Error Messages -– UX Planet](https://uxplanet.org/how-to-write-good-error-messages-858e4551cd4)
- [How to write better error messages –- opensource.com](https://opensource.com/article/17/8/write-effective-error-messages)
- [How to write better error messages for databases -- PostgreSQL](https://www.postgresql.org/docs/current/error-style-guide.html)

## Other style resources

Rather than reinvent the wheel, here are some resources curated by [Ivan Walsh](http://www.ihearttechnicalwriting.com/style-guide-technical-writing/) (Kudos!):

- [How to create a style guide: 25 expert tips for designers -- Creative Bloq](https://www.creativebloq.com/design/create-style-guides-1012963)
- [Content style guides: A complete process to develop your own -- Gather Content](http://blog.gathercontent.com/tone-of-voice-guide)
- [How to Create a Writing style guide Built for the Web -- HubSpot](http://blog.hubspot.com/blog/tabid/6307/bid/31247/The-Simple-Template-for-a-Thorough-Content-Style-Guide.aspx)
- [Editorial Style for the Web -- Meet Content](http://meetcontent.com/blog/elements-of-editorial-style-for-the-web/)
- [Creating a web style guide -- Stanford Web Services Blog](https://swsblog.stanford.edu/blog/creating-web-style-guide-cardinal-work)
- [Developing a Departmental Style Guide -- Techwhirl](http://techwhirl.com/developing-a-departmental-style-guide/)
