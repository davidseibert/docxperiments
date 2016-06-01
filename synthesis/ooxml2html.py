import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup
from xml.dom import minidom
from StringIO import StringIO

OOXML_FILE = 'test.oo.xml'

with open(OOXML_FILE) as f:
    ooxml_str = f.read()

html_target = """<!DOCTYPE html>
<html><body><p>How does a bastard, orphan, son of a whore, and a Scotsman, dropped in the middle of a forgotten spot in the Caribbean, by providence impoverished in squalor, grow up to be a hero and a scholar?</p><p>The ten-<b>dollar</b> founding <b>father</b> without a <b>father</b> got a lot <b>farther</b> by working a lot <b>harder</b>, by being a lot <b>smarter</b>, by being a self-<b>starter</b>; by fourteen, they placed him in <i>charge</i> of a trading <b>charter</b>.</p></body></html>"""



print ""
print "----- xml test -----"

#print ooxml_str

def basic_precleaning(dirty_ooxml):
    intermediate = dirty_ooxml
    # Remove namespaces
    intermediate = re.sub(' xmlns\S+"', '', intermediate)
    intermediate = re.sub('w:', '', intermediate)

    # Remove random word garbage
    intermediate = re.sub(' mc:Ignorable="w14 w15 wp14"', '', intermediate)
    intermediate = re.sub(' w14:\w+="\w{8}"', '', intermediate)
    intermediate = re.sub(' rsid\w+="\w{8}"', '', intermediate)
    intermediate = re.sub(' xml:space="preserve"', '', intermediate)
    intermediate = re.sub(r'<bookmark[^>]+>', ' ', intermediate)
    intermediate = re.sub(r'<sectPr.+</sectPr>', '', intermediate)

    clean_ooxml = intermediate
    return clean_ooxml

def post_cleaning(processed_ooxml):
    intermediate = processed_ooxml
    intermediate = re.sub(' {2,}', ' ', intermediate)
    print intermediate
    return intermediate

def prettification(finished_ooxml):
    soup = BeautifulSoup(finished_ooxml, "html5lib")
    pretty = soup.prettify()
    return pretty


def revise_markup(clean_ooxml):
    intermediate = clean_ooxml

    intermediate = re.sub(r'<\?xml[^<]+>', r'<!DOCTYPE html>', intermediate)
    intermediate = re.sub(r'<document>', r'<html>', intermediate)
    intermediate = re.sub(r'</document>', r'</html>', intermediate)
    intermediate = re.sub(r'<r><rPr><b/></rPr><t>([^<]+)</t></r>', r'<b>\g<1></b>', intermediate)
    intermediate = re.sub(r'<r><rPr><i/></rPr><t>([^<]+)</t></r>', r'<i>\g<1></i>', intermediate)
    intermediate = re.sub(r'<r><t>([^<]+)</t></r>', r'\g<1>', intermediate)

    cleaner_ooxml = post_cleaning(intermediate)
    pretty = prettification(cleaner_ooxml)
    return pretty



def main():
    clean_ooxml = basic_precleaning(ooxml_str)
    print revise_markup(clean_ooxml)

if __name__ == '__main__':
    main()
