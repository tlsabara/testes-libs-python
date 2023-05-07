from requests import request
from bs4 import BeautifulSoup


# todo: método de self update

def get_public_ip_addr():
    try:
        site_html = request(method='get', url='https://meuip.com.br').text
        soup = BeautifulSoup(site_html, "html.parser")
        return soup.find('h3').text.split('Meu ip é ')[-1]
    except Exception as e:
        print(e)
        # todo tratar o erro
