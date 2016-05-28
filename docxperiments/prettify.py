# coding: utf-8

from bs4 import BeautifulSoup

def prettify(xml_file_path):
    with open(xml_file_path) as f:
        soup = BeautifulSoup(f, 'xml')
    return soup.prettify()

def main():
    pretty = prettify('../tests/testdata/ugly.xml')
    utf_pretty = pretty.encode('utf-8')
    print utf_pretty

if __name__ == '__main__':
    main()
