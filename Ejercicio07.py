import requests
from bs4 import BeautifulSoup

import json
from pymongo import MongoClient

#url = "https://listado.mercadolibre.com.ar/camiseta-independiente-original#D[A:camiseta%20independiente%20original]"
url = "https://listado.mercadolibre.com.ar/cerveza#D[A:cerveza]"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

productos = soup.find_all('div', class_="poly-card__content")

data = []  # Inicializamos una lista

for producto in productos:
    titulo = producto.find('h2', class_='poly-box poly-component__title')
    precio = producto.find('span', class_='andes-money-amount andes-money-amount--cents-superscript')
    simbolo = producto.find('span', class_='andes-money-amount__currency-symbol')

    if titulo and precio and simbolo:
        producto_data = {
            "titulo": titulo.get_text(strip=True),
            "precio": precio.get_text(strip=True),
            "simbolo": simbolo.get_text(strip=True)
        }
        data.append(producto_data) # Agrega un elemento al final de una lista existente

# Print JSON data
json_data = json.dumps(data, ensure_ascii=False, indent=2)
print(json_data)


client = MongoClient('mongodb://localhost:27017/') 

db = client['dbi12']  # Reemplazar de la base de datos 
collection = db['meli']  # Reemplazar por la base de datos

# Insertamos el JSON en MongoDB
if data:
    collection.insert_many(data)

print("JSON ingresado en MongoDB.")