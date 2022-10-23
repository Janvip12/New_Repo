from flask import Flask, request
import json
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def studentNumber():
    dictionary =  {"Student Number" : "PUT YOUR STUDENT NUMBER HERE"}
    return json.dumps(dictionary)