from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd

req = Request(
    url='https://www.zapimoveis.com.br/venda/terrenos-lotes-condominios/pe+olinda/?onde=,Pernambuco,Olinda,,,,,,BR%3EPernambuco%3ENULL%3EOlinda,-7.992019,-34.842237,&tipos=lote-terreno_residencial&transacao=venda',
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
html = urlopen(req)
listdata = []


def get_data(url):
    bs = BeautifulSoup(html, 'html.parser')
    listing = bs.find_all("div", {"class": "card-container js-listing-card"})

    data = []

    for list in listing:
        item = {}
        item['id'] = list['data-id']
        item['Preco'] = list.p.strong.get_text()
        item['image'] = list.find('img', {'class': 'img'})['src']
        data.append(item)
    return data


def export_data(data):
    df = pd.DataFrame(data)
    df.to_excel('terrenos.xlsx')


if __name__ == '__main__':
    data = get_data(req)
    export_data(data)
    print('fim.')
