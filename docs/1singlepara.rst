===========
1singlepara
===========

docProps/app.xml
----------------

Changes
~~~~~~~


TotalTime
    0 to 1

Words
    0 to 29

Characters
    0 to 166

Lines
    0 to 1

Paragraphs
    0 to 1

CharacterWithSpaces
    0 to 194

word/settings.xml
-----------------

Changes
~~~~~~~

Two new `<w:rsid>` tags, inserted alphabetically:

+  `<w:rsid w:val="009D3123"/>`
+  `<w:rsid w:val="00FD3E79"/>`


word/document.xml
-----------------

Changes
~~~~~~~

`<w:r>` and `<w:t>` tags added to an already existing `<w:p>` tag.

Before::

    <w:p w14:paraId="2755313D"
        w14:textId="77777777"
        w:rsidR="00617040"
        w:rsidRDefault="00617040">

After::

    <w:p w14:paraId="2755313D"
        w14:textId="22B9D595"
        w:rsidR="00617040"
        w:rsidRDefault="009D3123">
     <w:r w:rsidRPr="009D3123">
      <w:t>
       How does a bastard, orphan, son of a whore, and a Scotsman,
       dropped in the middle of a forgotten spot in the Caribbean,
       by providence impoverished in squalor,
       grow up to be a hero and a scholar?
      </w:t>
     </w:r>
