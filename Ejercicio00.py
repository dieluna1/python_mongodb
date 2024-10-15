import requests
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.ar/camiseta-independiente-original#D[A:camiseta%20independiente%20original]"

response = requests.get(url)  ## carga todo el contenido de la página

soup = BeautifulSoup(response.content, 'html.parser')

productos = soup.find_all('div', class_="poly-card__content")

for producto in productos:
    print(producto.get_text())
    print("\n")