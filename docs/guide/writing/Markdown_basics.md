# Markdown basics

## What is Markdown?

Markdown is a simple formatting syntax. You can use it for creating webpages, documents or any text that needs to be transformed into other formats like HTML.

## Why to use Markdown?

It makes it easier for non-tech writers to produce documentation that can be collaborative and flexible at the same time.

## How to use Markdown?

### How to format text in Markdown?

If you need to format the text, just follow these rules:
  - For italics, you need to wrap the item with one star on each side, like this: `*one star on each side*`.
  - For bold letters, you need to wrap the item with two stars on each side, like this: `**two stars on each side**`.
  - If you are using GitHub, you also have a possibility of using a strikethrough formatting, like this: `~~strikethrough~~`.
  - You can also add links like this: `[This text links to WritetheDocs](https://www.writethedocs.org)`.

This will render like this:

- For italics, you need to wrap the item with one star on each side, like this: *one star on each side*.
- For bold letters, you need to wrap the item with two stars on each side, like this: **two stars on each side**.
- If you are using GitHub, you also have a possibility of using a strikethrough formatting, like this: ~~strikethrough~~.
- You can also add links like this: [This text links to WritetheDocs](https://www.writethedocs.org).

### How to add images?

Adding images works like adding links, the only difference being an exclamation mark at the beginning of the line, like this:

`![alt text](https://pbs.twimg.com/profile_images/556169790587281409/AwkaVrhP_400x400.png).`

This will render an image like this:

![alt text](https://pbs.twimg.com/profile_images/556169790587281409/AwkaVrhP_400x400.png).

### How to produce lists of items?

If you need to add an unordered (that is, bulleted) list of items, here is how to go about it.

```
- Just add a dash first and then write a text.
- If you add another dash in the following line, you will have another item in the list.
  - If you add four spaces or use a tab key, you will create an indented list.
    - If you need to insert an indented list within an intended one, just press a tab key again.
```

This will render like this:

- Just add a dash first and then write a text.
- If you add another dash in the following line, you will have another item in the list.
  - If you add four spaces or use a tab key, you will create an indented list.
    - If you need to insert an indented list within an intended one, just press a tab key again.

If you need to add an ordered (that is, numbered) list of items, here is the syntax:

```
1. Just type a number followed by a dot.
2. If you want to add a second item, just type in another number followed by a dot.
1. If you make a mistake when typing numbers, fear not, Markdown will correct it for you.
  1. If you press a tab key or type four spaces, you will get an indented list and the numbering 
  will start from scratch.
    1. If you want to insert an indented numbered list within an existing indented numbered one, 
    just press the tab key again.
      - If need be, you can also add an indented unordered list within an indented numbered one, an vice versa, 
      by pressing a tab key and typing a dash.
```

This will render like this:

1. Just type a number followed by a dot.
2. If you want to add a second item, just type in another number followed by a dot.
1. If you make a mistake when typing numbers, fear not, Markdown will correct it for you.
  1. If you press a tab key or type four spaces, you will get an indented list and the numbering will start from scratch.
    1. If you want to insert an indented numbered list within an existing indented numbered one, 
    just press the tab key again.
      - If need be, you can also add an indented unordered list within an indented numbered one, an vice versa, 
      by pressing a tab key and typing a dash.

### Headers

If you have longer documents, it is better to give them some structure, which you can actually achieve with headers. You do this with hashes (#):

`# This is a first-tier header`

`## This is a second-tier header`

`### This is a third-tier header`

And so on, up to a sixth-tier header.

This is how these lines will be rendered:

# This is a first-tier header

## This is a second-tier header

### This is a third-tier header

Since we have just seen headers, we want now to divide this section from the following one with a horizontal ruler. This can be achieved by adding 3 stars separated by spaces, like this:

`* * *`

This is what a rendering of a division line looks like:

* * *

### Quotes and Code

If you need to quote someone in your document, you do by adding a > character at the beginning of each line, like this:

```
> “I make Jessica Simpson look like a rock scientist.”

> —Tara Reid, actress
```

And this is what a quote looks like:

> “I make Jessica Simpson look like a rock scientist.”

> —Tara Reid, actress

And finally, if you need to insert code into your text, you can do it with one apostrophe on each side when adding code within one line, or with 3 apostrophes opening and closing your code block, like this:

This line contains \`code\`

This is a code section:

<pre>
```
this is code
```
</pre>

Which will render like this:

This line contains `code`

This is a code section:

```
this is code
```

You can also "cheat", adding HTML-formatted text when markdown seems too limited, but first look at these resources to find solutions:

### Resources

- [The fundamental guide for using Markdown](https://daringfireball.net/projects/markdown/)
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [Atom - a flexible editor that you can use for formatting Markdown texts](https://atom.io/)
- [Stackedit - an online Markdown editor](https://stackedit.io/editor)
- [Codecademy course on Markdown](https://www.codecademy.com/courses/web-intermediate-en-Bw3bg/0/1)
