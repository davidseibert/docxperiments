=========================
Adding a Second Paragraph
=========================

.. highlight:: xml

Procedure
---------

Starting with a single paragraph:

.. image:: ./screenshots/1-singlepara1024.png

I added a second paragraph:

.. image:: ./screenshots/2-secondpara1024.png

Results
-------

Document XML Changes
~~~~~~~~~~~~~~~~~~~~

Something went wrong. Adding the first paragraph gave me this::

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
     <sectionProperty>
      <pageSize/>
      <pageMargin/>
      <cols>
      <docGrid>
     </sectionProperty>
    </body>

Somehow, the second paragraph yielded *this*::

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
       </t>
      </r>
      <r>
       <t>
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

What happened? Somehow, the second paragraph got divided
into a pair of runs. I recreated the docx and the same
thing happened, in the same location. I wonder what it means.


