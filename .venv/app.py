import requests
import json
from flask import Flask, render_template, abort, redirect, request

app = Flask(__name__)

@app.route('/',methods=["GET","post"])
def inicio():
    return render_template("index.html")

@app.route('/list',methods=["GET","post"])
def list():
    return render_template("list.html")

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