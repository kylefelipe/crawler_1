import requests
from bs4 import BeautifulSoup as bs
#termo = str(input("Digite um termo: "))
termo = 'bola'

def get_html(termo):
    html = requests.get(f'https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro/{termo}/')
    parsed_html = bs(html.content, 'html.parser')
    return parsed_html

def get_block():
    html = get_html(termo)
    txt = []
    dicionario = {}
    tags = [tag for tag in html.find_all('div', {'id': 'content'})]
    print(tags)
    # for tag in tags:
    #     tgs = [tg for tg in tag.find_all('div')]
    #     for tg in tgs:
    #         print(f"------------ Tag: {tgs.index(tg)} ------------")
    #         print(tg)
    #         print("------------------------------------------------")
    
    return txt
    
get_block()
