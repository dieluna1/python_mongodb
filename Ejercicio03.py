import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')  # Instalación por default

db = client['unaj']  # Reemplaza con tu base de datos
collection = db['meli']  # Reemplaza con tu coleccion

url = "https://listado.mercadolibre.com.ar/camiseta-independiente-original#D[A:camiseta%20independiente%20original]"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

productos = soup.find_all('h2', class_="poly-box poly-component__title")

# Insertamos cada titulo en MongoDB
for producto in productos:
    title = producto.get_text().strip()  # Obtenemos el text and eliminamos los espacios
    if title:  # Solo inserta titulos si no esta vacio
        collection.insert_one({"titulo": title})  # Insertamos un documento

# Recorremos e imprimimos.
for producto in productos:
    print(producto.get_text().strip())