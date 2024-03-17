import requests
from pyquery import PyQuery as pq

# website main domain onde conseguimos montar as urls
domain_base = 'https://www.fragrantica.com.br/'

# url para acessar página com todos os países
domain_country_list = 'https://www.fragrantica.com.br/country/'

# headers para validar o acesso a página
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

# função para pegar lista de países mais suas urls
def get_country(domain_country_list, headers):
    r = requests.get(domain_country_list, headers=headers)
    status = r.status_code
    if status == 200:
        html_content = r.text
        doc = pq(html_content)
        countries_info = []
        for a_tag in doc('.countrylist a'):
            a_tag = pq(a_tag)
            country_name = a_tag.text()
            href_country = a_tag.attr('href')
            countries_info.append({'name': country_name, 'href_country': href_country})
        return countries_info
    else:
        print(f"Ocorreu o seguinto erro {status} em sua requisição.")

# função para pegar lista de marcas por país e suas urls
def get_brand(domain_each_country, headers):
    r = requests.get(domain_each_country, headers=headers)
    status = r.status_code
    if status == 200:
        html_content = r.text
        doc = pq(html_content)
        brand_list = []
        for a_tag in doc('.designerlist a'):
            a_tag = pq(a_tag)
            brand_name = a_tag.text()
            href_brand = a_tag.attr('href')
            brand_list.append({'brand_name': brand_name, 'href_brand': href_brand})
        return brand_list
    else:
        print(f"Ocorreu o seguinto erro {status} em sua requisição.")