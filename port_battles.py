import argparse

import requests
from bs4 import BeautifulSoup as bs
from html_table_parser import parser_functions as parse
from tabulate import tabulate

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.2) Gecko/20100115 Firefox/3.6'


def main():
    parser = argparse.ArgumentParser(description='Provide credentials')
    parser.add_argument('--login', required=True)
    parser.add_argument('--password', required=True)
    parser.add_argument('--syndicateId', required=True)
    args = parser.parse_args()

    battles = [[]]

    session = requests.Session()
    session.headers.update({'User-Agent': USER_AGENT})
    login_page = session.get('https://www.ganjawars.ru/login.php')

    # Generate POST fields
    form_items = bs(login_page.text, 'lxml')
    post_data = {e['name']: e.get('value', '') for e in form_items.find_all('input', {'name': True})}
    post_data['login'] = args.login
    post_data['pass'] = args.password

    # Login
    session.post('https://www.ganjawars.ru/login.php', data=post_data)

    port_page = session.get('http://www.ganjawars.ru/object.php?id=69403&page=oncoming1&sid=%s' % args.syndicateId)
    session.close()

    # Parse page
    soup = bs(port_page.text, "html.parser")
    battles_table = soup.find_all('table')[-1]
    battles_list = parse.make2d(battles_table)
    del battles_list[0]

    for battle in battles_list:
        del battle[3]
        syndicate_a, syndicate_b = str(battle[2]).split(' vs ', 1)

        if args.syndicateId + ' ' in syndicate_a:
            enemy_syndicate = syndicate_b
        else:
            enemy_syndicate = syndicate_a

        table_row = [battle[0], battle[1], enemy_syndicate]
        battles.append(table_row)

    print(tabulate(battles, headers=['ВРЕМЯ', 'ФОРМАТ', 'ПРОТИВНИК'], tablefmt='simple'))


if __name__ == '__main__':
    main()
