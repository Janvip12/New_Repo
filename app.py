from flask import Flask, request
import json
import requests

app = Flask(__name__)
app.debug = True

# @app.route('/')
# def studentNumber():
#     dictionary =  {"Student Number" : "200511517"}
#     return json.dumps(dictionary)

@app.route('/webhook',methods=['POST'])
def index():
    #Get the formula1-gossip entity from the dialogflow fullfilment request.
    body = request.json
    alcohol_name = body['queryResult']['parameters']['Alcohol-Name']

    #Connect to the API and get the JSON file.
    api_url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + alcohol_name + ''
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url, headers=headers)
    r = response.json()

    #Extract most famous alcohol name
    drink_name = str(r["drinks"][0]["strDrink"])

    #Build the Dialogflow reply.
    reply = '{"fulfillmentMessages": [ {"text": {"text": ["The most famous drink is ' + drink_name + '"] } } ]}'
    return reply
