import requests
import json

url = "https://webfonts.googleapis.com/v1/webfonts"
params = {"key": "AIzaSyDfz0lHOk42n4-7hPBV_j7xj3SrBu9b5A8"}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = json.loads(response.content)
    titulos = []
    for font in data['items']:
        titulos.append(font['family'])
    for titulo in titulos:
        print(titulo)
    print(f"Se han encontrado un total de {len(titulos)} tipos de letra disponibles para su descarga")
else:
    print("Error al hacer la solicitud: ", response.status_code)