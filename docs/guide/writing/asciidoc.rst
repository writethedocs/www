Introduction to AsciiDoc
========================

What is AsciiDoc?
-----------------

`AsciiDoc <http://asciidoc.org>`_ is a text document format that was explicitly designed with the needs of publishing in mind, both print and web. It supports all the structural elements necessary for writing notes, documentation, articles, books, ebooks, slideshows, web pages, technical manuals and blogs. AsciiDoc is used in static site generators like `Antora <https://antora.org>`_.

AsciiDoc is highly configurable: both the AsciiDoc source file syntax and the backend output markups (which can be almost any type of SGML/XML markup) can be customized and extended by the user.

AsciiDoc files can be translated to many formats including HTML, PDF, EPUB, DocBook, man page. Some websites, like GitHub, render AsciiDoc files directly into HTML.

In 2013, the Asciidoctor project was released. It was an effort to bring a comprehensive and accessible publishing toolchain, centered around the AsciiDoc syntax, to a growing range of ecosystems, including Ruby, JavaScript and the JVM.

Why use AsciiDoc?
-----------------

AsciiDoc is a lightweight markup language that helps you concentrate on writing content rather than being distracted by complex word processors, bury the content in XML schemas like DocBook, or battle with finicky WYSIWYG editors. With AsciiDoc you can forget about layout, typesetting, styling (and even some semantics) and just write.

    You write an AsciiDoc document the same way you would write a normal text document. There are no markup tags or weird format notations. AsciiDoc files are designed to be viewed, edited and printed directly or translated to other presentation formats.

What truly makes AsciiDoc the right investment is that its syntax was designed to be extended as a core feature. This extensibility not only means that AsciiDoc has a lot more to offer, with room to grow, it also fulfills the objective of ensuring your content is maximally reusable.

How to use AsciiDoc?
--------------------

Paragraphs
~~~~~~~~~~

Paragraphs don't require any special markup in AsciiDoc. A paragraph is just one or more lines of consecutive text.

To begin a new paragraph, separate it by at least one blank line. Newlines within a paragraph are not displayed.

Text Formatting
~~~~~~~~~~~~~~~

::

    bold *constrained* & **un**constrained
    
    italic _constrained_ & __un__constrained
    
    bold italic *_constrained_* & **__un__**constrained
    
    monospace `constrained` & ``un``constrained
    
    monospace bold `*constrained*` & ``**un**``constrained
    
    monospace italic `_constrained_` & ``__un__``constrained
    
    monospace bold italic `*_constrained_*` & ``**__un__**``constrained

Section Titles (Headings)
~~~~~~~~~~~~~~~~~~~~~~~~~

Headers are created using equal signs followed by a space. The number of equal signs matches the heading level in the HTML output. For example, Section Level 1 becomes an <h2> heading:::

    = Document Title (Level 0)

    == Level 1 Section Title

    === Level 2 Section Title

    ==== Level 3 Section Title

    ===== Level 4 Section Title

    ====== Level 5 Section Title

    == Another Level 1 Section Title

Headers
~~~~~~~

Headers in AsciiDoc are optional.
The header may not contain blank lines and must be offset from the content by at least one blank line::

    = My Document's Title

    My document provides...

::

    = My Document's Title
    Doc Writer <doc.writer@asciidoctor.org>

    My document provides...

Lists
~~~~~

Unordered lists::

    * Edgar Allen Poe
    * Sheri S. Tepper
    * Bill Bryson

    - Edgar Allen Poe
    - Sheri S. Tepper
    - Bill Bryson

    * level 1
    ** level 2
    *** level 3
    **** level 4
    ***** level 5
    * level 1

Ordered lists::

    . Step 1
    . Step 2
    . Step 3

    . Step 1
    . Step 2
    .. Step 2a
    .. Step 2b
    . Step 3

    . level 1
    .. level 2
    ... level 3
    .... level 4
    ..... level 5
    . level 1

Mixed list::

    Operating Systems::
    Linux:::
        . Fedora
        * Desktop
        . Ubuntu
        * Desktop
        * Server
    BSD:::
        . FreeBSD
        . NetBSD

    Cloud Providers::
    PaaS:::
        . OpenShift
        . CloudBees
    IaaS:::
        . Amazon EC2
        . Rackspace

Checklist::

    * [*] checked
    * [x] also checked
    * [ ] not checked
    *     normal list item

Links
~~~~~

External::

    https://asciidoctor.org - automatic!

    https://asciidoctor.org[Asciidoctor]

    https://github.com/asciidoctor[Asciidoctor @ *GitHub*]

Relative::

    link:index.html[Docs]

Inline anchors::

    [[bookmark-a]]Inline anchors make arbitrary content referenceable.

    [#bookmark-b]#Inline anchors can be applied to a phrase like this one.#

    anchor:bookmark-c[]Use a cross reference to link to this location.

    [[bookmark-d,last paragraph]]The xreflabel attribute will be used as link text in the cross-reference link.

Internal cross-references::

    See <<paragraphs>> to learn how to write paragraphs.

    Learn how to organize the document into <<section-titles,sections>>.

Images
~~~~~~

Block::

    image::sunset.jpg[]

    image::sunset.jpg[Sunset]

    .A mountain sunset
    [#img-sunset]
    [caption="Figure 1: ",link=https://www.flickr.com/photos/javh/5448336655]
    image::sunset.jpg[Sunset,300,200]

Inline::

    Click image:icons/play.png[Play, title="Play"] to get the party started.

    Click image:icons/pause.png[title="Pause"] when you need a break.

    image:sunset.jpg[Sunset,150,150,role="right"] What a beautiful sunset!

Source Code
~~~~~~~~~~~

Code block with title and syntax highlighting::

    .app.rb
    [source,ruby]
    ----
    require 'sinatra'

    get '/hi' do
    "Hello World!"
    end
    ----

Code block with callouts::

    [source,ruby]
    ----
    require 'sinatra' // <1>

    get '/hi' do // <2>
    "Hello World!" // <3>
    end
    ----
    <1> Library import
    <2> URL mapping
    <3> HTTP response body


Tables
~~~~~~

Table with a title, three columns, a header, and two rows of content::

    .Table Title
    |===
    |Name of Column 1 |Name of Column 2 |Name of Column 3 

    |Cell in column 1, row 1
    |Cell in column 2, row 1
    |Cell in column 3, row 1

    |Cell in column 1, row 2
    |Cell in column 2, row 2
    |Cell in column 3, row 2
    |===

Admonitions
~~~~~~~~~~~

AsciiDoc provides five admonition style labels out-of-the-box::

    NOTE: Please note that...

    TIP: Pro tip...

    IMPORTANT: Don't forget...

    WARNING: Watch out for...

    CAUTION: Ensure that...

Admonitions can also encapsulate any block content::

    [IMPORTANT] 
    .Feeding the Werewolves
    ==== 
    While werewolves are hardy community members, keep in mind the following dietary concerns:

    . They are allergic to cinnamon.
    . More than two glasses of orange juice in 24 hours makes them howl in harmony with alarms and sirens.
    . Celery makes them sad.
    ====

Table of Contents
~~~~~~~~~~~~~~~~~

Document with ToC::

    = AsciiDoc Writer's Guide
    Doc Writer <doc.writer@asciidoctor.org>
    v1.0, 2019-08-01
    :toc:

Document with ToC positioned on the right::

    = AsciiDoc Writer's Guide
    Doc Writer <doc.writer@asciidoctor.org>
    v1.0, 2014-08-01
    :toc: right

Include Files
~~~~~~~~~~~~~

::

    = Reference Documentation
    Lead Developer

    This is documentation for project X.

    include::basics.adoc[]

    include::installation.adoc[]

    include::example.adoc[]

    include::https://raw.githubusercontent.com/asciidoctor/asciidoctor/master/README.adoc[]


Resources
---------
* `AsciiDoc <http://asciidoc.org>`_ 
* `AsciiDoc Cheatsheet <https://powerman.name/doc/asciidoc>`_
* `Asciidoctor <https://asciidoctor.org>`_
* `AsciiDoctor Syntax Quick Reference <https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/>`_