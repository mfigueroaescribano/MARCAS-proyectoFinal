import requests
import json
from flask import *

app = Flask(__name__)
url = "https://webfonts.googleapis.com/v1/webfonts"
key = {"key": "AIzaSyDfz0lHOk42n4-7hPBV_j7xj3SrBu9b5A8"}
key2 = "AIzaSyDfz0lHOk42n4-7hPBV_j7xj3SrBu9b5A8"


@app.route('/',methods=["GET","post"])
def inicio():
    return render_template("index.html")

@app.route('/list',methods=["GET","post"])
def list():
    
    response = requests.get(url, params=key)
    
    if response.status_code == 200:
        font_data = response.json()
        font_names = [font['family'] for font in font_data['items']]
        return render_template("list.html", font_names=font_names)
    else:
        return "Error al hacer la solicitud: {}".format(response.status_code)

@app.route('/detalles',methods=["GET","POST"])
def search_fonts():
    if request.method == "POST":
        fuente = request.form.get('nombre')

        url = f'https://webfonts.googleapis.com/v1/webfonts?family={fuente}&key={key2}'

        response = requests.get(url)

        if response.status_code == 200:
            json = response.json()
            nombre = json['items'][0]['family']
            categoria = json['items'][0]['category']
            version = json['items'][0]['version']
            modif = json['items'][0]['lastModified']
            links = json['items'][0]['files']

            return render_template("detalles.html", nombre=nombre, categoria=categoria, version=version, modif=modif, links=links)
        else:
            error = f'No se ha encontrado ninguna fuente 😥'
            return render_template("detalles.html", error=error)
    else:
        return render_template("detalles.html")

@app.route('/detalles/<fuente>', methods=["GET"])
def detalles_fuente(fuente):
    url = f'https://webfonts.googleapis.com/v1/webfonts?family={fuente}&key={key2}'
    response = requests.get(url)

    if response.status_code == 200:
        json = response.json()
        nombre = json['items'][0]['family']
        categoria = json['items'][0]['category']
        version = json['items'][0]['version']
        modif = json['items'][0]['lastModified']
        links = json['items'][0]['files']

        return render_template("detalles.html", nombre=nombre, categoria=categoria, version=version, modif=modif, links=links)
    else:
        error = f'No se ha encontrado ninguna fuente 😥'
        return render_template("detalles.html", error=error)

@app.route('/error')
def error():
    return abort(404)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)