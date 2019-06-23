===================
Introduction to XML
===================

What is XML?
============

Similar to reStructuredText, Markdown, and HTML, XML is a markup language. Unlike other markup languages, it is not predefined and you must define your own tags and attributes. It's different from other markup languages in that instead of being used to present content on a page, it distributes that page's data over the Internet.

XML defines a set of rules to encode data in a format that is both human-readable and understandable to computers.

With XML, you can define your own unique tags and attributes. HTML, for example, is more rigid in that all of its tags are predefined. Many document formats use XML syntax, including Microsoft Office, Apple iWork, LibreOffice, RSS, and the SVG vector graphic format.

Why Use XML?
============

Because you define your own tags and attributes, you can use XML to create essentially your own markup language. Defining these unique tags and attributes also gives structure to your document.

Additionally, XML stores data in plain text. This makes it independent on the software and hardware to which the data wrapped in XML is being sent, received, and stored. This design also makes it easier to update to new browsers, new operating systems, and new software without losing data. 

How To Use XML
==============

Let's say we wanted to create a table laying out the trees in a certain region. We could define a <tree> tag that would have the names of the trees, a <height> tag, a <type> tag, and more. These tags give structure to our document and it's fairly easily readable to humans.::

    <tree>
        <name> Sugar Maple </name>
        <height units="m"> 30 </height>
        <type> Deciduous </type>
    </tree>

    <tree>
        <name> Black Walnut </name>
        <height units="m"> 16 </height>
        <type> Deciduous </type>
    </tree>
    
XML is often used in concert with HTML, CSS, and JavaScript.

Displaying XML
--------------

XML needs a stylesheet to be readable and usable. Stylesheets for XML work much the same as those for HTML. The difference is that we assign styles to our unique XML tags, not to the standard tags used in HTML.::

    <?xml-stylesheet type="text/css" href="nutrition.css"?>
 
    name {
        font-family: "Cooper Black", serif;
        font-size: 3em;
        font-style: bold;
    }
    
    height, type {
        font-family: "Bodoni", serif;
        font-size: 1em;
        font-style: none;
    }        
 
Resources
=========

`W3Schools tutorial on XML <https://www.w3schools.com/xml/default.asp>`_
`Using XML by A List Apart <https://alistapart.com/article/usingxml/#comments>`_
