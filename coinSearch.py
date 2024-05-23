## Usando API
## https://moralis.io/get-crypto-data-using-a-python-api-for-cryptocurrency/
## https://www.coingecko.com/learn/python-query-coingecko-api
## https://pypi.org/project/cryptocompare/

from pprint import pprint

import requests ## pip install requests
from bs4 import BeautifulSoup ## pip install beautifulsoup4


def get_table_heading(table):
    '''Extracting Table Heading From Webpage'''

    heading = list()
    thead = table.find('thead').find('tr').find_all('th')[1:7]
    for th in thead:
        heading.append(th.text)

    return heading


def extract_crypto_data(table):
    '''Extracting Crypto Data From Table'''

    crypto_list = list()
    tbody = table.find('tbody').find_all('tr')
    for tr in tbody:
        tds = tr.find_all('td')[1:7]

        crypto_list.append((
            tds[0].text,
            tds[1].find('span').text,
            tds[2].find('div').text,
            tds[3].text,
            tds[4].text,
            tds[5].text,))

    return crypto_list


if __name__ == '__main__':
    url = 'https://crypto.com/price'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')

    heading = get_table_heading(table)
    crypto_data = extract_crypto_data(table)

    pprint(heading)
    pprint(crypto_data)

from pandas import DataFrame ## pip install pandas
crypto_df = DataFrame(crypto_data, columns=heading)
crypto_df.to_csv('result.csv', index=False)
crypto_df.to_json('result.json', index=False) ## https://jsonviewer.stack.hu

