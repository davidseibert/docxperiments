word/document.xml
-----------------

.. highlight:: xml

This, obviously, is the main piece of the package.
The original looks like this, in essence::

    <?xml version="1.0" encoding="utf-8"?>
    <w:document mc:Ignorable="w14 w15 wp14"
                xmlns:m="[schema url]"
                xmlns:mc="[schema url]"
                xmlns:mo="[schema url]"
                xmlns:mv="[schema urn]"
                xmlns:o="[schema urn]"
                xmlns:r="[schema url]"
                xmlns:v="[schema urn]"
                xmlns:w="[schema url]"
                xmlns:w10="[schema urn]"
                xmlns:w14="[schema url]"
                xmlns:w15="[schema url]"
                xmlns:wne="[schema url]"
                xmlns:wp="[schema url]"
                xmlns:wp14="[schema url]"
                xmlns:wpc="[schema url]"
                xmlns:wpg="[schema url]"
                xmlns:wpi="[schema url]"
                xmlns:wps="[schema url]">
     <w:body>
      <w:p  w14:paraId="2755313D"
            w14:textId="22B9D595"
            w:rsidR="00617040"
            w:rsidRDefault="009D3123">
       <w:r w:rsidRPr="009D3123">
        <w:t>
         How does a bastard, orphan, son of a whore,
         and a Scotsman, dropped in the middle of
         a forgotten spot in the Caribbean,
         by providence impoverished in squalor,
         grow up to be a hero and a scholar?
        </w:t>
       </w:r>
      </w:p>
      <w:p  w14:paraId="60C4CAE9"
            w14:textId="6037BB23"
            w:rsidR="00F564C0"
            w:rsidRDefault="00F564C0">
       <w:r w:rsidRPr="00F564C0">
        <w:t>
         The ten-
        </w:t>
       </w:r>
       <w:r w:rsidRPr="008937FE">
        <w:rPr>
         <w:b/>
        </w:rPr>
        <w:t>
         dollar
        </w:t>
       </w:r>
       <w:r w:rsidRPr="00F564C0">
        <w:t xml:space="preserve">
         founding
        </w:t>
       </w:r>
       <w:r w:rsidRPr="00E326CC">
        <w:rPr>
         <w:b/>
        </w:rPr>
        <w:t>
         father
        </w:t>
       </w:r>
       <w:r w:rsidRPr="00F564C0">
        <w:t xml:space="preserve">
         without a
        </w:t>
       </w:r>
       <w:r w:rsidRPr="008937FE">
        <w:rPr>
         <w:b/>
        </w:rPr>
        <w:t>
         father
        </w:t>
       </w:r>
       <w:r w:rsidRPr="00F564C0">
        <w:t xml:space="preserve">
         got a
        </w:t>
       </w:r>
       <w:bookmarkStart w:id="0"
                        w:name="_GoBack"/>
       <w:bookmarkEnd w:id="0"/>
       <w:r w:rsidRPr="00F564C0">
        <w:t xml:space="preserve">
         lot
        </w:t>
       </w:r>
       <w:r w:rsidRPr="008937FE">
        <w:rPr>
         <w:b/>
        </w:rPr>
        <w:t>
         farther
        </w:t>
       </w:r>
       <w:r w:rsidRPr="00F564C0">
        <w:t xml:space="preserve">
         by working a lot
        </w:t>
       </w:r>
       <w:r w:rsidRPr="008937FE">
        <w:rPr>
         <w:b/>
        </w:rPr>
        <w:t>
         harder
        </w:t>
       </w:r>
       <w:r w:rsidRPr="00F564C0">
        <w:t xml:space="preserve">
         , by being a lot
        </w:t>
       </w:r>
       <w:r w:rsidRPr="008937FE">
        <w:rPr>
         <w:b/>
        </w:rPr>
        <w:t>
         smarter
        </w:t>
       </w:r>
       <w:r w:rsidRPr="00F564C0">
        <w:t>
         , by being a self-
        </w:t>
       </w:r>
       <w:r w:rsidRPr="008937FE">
        <w:rPr>
         <w:b/>
        </w:rPr>
        <w:t>
         starter
        </w:t>
       </w:r>
       <w:r w:rsidRPr="00F564C0">
        <w:t xml:space="preserve">
         ; by fourteen, they placed him
        </w:t>
       </w:r>
       <w:r>
        <w:t xml:space="preserve">
         in
        </w:t>
       </w:r>
       <w:r w:rsidRPr="008937FE">
        <w:rPr>
         <w:i/>
        </w:rPr>
        <w:t>
         charge
        </w:t>
       </w:r>
       <w:r>
        <w:t xml:space="preserve">
         of a trading
        </w:t>
       </w:r>
       <w:r w:rsidRPr="008937FE">
        <w:rPr>
         <w:b/>
        </w:rPr>
        <w:t>
         charter
        </w:t>
       </w:r>
       <w:r>
        <w:t>
         .
        </w:t>
       </w:r>
      </w:p>
      <w:sectPr w:rsidR="00F564C0"
                w:rsidSect="00E7316D">
       <w:pgSz  w:h="15840"
                w:w="12240"/>
       <w:pgMar w:bottom="1440"
                w:footer="720"
                w:gutter="0"
                w:header="720"
                w:left="1440"
                w:right="1440"
                w:top="1440"/>
       <w:cols w:space="720"/>
       <w:docGrid w:linePitch="360"/>
      </w:sectPr>
     </w:body>
    </w:document>

And this is a two-paragraph document! This does not bode well.
Let's see what simplifications are available:

1. The :code:`w:rsidR` tags can be removed.
2. The :code:`w:rsidRPr` tags can be removed.
3. The :code:`w14:textID` and :code:`w14:paraID` tags can be removed.
4. The :code:`w:rsidDefault` tags can be removed.
5. The :code:`w:rsidSect` tag can be removed.
6. The :code:`w:bookmarkStart` and :code:`w:bookmarkEnd` tags can be removed.

That leaves us with the following. I've taken out
the :code:`w:` prefix on everything,
the :code:`w:document` attributes, and I collapsed the run tags::

    <?xml version="1.0" encoding="utf-8"?>
    <document>
     <body>
      <p>   <!-- paragraph #1 -->
       <r><t>   <!-- regular -->
         How does a bastard, orphan, son of a whore,
         and a Scotsman, dropped in the middle of a
         forgotten spot in the Caribbean, by providence
         impoverished in squalor, grow up to be a hero
         and a scholar?
        </t></r>
      </p>
      <p>   <!-- paragraph #2 -->
       <r><t>   <!-- regular -->
         The ten-
        </t></r>
       <r><rPr><b/></rPr><t>    <!-- bold -->
         dollar
        </t></r>
       <r><t xml:space="preserve">  <!-- regular -->
         founding
        </t></r>
       <r><rPr><b/></rPr><t>    <!-- bold -->
         father
        </t></r>
       <r><t xml:space="preserve">  <!-- regular -->
         without a
        </t></r>
       <r><rPr><b/></rPr><t>    <!-- bold -->
         father
        </t></r>
       <r><t xml:space="preserve">  <!-- regular -->
         got a
        </t></r>
       <r><t xml:space="preserve">  <!-- regular -->
         lot
        </t></r>
       <r><rPr><b/></rPr><t>    <!-- bold -->
         farther
        </t></r>
       <r><t xml:space="preserve">  <!-- regular -->
         by working a lot
        </t></r>
       <r><rPr><b/></rPr><t>    <!-- bold -->
         harder
        </t></r>
       <r><t xml:space="preserve">  <!-- regular -->
         , by being a lot
        </t></r>
       <r><rPr><b/></rPr><t>    <!-- bold -->
         smarter
        </t></r>
       <r><t>   <!-- regular -->
         , by being a self-
        </t></r>
       <r><rPr><b/></rPr><t>    <!-- bold -->
         starter
        </t></r>
       <r><t xml:space="preserve">  <!-- regular -->
         ; by fourteen, they placed him
        </t></r>
       <r><t xml:space="preserve">  <!-- regular -->
         in
        </t></r>
       <r><rPr><i/></rPr><t>    <!-- italic -->
         charge
        </t></r>
       <r><t xml:space="preserve">  <!-- regular -->
         of a trading
        </t></r>
       <r><rPr><b/></rPr><t>    <!-- bold -->
         charter
        </t></r>
       <r><t>   <!-- regular -->
         .
        </t></r>
      </p>
      <sectPr>
       <pgSz    h="15840"
                w="12240"/>
       <pgMar   bottom="1440"
                footer="720"
                gutter="0"
                header="720"
                left="1440"
                right="1440"
                top="1440"/>
       <cols space="720"/>
       <docGrid linePitch="360"/>
      </sectPr>
     </body>
    </document>

One more thing in terms of modifying document.xml itself:
A few of these runs don't seem to be necessary::

    <r><t xml:space="preserve">  <!-- regular -->
      got a
     </t></r>
    <r><t xml:space="preserve">  <!-- regular -->
      lot
     </t></r>
     . . .
    <r><t xml:space="preserve">  <!-- regular -->
      ; by fourteen, they placed him
     </t></r>
    <r><t xml:space="preserve">  <!-- regular -->
      in
     </t></r>

Done::

    <r><t xml:space="preserve">  <!-- regular -->
      got a lot
     </t></r>
     . . .
    <r><t xml:space="preserve">  <!-- regular -->
      ; by fourteen, they placed him in
     </t></r>

So, by this point the document has become fairly simple.
Most of the complication is due to the bizarre OOXML markup
scheme. What is the point of the :code:`<t>` tag?
I think we can get rid of them. We can get rid
of a *lot* of this mess.

New Markup
~~~~~~~~~~

I'll just make a few substitutions:

:code:`<t xml:space="preserve">`
    Nothing.

    The obvious point is to mark the elements where spacing is literal.
    It seems simple to include a rule in a parser that says any multi-word
    element preserves space.

:code:`<r><t>`
    :code:`<n>`

    This is just normal, unstyled text. I don't know why it needs markup.
    To be be conservative, I'll give it the tag 'n' for 'normal'.

:code:`<r><rPr><b/></rPr><t>`
    :code:`<b>`

    Because obviously.

:code:`<r><rPr><i/></rPr><t>`
    :code:`<i>`

    Because obviously.

Leaving aside the section properties for now, here is the new markup::

    <docx>
     <body>
      <p><n>How does a bastard, orphan, son of a whore,
         and a Scotsman, dropped in the middle of a
         forgotten spot in the Caribbean, by providence
         impoverished in squalor, grow up to be a hero
         and a scholar?</n></p>
      <p><n>The ten-</n><b>dollar</b><n> founding </n>
       <b>father</b><n> without a </n><b>father</b>
       <n> got a lot </n><b>farther</b><n> by working a lot </n>
       <b>harder</b><n>, by being a lot </n><b>smarter</b>
       <n>, by being a self-</n><b>starter</b><n>; by fourteen,
       they placed him in </n><i>charge</i><n> of a trading </n>
       <b>charter</b><n>.</n></p>
     </body>
     <sectionProperties/>
    </docx>

Not bad. Let's build ourselves a compiler.

.. highlight:: python
.. doctest::

    >>> import os, difflib
    >>> from bs4 import BeautifulSoup
    >>> simplified_doc_xml = \
    ...     os.path.realpath(
    ...         '../../../synthesis/stages/'
    ...         '13.8-documentxml_redundant_runs_removed'
    ...         '/decomposed/word/document.xml')
    >>> os.path.exists(simplified_doc_xml)
    True
    >>> with open(simplified_doc_xml) as f:
    ...     target_markup = f.read()
    >>> print target_markup # doctest: +ELLIPSIS
    <?xml version="1.0"...
    >>> with open('docx_boilerplate.xml', 'r') as f:
    ...     docx_boilerplate = f.read()[:-1]
    >>> print docx_boilerplate # doctest: +ELLIPSIS
    <?xml version="1.0"...
    >>> with open('section_properties.xml', 'r') as f:
    ...     section_properties = f.read()
    >>> print section_properties # doctest: +ELLIPSIS
    <w:sectPr ><w:pgSz w:w="12240"...
    >>> with open('test_markup.xml', 'r') as f:
    ...     test_markup = f.read()
    >>> print test_markup # doctest: +ELLIPSIS
    <docx><body><p><n>How does a bastard...
    >>> replacements = [
    ...     ('<n>', '<w:r><w:t xml:space="preserve">'),
    ...     ('<b>', '<w:r><w:rPr><w:b/></w:rPr><w:t>'),
    ...     ('<i>', '<w:r><w:rPr><w:i/></w:rPr><w:t>'),
    ...     ('</n>', '</w:t></w:r>'),
    ...     ('</b>', '</w:t></w:r>'),
    ...     ('</i>', '</w:t></w:r>'),
    ...     ('<p>', '<w:p>'),
    ...     ('</p>', '</w:p>'),
    ...     ('<sectionProperties/>', section_properties),
    ...     ('<body>', '<w:body>'),
    ...     ('</body>', '</w:body>'),
    ...     ('<docx>', docx_boilerplate),
    ...     ('</docx>', '</w:document>'),
    ...     ]
    >>> intermediate = test_markup
    >>> for i, j in replacements:
    ...     intermediate = intermediate.replace(i, j)
    >>> with open('output.xml', 'w') as f:
    ...     f.write(intermediate)
    >>> pretty_test_markup = \
    ...     BeautifulSoup(intermediate, "xml").prettify()
    >>> pretty_target_markup = \
    ...     BeautifulSoup(target_markup, "xml").prettify()
    >>> diff = difflib.unified_diff(
    ...     pretty_target_markup.split("\n"),
    ...     pretty_test_markup.split("\n")
    ...     )
    >>> print '\n'.join([ line for line in diff]) # doctest: +NORMALIZE_WHITESPACE
    ---
    <BLANKLINE>
    +++
    <BLANKLINE>
    @@ -3,14 +3,14 @@
    <BLANKLINE>
      <w:body>
       <w:p>
        <w:r>
    -    <w:t>
    +    <w:t xml:space="preserve">
          How does a bastard, orphan, son of a whore,
          and a Scotsman, dropped in the middle of a
          forgotten spot in the Caribbean,
          by providence impoverished in squalor,
          grow up to be a hero and a scholar?
         </w:t>
        </w:r>
       </w:p>
       <w:p>
        <w:r>
    -    <w:t>
    +    <w:t xml:space="preserve">
          The ten-
         </w:t>
        </w:r>
    @@ -88,7 +88,7 @@
    <BLANKLINE>
         </w:t>
        </w:r>
        <w:r>
    -    <w:t>
    +    <w:t xml:space="preserve">
          , by being a self-
         </w:t>
        </w:r>
    @@ -127,7 +127,7 @@
    <BLANKLINE>
         </w:t>
        </w:r>
        <w:r>
    -    <w:t>
    +    <w:t xml:space="preserve">
          .
         </w:t>
        </w:r>

Obviously, I need to touch up the preserve spacing,
but pop the output into the archive and you've
got yourself a working docx compiler. Huzzah!