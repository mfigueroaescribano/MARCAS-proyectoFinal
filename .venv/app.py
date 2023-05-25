import requests
import json
from flask import Flask, render_template, abort, redirect, request

app = Flask(__name__)

@app.route('/',methods=["GET","post"])
def inicio():
    return render_template("base.html")

@app.route('/error')
def error():
    return abort(404)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)