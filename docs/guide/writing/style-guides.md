# Style Guides

A style guide is a set of standards for the writing and design of content, defining the style to be used in communication within a particular organization. Basically, style guides are put together to clarify [the way a group of people talk and write about the things they do](https://www.writethedocs.org/style-guide/). Think of authoring best practices.

If you happen to have a background in academia or journalism, you will probably be familiar the [AP stylebook](https://en.wikipedia.org/wiki/AP_Stylebook) or the [Chicago manual of style](http://www.chicagomanualofstyle.org/book/ed17/frontmatter/toc.html). Those are great resources for writing in general, particularly for grammar and syntax, but if you're reading this page chances are you are considering style in the context of technical documentation.

### Technical Documentation

Style guides help you write a variety of content, such as documenting the methods of an API, or presenting an overview of complex technical concepts, or focusing on how to write particular content like user manuals, release notes, or tutorials.

Guides often help writers focus on the different readers of technical documentation, describing how to adapt content to different reader profiles, like developers, product managers, the general public, and others.

Many focus on the language itself (tone, style, grammar).

Others go beyond the content and discuss the organisation of the documentation, providing best practices on how to manage your content, version control, or publication and delivery strategies. While this is not what we focus on in our style guide, how your documentation is organized, and how easy it is for your readers to find what they are looking for, can be as important as the content itself.

## Why do I need a style guide?

A practical reason to use a style guide is that they help you write content. Human languages are extremely flexible, and there are many ways in which a particular message can be communicated. By following a style guide you limit the variation, making it easier for you to focus on getting your message across. This makes style guides extremely useful for people joining projects.

Style guides also increase consistency in your content. There are good reasons why you want to keep a consistent tone, voice and style in your documentation. Marketing-oriented folks understand the importance of voice and tone in building a brand identity, a strategy we can extend into technical writing. Consistency also has a big impact on how effectively you communicate -- that is, on how well you manage to transfer a particular information to your audience.

There's science behind this. Our brains appear to be hardwired to identify differences -- anything that stands out from its context will catch our attention. A lot of variation will drain our cognitive resources, making it more difficult for us to assimilate information. The degree to which cognitive resources are drained varies between people, but in general it is a good idea to minimize the [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) of your communications.

## Different styles for different folk

Choosing the right style guide for your project depends on your particular context:
  - Who you are
  - Who you are writing for
  - What you are writing about

### Selecting a good style guide for you

There may already be a style guide somewhere within your organization. It is a good idea to ask your colleagues about this before picking a particular style guide for your project.

Here are some good general resources -- perhaps someone in your company is already using one of these:
- [A list apart style guide](https://alistapart.com/about/style-guide)
- [Techprose techwriting guidelines (PDF)](http://www.techprose.com/assets/techwriting_guidelines.pdf)
- [Microsoft manual of style](https://ptgmedia.pearsoncmg.com/images/9780735648715/samplepages/9780735648715.pdf)
- [Oxford manual of style](https://www.ox.ac.uk/sites/files/oxford/media_wysiwyg/University%20of%20Oxford%20Style%20Guide.pdf)
- [IBM style guide](https://www.ibm.com/developerworks/library/styleguidelines/)
- [Handbook of Technical Writing](http://www.macmillanlearning.com/Catalog/product/handbookoftechnicalwriting-eleventhedition-alred)

If you belong to an open-source community or NGO, you can consider the following resources:
- [18F Content Guide](https://content-guide.18f.gov)
- [Open SUSE Style Guide](https://doc.opensuse.org/products/opensuse/Styleguide/opensuse_documentation_styleguide_sd/)
- [gnome Style Guide](https://developer.gnome.org/gdp-style-guide/2.32/gdp-style-guide.html)
- [Department of Defense Writing Style Guide and Preferred Usage](http://www.esd.whs.mil/DD/)

### Selecting a good style guide for your audience

Technical documentation takes many forms, each one targeting a certain need. Here, we can think of examples like tutorials, API documentation, and user manuals. So while many style guides adequately cover the main concerns of all technical documentation, sometimes a more specialized guide is needed.

## Style for developers

Developer documentation often have a specific set of rules in order to best meet their needs.

### Code samples

Here are some example guides for code samples

- [Google code samples](https://developers.google.com/style/code-samples)
- [Ruby / other languages](http://guides.rubyonrails.org/api_documentation_guidelines.html)
- [Al language snippets](https://bocoup.com/blog/documenting-your-api)

## Thinking about accessibility

It's important to consider accessibility in your style guide to ensure the content you produce can be best understood by all readers. Writing for accessibility includes making sure copy can be read by screenreaders, content organization, style and color of text emphasis, and more.

### Accessibility resources

- [MailChimp's writing style guide](https://styleguide.mailchimp.com/writing-for-accessibility/)
- [A11Y Style Guide](https://a11y-style-guide.com/style-guide/)
- [The Accessibility Cheatsheet](https://bitsofco.de/the-accessibility-cheatsheet/) by bitsofcode

Relevant talks from Write The Docs:

- [A11y-Friendly Documentation](https://www.writethedocs.org/videos/prague/2018/a11y-friendly-documentation-carolyn-stransky/) at Write The Docs Prague 2018
- [Inclusive Tech Docs - TechComm Meets Accessibility](http://www.writethedocs.org/videos/eu/2015/inclusive-tech-docs-techcomm-meets-accessibility-rmatic/) at Write the Docs EU 2015 

## Content guidelines

It's important to create consistency in your content types. This allows you to manage your audience's expectations for what they will learn on any given page.

### API documentation

Clear, well-formated, and detailed API documentation is the key for developers to quickly consume and implement your API. It is also key to helping developers understand what happens when an API call is mad, and in the case of failure, understand what went wrong and how to fix it.

The best API documentation is often the result of a designed API. Documentation cannot fix a badly planned API, and it is best to work on developing the API and the documentation concurrently.

[Our guide to API documentation](https://www.writethedocs.org/guide/api/about-api-documentation/).

Additional resources:

- [PayPal's API Design Guidelines](https://github.com/paypal/api-standards/blob/master/api-style-guide.md)
- [Microsoft's REST API Guidelines](https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md)
- [Documenting APIs: a guide for technical writers and engineers](https://idratherbewriting.com/learnapidoc/)
- [The Ten Essentials for Good API Documentation](https://alistapart.com/article/the-ten-essentials-for-good-api-documentation/) by A List Apart

### FAQs

Frequenty Asked Questions (FAQs) exist to educate and guide users through need-to-know information, pointing them to additional resources when necessary. FAQs should be short and limited.

Effective FAQ pages accomplish the following:

- Reflects the audience needs. This may derrive from understanding search results which lead to the website or documentation.
- Regularly updated to reflect the changes in user behavior and data.
- Drives users to different parts of the website to deliver more detailed information.
- Cover a broader range of topics that may not otherwise warrant individual pages or pieces of content.

### Release notes

Release notes exist to provide users with vital information needed to continue to use and benefit from a product, often as it relates to new or updated feature releases. These notes should be brief, linking out to more details as necessary.

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
1. What stakeholders have to approve this content? Does the legal team have to approve it?

Some example release notes:

- [Jira release notes](https://confluence.atlassian.com/jirasoftware/jira-software-release-notes-776821069.html)
- [Slack](https://slack.com/release-notes/mac) and [more about their release note style](https://slackhq.com/a-little-thing-about-release-notes#)
- [What's new in Google Ad Manager](https://support.google.com/admanager/answer/179039?hl=en)

Related talks:

- [Learning to love release notes](http://www.writethedocs.org/videos/prague/2018/learning-to-love-release-notes-anne-edwards/) at Write The Docs Prague 2018


### Content still needed

#### User Guide / Manuals

#### Tutorials / How-To 

#### Concepts, Overview

## Writing Style

The style guides below focus on the actual writing craft itself. They consider how to make technical content readable, clear, succinct, and engaging.

- [The Sense of Style](https://stevenpinker.com/publications/sense-style-thinking-persons-guide-writing-21st-century)
- [Stylish Academic Writing](http://www.hup.harvard.edu/catalog.php?isbn=9780674064485)
- [Voice and Tone](https://styleguide.mailchimp.com/)
- [Google developer documentation style guide](https://developers.google.com/style/)

## Other resources

Rather than reinvent the wheel, here are some resources curated by [Ivan Walsh](http://www.ihearttechnicalwriting.com/style-guide-technical-writing/) (Kudos!):

- [Brain Traffic — Web Content style guides that Don’t Suck](http://blog.braintraffic.com/2009/02/web-content-style-guides-that-dont-suck/)
- [Creative Blog — Create a website style guide](http://www.creativebloq.com/design/create-website-style-guide-6123030)
- [Gather Content — Developing a Content style guide](http://blog.gathercontent.com/tone-of-voice-guide)
- [HubSpot — How to Create a Writing style guide Built for the Web](http://blog.hubspot.com/blog/tabid/6307/bid/31247/The-Simple-Template-for-a-Thorough-Content-Style-Guide.aspx)
- [Meet Content — Editorial Style for the Web](http://meetcontent.com/blog/elements-of-editorial-style-for-the-web/)
- [Stanford — Creating a web style guide](https://swsblog.stanford.edu/blog/creating-web-style-guide-cardinal-work)
- [Techwhirl – Developing a Style Guide for Technical Publications](http://techwhirl.com/developing-a-departmental-style-guide/)
- [UCR — Writing for the Web, Content Guidelines](http://cms.ucr.edu/writing_web_content.html)
