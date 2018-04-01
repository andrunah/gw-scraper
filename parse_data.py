import codecs

from bs4 import BeautifulSoup as bs
from html_table_parser import parser_functions as parse
from tabulate import tabulate

doc = ''
resultset = [[]]


with codecs.open('port_list.html', 'r', encoding='cp1251', errors='ignore') as fd:
    for line in fd:
        line = line.lstrip()
        line = line.replace("&nbsp;", " ")
        doc += line.replace("\n", " ")

soup = bs(doc, "html.parser")
test_table = soup.find('table', {'cellspacing': '1', 'cellpadding': '5', 'width': '100%'})
twod_array = parse.make2d(test_table)
twod_array[0] = ['Время', 'Формат', 'Участники', 'Контроль']

for battle in twod_array:
    i = 0
    del battle[3]
    if battle[2] != 'Участники':
        sind1, sind2 = str(battle[2]).split(' vs ', 1)
        sind_1 = sind1.split(' ', 1)
        sind_2 = sind2.split(' ', 1)
        tlist = [battle[0], battle[1], sind_1[0].replace('#', ''), sind_1[1], sind_2[0].replace('#', ''), sind_2[1]]
        resultset.append(tlist)
        i += i
print(tabulate(resultset, tablefmt='simple'))
