from bs4 import BeautifulSoup as bs
from html_table_parser import parser_functions as parse

doc = ''

with open('port_list.html', 'r') as fd:
    for line in fd:
        line = line.lstrip()
        doc += line.replace("\n", " ")

soup = bs(doc, "html.parser")
test_table = soup.find('table', {'cellspacing': '1', 'cellpadding': '5', 'width': '100%'})
twod_array = parse.make2d(test_table)

# print 2D array
print(twod_array)