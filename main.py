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

# url para acessar marcas por país
domain_each_country = domain_base + countries_info[0]['href']

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

# função para pegar as fragâncias por marca, ano, gênero e suas urls
def get_fragrances(brands_url, headers):
    r = requests.get(brands_fragrances, headers=headers)
    if r.status_code == 200:
        html_content = r.text
        doc = pq(html_content)
        fragrance_list = []
        for a_tag in doc('.flex-child-auto a'):
            a_tag = pq(a_tag)
            fragrance_name = a_tag.text()
            href_fragrance = a_tag.attr('href')
            for span_tag in doc('.flex-container.align-justify'):
                span_tag = pq(span_tag)
                fragrance_type_year = span_tag.text()
            fragrance_list.append({'fragrance_name': fragrance_name, 'href_fragrance': href_fragrance, 'fragrance_type_year':fragrance_type_year})
        return fragrance_list
    else:
       print(f"Ocorreu o seguinto erro {status} em sua requisição.")
