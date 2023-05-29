import requests
import json


url = "https://webfonts.googleapis.com/v1/webfonts"
params = {"key": "AIzaSyDfz0lHOk42n4-7hPBV_j7xj3SrBu9b5A8", "sort": "alpha"}

tipo = input("Introduzca el tipo de letra a buscar: ")

response = requests.get(url, params=params)

if response.status_code == 200:
    data = json.loads(response.content)
    for font in data['items']:
        if font['family'] == tipo:
            print("Información para la fuente", tipo)
            print("================================")
            print("Categorías:", font['category'])
            print("Subsets:", font['subsets'])
            print("Variantes:", font['variants'])
            print("Enlace de descarga:", font['files'])
            break
else:
    print("Error al hacer la solicitud: ", response.status_code)