import requests
import json
from flask import Flask, render_template, abort, redirect, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, world!</h1>'

if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)