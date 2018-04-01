import lxml.html
from bs4 import BeautifulSoup as bs
from html_table_parser import parser_functions as parse

doc = ''

with open('port_list.html', 'r') as fd:
    for line in fd:
        line = line.lstrip()
        doc += line.replace("\n"," ")
    # print(doc)

root = lxml.html.fromstring(doc)
root.xpath('//tr/td//text()')

for tbl in root.xpath('//table'):
    elements = tbl.xpath('.//tr/td//text()')
    # print(elements)

soup = bs(doc, "html.parser")
test_table = soup.find('table')
twod_array = parse.make2d(test_table)

# print 2D array
print(twod_array)