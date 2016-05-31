Minor Files
-----------

.. highlight:: xml

word/styles.xml
~~~~~~~~~~~~~~~

Deleted and opened without complaint,
but the styles were all different, naturally.
I'll have to come back to this one.

word/theme/theme1.xml
~~~~~~~~~~~~~~~~~~~~~

After deleting it, Word opened the file but had to repair it.
I looked inside it and it was pretty uninteresting.

_rels/.rels
~~~~~~~~~~~


Initial State
*************

The original file looks like this, except that I've prettified it::

    <?xml version="1.0" encoding="utf-8"?>
    <Relationships xmlns="[schema url]">
     <Relationship  Id="rId3"
                    Target="docProps/core.xml"
                    Type="[schema url]">
     <Relationship  Id="rId4"
                    Target="docProps/app.xml"
                    Type="[schema url]">
     <Relationship  Id="rId1"
                    Target="word/document.xml"
                    Type="[schema url]">
     <Relationship  Id="rId2"
                    Target="docProps/thumbnail.jpeg"
                    Type="[schema url]">
    </Relationships>

Pretty verbose. I'll simplify it to
the following for clarity's sake::

    <?xml?>
    <Rels>
     <Rel Target="docProps_core.xml"/>
     <Rel Target="docProps_app.xml"/>
     <Rel Target="word_document.xml"/>
     <Rel Target="docProps_thumbnail.jpeg"/>
    </Rels>


Simplification
**************

1. Removing the file entirely: FAIL
2. Removing all four :code:`<Relationship/>` tags: FAIL
3. Removing the :code:`docProps/core.xml` tag: SUCCESS
4. Removing the :code:`docProps/app.xml` tag: SUCCESS
5. Removing the :code:`docProps/thumbnail.xml` tag: SUCCESS

The last three steps were cumulative. In the end,
I had a working file with this::

    <?xml?>
    <Rels>
     <Rel Target="word_document.xml"/>
    </Rels>

Or, in full::

    <?xml version="1.0" encoding="utf-8"?>
    <Relationships xmlns="[schema url]">
     <Relationship  Id="rId1"
                    Target="word/document.xml"
                    Type="[schema url]">
    </Relationships>

It would seem that only the :code:`word/document.xml` is essential,
which makes sense. Even then, I was able further to
remove some of the metadata from the
tags ang get Word to open them,
although it had to repair them.
The most minimal file I could produce was this::

    <Relationships>
     <Relationship  Target="word/document.xml"
                    Type="[schema url]">
    </Relationships>

The :code:`<?xml?>` declaration, the :code:`xmlns` attribute,
and the :code:`Id` attribute were all expendable,
at the cost of having to open the file and have it be repaired.

Having done all this, I now question the utility
of changing this file if it just has
to be copied over anyway. Oh well.
