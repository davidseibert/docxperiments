import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup
from xml.dom import minidom
from StringIO import StringIO
import difflib

OOXML_FILE = 'test.oo.xml'
SYNTH_OOXML = 'synth.oo.xml'

with open(OOXML_FILE) as f:
    ooxml_str = f.read()

with open(SYNTH_OOXML) as f:
    synth_ooxml_str = f.read()


html_target = "<!DOCTYPE html>\n<html><body><p>How does a bastard, orphan, son of a whore, and a Scotsman, dropped in the middle of a forgotten spot in the Caribbean, by providence impoverished in squalor, grow up to be a hero and a scholar?</p><p>The ten-<b>dollar</b> founding <b>father</b> without a <b>father</b> got a lot <b>farther</b> by working a lot <b>harder</b>, by being a lot <b>smarter</b>, by being a self-<b>starter</b>; by fourteen, they placed him in <i>charge</i> of a trading <b>charter</b>.</p></body></html>"




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
    #print intermediate
    return intermediate

def prettification(finished_ooxml):
    soup = BeautifulSoup(finished_ooxml, "html.parser")
    pretty = soup.prettify()
    return pretty


def revise_markup(clean_ooxml):
    intermediate = clean_ooxml
    
    intermediate = re.sub(r'<!DOCTYPE html>', r'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>', intermediate)

    #intermediate = re.sub(r'<\?xml[^<]+>', r'<!DOCTYPE html>', intermediate)
    intermediate = re.sub(r'<html>', r'<w:document>', intermediate)
    intermediate = re.sub(r'</html>', r'</w:document>', intermediate)
    intermediate = re.sub(r'<body>', r'<w:body>', intermediate)
    intermediate = re.sub(r'</body>', r'</w:body>', intermediate)
    intermediate = re.sub(r'<b>', r'<w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">', intermediate)
    intermediate = re.sub(r'</b>', r'</w:t></w:r>', intermediate)
    intermediate = re.sub(r'<i>', r'<w:r><w:rPr><w:i/></w:rPr><w:t xml:space="preserve">', intermediate)
    intermediate = re.sub(r'</i>', r'</w:t></w:r>', intermediate)
    intermediate = re.sub(r'<p>([^<]+)</p>', r'<w:p><w:r><w:t xml:space="preserve">\g<1></w:t></w:r></w:p>', intermediate)
    intermediate = re.sub(r'<p>([^<]+)<w:r>', r'<w:p><w:r><w:t xml:space="preserve">\g<1></w:t></w:r><w:r>', intermediate)
    intermediate = re.sub(r'</w:r>([^<]+)<w:r>', r'</w:r><w:r><w:t xml:space="preserve">\g<1></w:t></w:r><w:r>', intermediate)
    intermediate = re.sub(r'</w:r>([^<]+)</p>', r'</w:r><w:r><w:t xml:space="preserve">\g<1></w:t></w:r></w:p>', intermediate)
    #intermediate = re.sub(r'</document>', r'</html>', intermediate)
    #intermediate = re.sub(r'<r><rPr><b/></rPr><t>([^<]+)</t></r>', r'<b>\g<1></b>', intermediate)
    #intermediate = re.sub(r'<r><rPr><i/></rPr><t>([^<]+)</t></r>', r'<i>\g<1></i>', intermediate)
    #intermediate = re.sub(r'<r><t>([^<]+)</t></r>', r'\g<1>', intermediate)
    intermediate = re.sub(r'<head></head>', r'', intermediate)
    
    cleaner_ooxml = post_cleaning(intermediate)
    #pretty = prettification(cleaner_ooxml)
    #return pretty
    return cleaner_ooxml

def print_diff():
    print ""
    print "----- diff -----"
    test_markup = revise_markup(html_target).split('><')
    diff = difflib.ndiff(synth_ooxml_str.split('><'), test_markup)
    
    for line in diff:
        print line

def print_strings():
    print ""
    print "----- test -----"
    test_markup = revise_markup(html_target)
    print test_markup
    print ""
    print "----- target -----"
    print synth_ooxml_str
    



def main():
    print_diff()
    print_strings()

if __name__ == '__main__':
    main()