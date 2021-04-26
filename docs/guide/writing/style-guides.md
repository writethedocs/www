# Style Guides

A style guide contains a set of standards for writing and designing content. It
helps maintain a consistent style, voice, and tone across your documentation,
whether you're a lone writer or part of a huge docs team. A style guide saves
documentarians time and trouble by providing a single reference for writing
about common topics, features, and more. It can provide guidelines for different
documentation deliverables, such as API reference manuals, tutorials, release
notes, or overviews of complex technical concepts.

A consistent tone and style makes your content easier to read, reducing your
users' [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) and
increasing their confidence in the content's authority.

Some content that used to live on this page has moved. See:

- [Accessibility guidelines](https://www.writethedocs.org/guide/writing/accessibility)
- [Reducing bias in your writing](https://www.writethedocs.org/guide/writing/reducing-bias)


## Write your own style guide?

You can certainly create a style guide of your own. This approach might work if
you're a lone writer or just starting a small docs group. But neither software
nor its documentation operates in a vacuum, so it's a good idea to consult other
resources as well. Working from an existing style guide also helps you figure
out which things matter in your style guide.

## Style guide resources

Style guides have been around for as long as people have been publishing in any
format. Older style guides originally intended for specific forms of print
publication have become basic standards for many others, including
documentarians, to refer to:

- The [Chicago Manual of Style](http://www.chicagomanualofstyle.org/book/ed17/frontmatter/toc.html)
- The [AP Stylebook](https://www.apstylebook.com/)

Classics for software documentation include:

- [Microsoft Writing Style Guide](https://docs.microsoft.com/en-us/style-guide/welcome/)
- [The IBM Style Guide: Conventions for Writers and Editors](https://www.amazon.com/IBM-Style-Guide-Conventions-Writers/dp/0132101300)
- [Apple Style Guide](https://help.apple.com/applestyleguide/)

Others you might find useful:

- [Google developer documentation style guide](https://developers.google.com/style)
- [Salesforce Style Guide for Documentation and User Interface Text](https://developer.salesforce.com/docs/atlas.en-us.salesforce_pubs_style_guide.meta/salesforce_pubs_style_guide/overview.htm)
- [The Red Hat Style Guide](http://stylepedia.net/style/)
- [Rackspace Style Guide for Technical Content](https://docs.rackspace.com/docs/style-guide/)
- [18F Content Guide](https://content-guide.18f.gov)
- [SUSE Documentation Style Guide](https://documentation.suse.com/style/current/single-html/docu_styleguide/)
- [gnome Documentation Style Guide](https://developer.gnome.org/gdp-style-guide/2.32/gdp-style-guide.html)

## Developer documentation and APIs

Example guides for code samples:

- [Google code samples](https://developers.google.com/style/code-samples)
- [Ruby / other languages](http://guides.rubyonrails.org/api_documentation_guidelines.html)
- [Al language snippets](https://bocoup.com/blog/documenting-your-api)

### API documentation

Clear, well-formatted, and detailed API documentation is the key for developers to quickly consume and implement your API. It is also key to helping developers understand what happens when an API call is made, and in the case of failure, understand what went wrong and how to fix it.

From the perspective of a user:

> If a feature is not documented, it does not exist. If a feature is documented incorrectly, then it is broken.

The best API documentation is often the result of a well [designed API](#documentation-driven-design). Documentation cannot fix a poorly designed API. It is best to work on developing the API and the documentation concurrently.

If your API already exists, automated reference documentation can be useful to document the API in its current state. If your API is still being implemented, API documentation can perform a vital function in the design process.

#### Documentation-driven design

If your API isn't built yet, you can create API documentation to help with the design process. The documentation-driven design philosophy comes down to this:

> Documentation changes are cheap. Code changes are expensive.

By designing your API through documentation, you can easily get feedback and iterate your design before development begins.

Some API documentation formats have the added benefit of being machine-readable. These formats open the door to a multitude of additional tools that can help during the entire lifecycle of your API:

- Create a mock server to help during the initial API design
- Test your API before deployment to ensure that the API and the documentation matches
- Create interactive documentation that allows developers to perform demo requests to your API

#### Test-driven documentation

Test-driven documentation aims to improve upon the typical approaches to automated documentation. It allows you to write the bulk of the documentation by hand while also ensuring its accuracy by using your API's tests to generate some content.

Projects such as [Spring REST Docs](https://spring.io/projects/spring-restdocs) use your API's tests to generate small snippets of documentation that you can include in the hand-written API documentation. The accuracy of the documentation is ensured by the tests – if the API's documentation becomes inconsistent with its implementation, the tests that generate the snippets will fail.

#### API resources

- <a href="https://github.com/paypal/api-standards/blob/master/api-style-guide.md">PayPal's API Design Guidelines</a>
- <a href="https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md">Microsoft's REST API Guidelines</a>
- [Documenting APIs: a guide for technical writers and engineers](https://idratherbewriting.com/learnapidoc/)
- [The Ten Essentials for Good API Documentation](https://alistapart.com/article/the-ten-essentials-for-good-api-documentation/) by A List Apart

## Content guidelines

It's important to create consistency in your content types. Doing so allows you to manage your audience's expectations for what they will learn on any given page.

### FAQs

Frequently Asked Questions (FAQs) exist to educate and guide users through need-to-know information, pointing them to additional resources when necessary. FAQs should be short and limited.

Effective FAQ pages accomplish the following:

- Reflects the audience's needs. This may be derived from understanding search results, which lead to the website or documentation.
- Regularly updated to reflect the changes in user behavior and data.
- Drives users to different parts of the website to deliver more detailed information.
- Cover a broader range of topics that may not otherwise warrant individual pages or pieces of content.

### Release notes

Release notes exist to provide users with vital information needed to continue to use and benefit from a product, often related to new or updated feature releases. These notes should be brief, linking out to more details as necessary.

Consider the following when creating an entry for your release notes:

1. What is the change/release?
1. Why did we make this change? Why is it important to our users?
   1. Improvement in workflow or UI
   1. Consistency/feature parity
   1. Expected revenue increase/decrease
   1. Change in phase: Alpha/Beta/GA (Does this need to be called out?)
   1. Policy/legal changes
1. What is the goal for our users who use this feature?
1. When will this feature be available? Is it already available or coming soon?
1. Do our users have all the information they need to move forward?
1. Is there an additional article for users to read to learn more?
1. Would an image be beneficial to help users understand this release?
1. What stakeholders have to approve this content? Does it require the legal team's approval?

Some example release notes:

- [Jira release notes](https://confluence.atlassian.com/jirasoftware/jira-software-release-notes-776821069.html)
- [Slack](https://slack.com/release-notes/mac) and [more about their release note style](https://slackhq.com/a-little-thing-about-release-notes#)
- [What's new in Google Ad Manager](https://support.google.com/admanager/answer/179039?hl=en)

Related talks:

- [Learning to love release notes](http://www.writethedocs.org/videos/prague/2018/learning-to-love-release-notes-anne-edwards/) at Write the Docs Prague 2018

### User Guide / Manuals

### Tutorials / How-To

### Concepts, Overview

## Writing Style

The following style guides focus on writing more generally:

- [The Sense of Style](https://stevenpinker.com/publications/sense-style-thinking-persons-guide-writing-21st-century)
- [Stylish Academic Writing](https://www.hup.harvard.edu/catalog.php?isbn=9780674064485)
- [Mailchimp's Voice and Tone guidelines](https://styleguide.mailchimp.com/voice-and-tone/)

## Other style resources

Rather than reinvent the wheel, here are some resources curated by [Ivan Walsh](http://www.ihearttechnicalwriting.com/style-guide-technical-writing/) (Kudos!):

- [Creative Blog — Create a website style guide](http://www.creativebloq.com/design/create-website-style-guide-6123030)
- [Gather Content — Developing a Content style guide](http://blog.gathercontent.com/tone-of-voice-guide)
- [HubSpot — How to Create a Writing style guide Built for the Web](http://blog.hubspot.com/blog/tabid/6307/bid/31247/The-Simple-Template-for-a-Thorough-Content-Style-Guide.aspx)
- [Meet Content — Editorial Style for the Web](http://meetcontent.com/blog/elements-of-editorial-style-for-the-web/)
- [Stanford — Creating a web style guide](https://swsblog.stanford.edu/blog/creating-web-style-guide-cardinal-work)
- [Techwhirl – Developing a Style Guide for Technical Publications](http://techwhirl.com/developing-a-departmental-style-guide/)
- [UCR — Writing for the Web, Content Guidelines](http://cms.ucr.edu/writing_web_content.html)
