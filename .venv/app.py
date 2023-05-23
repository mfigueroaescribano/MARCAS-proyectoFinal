import requests
import json
from flask import Flask, render_template, abort, redirect, request

app = Flask(__name__)

app.run("0.0.0.0", 5000, debug=True)