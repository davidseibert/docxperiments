===============================
Spin-off: Minimum Viable Markup
===============================

.. highlight:: xml

Intro
-----

I was playing around with the innards of some docx files
and found that all this :code:`rsid` business
was *quite complicated*. Intimidatingly so.

However, I found that adding in a few run, text,
and bold tags to a file and recompressing it did work
*even without any of those tags.*
From there I messed about further and eventually I even copied in some
raw markup from a fairly complicated table in another docx file,
with custom paragraph styles, and that worked!
The styles were stripped, of course, but the table
made it through intact, with the correct proportions and borders,
with no complaints from Word.
I didn't edit any of the markup; it had undefined style names
and undefined document property fields.

So, I thought: How much can I get away with?
How strict *is* word?

Recompressing my pretty files does *not* work, which is too bad.
Editing the ugly files is annoying.
I think the extra spaces between the tags is the problem,
but I'm not going to try to solve that for now.
I started removing tags at random from some of the ugly files
and found that I could get away with not having many of them.
That means that, theoretically,
creating a docx from scratch might be manageable if I
can just need to nail down the bare minimum that Word requires.
After tooling around randomly, I thought I should
make it a bit more rigorous.
Starting with the docx file from specimen four,
I'm going to strip away as much as I can.

Here we go.

The whole directory structure looks like this::

    DOCX
    ├── [Content_Types].xml
    ├── _rels
    │   └── .rels
    ├── docProps
    │   ├── app.xml
    │   ├── core.xml
    │   └── thumbnail.jpeg
    └── word
        ├── _rels
        │   └── document.xml.rels
        ├── document.xml
        ├── fontTable.xml
        ├── settings.xml
        ├── styles.xml
        ├── theme
        │   └── theme1.xml
        └── webSettings.xml

It's pretty scary. But, a lot of this can be
deleted without a second thought, it turns out.
This is the most minimal structure I could get to work::

    DOCX
    ├── [Content_Types].xml
    ├── _rels
    │   └── .rels
    └── word
        ├── document.xml
        └── theme
            └── theme1.xml


.. toctree::
    :maxdepth: 2

    documentxml
    minorfiles

