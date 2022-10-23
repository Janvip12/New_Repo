from flask import Flask, request
import json
import requests

app1 = Flask(__name__)
app1.debug = True

@app1.route('/')
def studentNumber():
    dictionary =  {"Student Number" : "12345"}
    return json.dumps(dictionary)
