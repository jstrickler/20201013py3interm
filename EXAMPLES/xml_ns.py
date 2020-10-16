#!/usr/bin/env python
from pprint import pprint
import lxml.etree as ET

XML_FILE = '../DATA/libreoffice_content.xml'

TAG_LIST = [  # <1>
    'style:font-face',
    'text:list-style',
]

ATTRIBUTE_LIST = [  # <2>
    'text:name',
    'style:name',
]


def main():

    doc = ET.parse(XML_FILE)  # <3>

    root = doc.getroot()  # <4>

    print("Namespace map:\n")
    pprint(root.nsmap)  # <5>
    print("\n\n")

    print("Finding nodes by tags:\n")

    for tag in TAG_LIST:
        xpath = './/' + tag  # <6>
        node = root.find(xpath, root.nsmap)  # <7>
        print("Searching for tag [{}]\n".format(xpath))
        print_node(node)

    print("Finding nodes by attributes:\n")

    for attribute in ATTRIBUTE_LIST:
        xpath = './/*[@{}]'.format(attribute)  # <8>
        node = root.find(xpath, root.nsmap)
        print("Searching for attribute [{}]\n".format(xpath))
        print_node(node)


def print_node(node):
    node_as_string = ET.tostring(node, pretty_print=True).decode()  # <9>
    print(node_as_string, '\n')

if __name__ == '__main__':
    main()
