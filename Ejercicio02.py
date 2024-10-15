import requests
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.ar/camiseta-independiente-original#D[A:camiseta%20independiente%20original]"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

productos = soup.find_all('span', class_="poly-component__brand")

for producto in productos:
    print(producto.get_text())