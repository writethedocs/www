# Style Guides

A style guide contains a set of standards for writing and designing content. It helps maintain a consistent style, voice, and tone across your documentation, whether you're a lone writer or part of a huge docs team. It can provide guidelines for different documentation deliverables, such as API reference manuals, tutorials, release notes, or overviews of complex technical concepts.

A style guide saves documentarians time and trouble by providing a single reference for writing about common topics, features, and more. 
The guidelines in a style guide help writers to produce documentation that has the same tone and grammatical style, regardless of who writes the documentation.
A consistent tone and style can make your content easier to read by reducing your users' [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) and increasing their confidence in the content's authority. 

## Write your own style guide?

A style guide can be something as simple as a list of decisions you've made about how to refer to different items you frequently write about. Or it can be as complicated as the mighty tomes of major publication houses. 

You can certainly create a style guide of your own. For the sake of simplicity, this approach might work if you're a lone writer or just starting a small docs group. But neither software nor its documentation operates in a vacuum, so it's a good idea to consult other resources as well. Working from an existing style guide can also help you figure out which things matter in your style guide.

## Style guide resources

Style guides have been around for as long as people have been publishing in any format. Older style guides originally intended for specific forms of print publication have become basic standards for many others to refer to, including documentarians:

- The [Chicago Manual of Style](http://www.chicagomanualofstyle.org/book/ed17/frontmatter/toc.html)
- The [AP Stylebook](https://www.apstylebook.com/)

Classics for software documentation include:

- [Microsoft Writing Style Guide](https://docs.microsoft.com/en-us/style-guide/welcome/)
- [IBM style guide](https://www.ibm.com/developerworks/library/styleguidelines/)
- [Apple Style Guide](https://help.apple.com/applestyleguide/)

Others you might find useful:

- [Google developer documentation style guide](https://developers.google.com/style)
- [Salesforce Style Guide](https://developer.salesforce.com/docs/atlas.en-us.salesforce_pubs_style_guide.meta/salesforce_pubs_style_guide/overview.htm)
- [The Red Hat Style Guide](http://stylepedia.net/style/)
- [Rackspace Style Guide](https://docs.rackspace.com/docs/style-guide/)
- [18F Content Guide](https://content-guide.18f.gov)
- [Open SUSE Style Guide](https://documentation.suse.com/style/current/single-html/docu_styleguide/)
- [gnome Style Guide](https://developer.gnome.org/gdp-style-guide/2.32/gdp-style-guide.html)

## Thinking about accessibility and bias

It's important to consider accessibility and biases in your style guide to ensure that all readers can understand the content you produce. 

### Writing for accessibility

Writing for accessibility includes making sure copy can be read by screenreaders, content organization, style and color of text emphasis, and more.

- [Atlassian Design System - Inclusive writing reference](https://atlassian.design/content/inclusive-writing)
- [MailChimp's writing style guide](https://styleguide.mailchimp.com/writing-for-accessibility/)
- [A11Y Style Guide](https://a11y-style-guide.com/style-guide/)
- [The Accessibility Cheatsheet](https://bitsofco.de/the-accessibility-cheatsheet/) by bitsofcode
- [Microsoft Style Guide Accessibility Terms](https://docs.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/accessibility-terms)


Relevant talks from Write the Docs:

- [A11y-Friendly Documentation](https://www.writethedocs.org/videos/prague/2018/a11y-friendly-documentation-carolyn-stransky/) at Write the Docs Prague 2018
- [Inclusive Tech Docs - TechComm Meets Accessibility](http://www.writethedocs.org/videos/eu/2015/inclusive-tech-docs-techcomm-meets-accessibility-rmatic/) at Write the Docs EU 2015

### Reducing bias in your writing

You can reduce bias in your writing by considering the meanings and origins of your word choices and how those might be perceived or understood by your readers.
Even thinking twice about what example user names you include in your documentation can significantly reduce bias in your documentation.
Fortunately, resources are increasingly available to help you with this kind of attention to your writing.

Free guides:

- [Atlassian Design System - Inclusive Writing](https://atlassian.design/content/inclusive-writing)
- [Google's Developer Style Guide on Inclusive Documentation](https://developers.google.com/style/inclusive-documentation)
- [Microsoft Style Guide on Bias-Free Communication](https://docs.microsoft.com/en-us/style-guide/bias-free-communication)
- [American Psychological Association (APA)'s Guide on Bias-Free Language](https://apastyle.apa.org/style-grammar-guidelines/bias-free-language/)

Free resources:

- [Internet Engineering Task Force (IETF) on Terminology, Power, and Oppressive Language](https://tools.ietf.org/id/draft-knodel-terminology-00.html)
- [The Conscious Style Guide - a collection of resources](https://consciousstyleguide.com/)
- [Diversity Style Guide](https://www.diversitystyleguide.com/)
- [Linguistic Society of America Guidelines for Inclusive Language](https://www.linguisticsociety.org/resource/guidelines-inclusive-language)
- [Linguistic Society of America Additional Inclusive Language Resources](https://www.linguisticsociety.org/content/further-content-related-inclusive-language-guidelines)
- [American Psychological Association (APA)'s Guide on Bias-Free Language](https://apastyle.apa.org/style-grammar-guidelines/bias-free-language/)

Paid resources:

- [The Responsible Communication Style Guide](https://rcstyleguide.com/)

Relevant talks from Write the Docs:

- [What They Don’t Tell You About Creating New Style Guides](https://www.writethedocs.org/videos/portland/2018/what-they-don-t-tell-you-about-creating-new-style-guides-thursday-bram/)

### Providing inclusive example names

- Wikipedia's lists of [most common forenames](https://en.wikipedia.org/wiki/List_of_most_popular_given_names) and [most common surnames](https://en.wikipedia.org/wiki/Lists_of_most_common_surnames) by region.
- [Splunk style guide on example names](https://docs.splunk.com/Documentation/StyleGuide/current/StyleGuide/Domains)
- [Behind the Name - name generator](https://www.behindthename.com/random/)
- [The Story Shack - name generators](https://thestoryshack.com/tools/)

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

### Error messages

Mistakes in the software are unavoidable. Users might click on a link that turns out to be broken, or they might perform an action only to be met with an error. This is where error messages come into play and it's important to write them in a way that doesn't alienate the user. 

Here are a few tips on what makes a good error message: 

- Provide explicit indication that something has gone wrong. 
- Write like a human, not a robot. 
- Don't blame the user – be humble. 
- Make the message short and meaningful. 
- Include precise descriptions of exact problems. 
- Offer constructive advice on how to fix the problem. 

Related resources: 
- [Error Message Guidelines – NN Group](https://www.nngroup.com/articles/error-message-guidelines/)
- [How to Write Good Error Messages – UX Planet](https://uxplanet.org/how-to-write-good-error-messages-858e4551cd4)
- [How to write better error messages – opensource.com](https://opensource.com/article/17/8/write-effective-error-messages)

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
