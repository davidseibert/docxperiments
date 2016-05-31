# Docxperiments

Experiments in Microsoft Word OOXML

## The Problem

Why is it so hard to produce a decent Word file these days?
Pandoc and docutils can get you part of the way, but the limitations 
quickly become clear. There are some good libraries (cheers, python-docx),
but even that can have limitations. More importantly, hiding the markup
behind a library begs the question: Why is it so hard?

A few reasons:

1. The Word OOXML is hidden inside a zipped .docx file, 
   such that most users, even hackers, 
   aren't aware that they have direct access to it.

2. Despite being an 'open' schema, the way that Word uses
   and writes the OOXML is pretty opaque. If you edit the markup
   directly and Word doesn't like it, you'll get a useless error
   message and be sent on your way.

3. Word OOXML is an insanely, obscenely, pointlessly verbose markup language.
   This hides the fact that a Word OOXML document is fairly predictable and
   even simple.

This is a collection of prods and pokes into OOXML, with the vague hope that
at some point we can have a set of functional and robust tools for generating 
OOXML. 

## Reverse Engineering

Part of the process is building up the DOM gradually and seeing what
Word produces in the OOXML. Using some pseudo-OOXML, we can cut through
the nonsense and see what is really happening. Here is a sample progression:

### 1. Blank Document

```xml
<body>
 <p>
  <bookmarkStart/>
  <bookmarkEnd/>
 </p>
 <sectionProperty>
  <pageSize/>
  <pageMargin/>
  <cols>
  <docGrid>
 </sectionProperty>
</body>
```

### 2. Single Paragraph

```xml
<body>
 <p>
  <r>
   <t>
     How does a bastard, orphan, son of a whore,
     and a Scotsman, dropped in the middle of
     a forgotten spot in the Caribbean,
     by providence impoverished in squalor,
     grow up to be a hero and a scholar?
   </t>
  </r>
  <bookmarkStart/>
  <bookmarkEnd/>
 </p>
</body>
```

### 3. Two Paragraphs

```xml
<body>
 <p>
  <r>
   <t>
    How does a bastard, orphan, son of a whore,
    and a Scotsman, dropped in the middle of
    a forgotten spot in the Caribbean,
    by providence impoverished in squalor,
    grow up to be a hero and a scholar?
   </t>
  </r>
 </p>
 <p>
  <r>
   <t>
    The ten-dollar founding father without a father
    got a lot farther by working a lot harder,
    by being a lot smarter, by being a self-starter;
    by fourteen, they placed him
    in charge of a trading charter.
   </t>
  </r>
  <bookmarkStart/>
  <bookmarkEnd/>
 </p>
 <sectionProperty>
  <pageSize/>
  <pageMargin/>
  <cols>
  <docGrid>
 </sectionProperty>
</body>
```

### 4. Runs

Adding some bold and italic text creates an explosion in tags::

```xml
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
 <sectionProperty>
  <pageSize/>
  <pageMargin/>
  <cols>
  <docGrid>
 </sectionProperty>
</body>
```

## Synthesis

It turns out that most of Word's OOXML verbosity is optional.
If you take the last document above, in it's native form,
it actually looks like this (except compressed to a single line)::

```xml
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
```

And this is a two-paragraph document!
But a lot of it can be ignored:

1. The `w:rsidR` tags can be removed.
2. The `w:rsidRPr` tags can be removed.
3. The `w14:textID` and :code:`w14:paraID` tags can be removed.
4. The `w:rsidDefault` tags can be removed.
5. The `w:rsidSect` tag can be removed.
6. The `w:bookmarkStart` and :code:`w:bookmarkEnd` tags can be removed.

It's all noise.
This document can be much simpler with just a few tag substitutions:

1. :code:`<r><t>`: --> :code:`<n>`

   This is just normal, unstyled text.
   I don't know why it needs markup.
   To be be conservative, I'll give it the tag 'n' for 'normal'.

2. :code:`<r><rPr><b/></rPr><t>` --> :code:`<b>`

   Because obviously.

3. :code:`<r><rPr><i/></rPr><t>` --> :code:`<i>`

   Because obviously.

Leaving aside the schemas and section properties for now,
here is the new markup::

```xml
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
```

Not bad. Let's build ourselves a compiler.

```python
import os, difflib
from bs4 import BeautifulSoup
simplified_doc_xml = \
    os.path.realpath(
        '../../../synthesis/stages/'
        '13.8-documentxml_redundant_runs_removed'
        '/decomposed/word/document.xml')
with open(simplified_doc_xml) as f:
    target_markup = f.read()
with open('docx_boilerplate.xml', 'r') as f:
    docx_boilerplate = f.read()[:-1]
with open('section_properties.xml', 'r') as f:
    section_properties = f.read()
with open('test_markup.xml', 'r') as f:
    test_markup = f.read()
replacements = [
    ('<n>', '<w:r><w:t xml:space="preserve">'),
    ('<b>', '<w:r><w:rPr><w:b/></w:rPr><w:t>'),
    ('<i>', '<w:r><w:rPr><w:i/></w:rPr><w:t>'),
    ('</n>', '</w:t></w:r>'),
    ('</b>', '</w:t></w:r>'),
    ('</i>', '</w:t></w:r>'),
    ('<p>', '<w:p>'),
    ('</p>', '</w:p>'),
    ('<sectionProperties/>', section_properties),
    ('<body>', '<w:body>'),
    ('</body>', '</w:body>'),
    ('<docx>', docx_boilerplate),
    ('</docx>', '</w:document>'),
    ]
intermediate = test_markup
for i, j in replacements:
    intermediate = intermediate.replace(i, j)
with open('output.xml', 'w') as f:
    f.write(intermediate)
```

Pop the output into the archive and you've
got yourself a working (albeit naive) docx compiler. Huzzah!

## What next?

Formatting, styles, a dedicated parser and compiler.
Sky's the limit.
