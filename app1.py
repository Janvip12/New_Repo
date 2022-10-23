from flask import Flask, request
import json
import requests

app1 = Flask(__name__)
app1.debug = True

@app1.route('/')
def studentNumber():
    dictionary =  {"Student Number" : "PUT YOUR STUDENT NUMBER HERE"}
    return json.dumps(dictionary)
