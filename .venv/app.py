import requests
import json
from flask import *

app = Flask(__name__)
url = "https://webfonts.googleapis.com/v1/webfonts"
key = {"key": "AIzaSyDfz0lHOk42n4-7hPBV_j7xj3SrBu9b5A8"}


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

@app.route('/detalles',methods=["GET","post"])
def detalles():
    return render_template("detalles.html")

@app.route('/filtrar',methods=["GET","post"])
def filtrar():
    return render_template("filtrar.html")

@app.route('/error')
def error():
    return abort(404)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)