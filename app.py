from flask import Flask, render_template
import requests


app = Flask(__name__)
api_key = ""

@app.route('/') 
def index():
    pokemon = pokemon
    response = requests.get(f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/shiny/959.png')
    pokemon  = response.json()
    return render_template ('index.html', pokemon = )

print ("https://pokeapi.co/api/v2/{endpoint}/")

def tinkaton :
    "sprites" : "official art",
    