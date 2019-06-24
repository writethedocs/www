===================
Introduction to XML
===================

What is XML?
============

XML is a meta markup language developed for the Internet. It is derived from SGML (Standard Generalized Markup Language), the mother of all markup languages. XML was designed to store and transport data. Unlike HTML that defines how data looks, XML defines what data is. Users can use XML "as is" or adapt it to their needs by defining new tags or building blocks.

XML defines a set of rules to encode data in a format that is both human and machine readable. That is why XML syntax is used in Microsoft Office, Apple iWork, LibreOffice, RSS, SVG, and many other tools.

Why Use XML?
============

Because you define your own tags and attributes, you can use XML to create essentially your own markup language. Defining these unique tags and attributes also gives structure to your document.

Additionally, XML stores data in plain text. This makes it independent on the software and hardware to which the data wrapped in XML is being sent, received, and stored. This design also makes it easier to update to new browsers, new operating systems, and new software without losing data. 

How To Use XML
==============

Let's say we want to create a table laying out the trees in a certain region. We could define a <tree> tag that would have the names of the trees, a <height> tag, a <type> tag, and more. These tags give structure to our document and it's still human-readable.::

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

How to Display XML
------------------

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
