# Devuelve los nombres de las fuentes disponibles en el repositorio

import requests
import json

import requests

url = "https://webfonts.googleapis.com/v1/webfonts"
params = {"key": "AIzaSyDfz0lHOk42n4-7hPBV_j7xj3SrBu9b5A8"}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print("Error al hacer la solicitud: ", response.status_code)
