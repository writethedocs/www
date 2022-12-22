================================
Choosing tools for documentation
================================

One of the most important tasks for the documentation team is choosing what tooling to use for creating the docs.
There are many, many choices out there.
Paid, proprietary tools that can do a lot of the back end heavy lifting for you.
Highly customizable static site generators that offer bespoke pipeline, but require a lot of time and knowledge investment.

How does one go about deciding which set of tools will work best for your situation?

Below are some questions you can ask and some considerations to keep in mind as you go about navigating the doc tooling landscape.

Questions to ask
----------------

- What is your budget?
  Make sure you plan for both money and time.
- What kind of output(s) do you need? 
  Some common outputs include:
  - Website 
  - PDFs
  - Word docs
  - Embedded in the product
  - eBooks
  - Salesforce/Zendesk/help center
- What kind of programming skill do you have access to? 
  Specifically, what (if any) languages?
  Consider both what you yourself or your team already know or are willing to learn and what development resources can be available to you within your company.
- Are you comfortable editing HTMl/CSS/JS directly, or do you want more hand holding?
  Some tools put all of the design and coding work on you.
  Other tools provide helpers and interfaces to minimize the hard coding required.
- Do you prefer to work in a *What You See Is What You Get* environment (WYSIWYG) or do you like using a text editor so formatting doesn't get in the way of writing?
  Whichever you prefer, you still need a way to preview your content as you draft to make sure it turns out as expected.
  Plan for some kind of staging area for yourself and other reviewers.
- How do you plan to handle subject matter expert reviews before publication?
  Some tools require a separate license for each reviewer.
  Others will require that you train some reviewers on how to use tools that might be new to them.
- Is there a support portal already in place (Zendesk, Freshdesk, Salesforce Service, or the like)? 
  The knowledge management solution attached to one of those tools might be a great option.
- What other tooling already exists at your company? 
  Usually, you are better off leaning in to what is already available rather than trying to spin up something new.
  If your end users are already active on a Confluence or SharePoint site, exposing your content there will be much easier than launching yet another place for them to keep track of.
- Do you use or want to use version control (like Git or Subversion)?
  Version control offers some really nice perks and benefits for managing your content, but it also comes with a relatively steep learning curve.
  If you use version control, choose a system already in use at your company.
- How much do you want to be able to reuse or single-source content?
- Do you want to use a markup language? 
  If so, which one? reStructured Text? Markdown? Asciidoc? Docbook? DITA?
- How many contributors are you going to have? Reviewers?
  Licensing fees and training costs can add up quickly depending on who all needs access to your toolset.
- Do you need Continuous Integration/Continuous Deployment pipeline support?
- Will you need to consider translation work?
  If so, you need to make sure that your content works well with the translation pipeline.

Consirations and "Gotchas"
--------------------------

- Static Site Generators can be a great tooling choice, but the time spent spinning them up may cost as much as investing in a commercial tool.
  Consider contracting with an expert for your chosen tool or SSG to get your content looking how you want it.
- Plan who will be responsible for long term maintenance.
  Who will handle tooling upgrades?
  Who will be responsible when something breaks down?
- Most tools come with themes to get you started, but companies are going to want their content to look like their content.
  There is time and knowledge required to implement customizations for the design and the idiosyncrasies of your particular work methods.
- Some tool choices provide for content reuse, and single sourcing is a major topic in technical writing forums.
  However, how content gets reused and who can reuse it may be limiting factors.
- Some tools maintain internal databases of links that propagate changes throughout the docs.
  Other tools leave it up to you to find and replace each link.
  Pages inevitably get moved or deleted.
  Make sure you have a plan in place for managing link maintenance.
- Import or export requirements (to or from other tools or sites, for example?).
  Your content may need to be made available to third party clients or other software consumers that repackage it for their uses.
  Likewise, you may consume content from other sources, such as code examples from an engineering repository.
