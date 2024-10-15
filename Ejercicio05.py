import requests
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.ar/camiseta-independiente-original#D[A:camiseta%20independiente%20original]"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

productos = soup.find_all('div', class_="poly-card__content")

for producto in productos:
    titulo = producto.find('h2', class_='poly-box poly-component__title')
    print(titulo.get_text())
