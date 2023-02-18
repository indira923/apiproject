import random
from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/') 
def index():
    rid = random.randint(1,1001)
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{rid}')
    pokemon = response.json()
    print(pokemon)
    # pokemon = [rid],["official-artwork"],["other"],["front_default"], 
    return render_template ('index.html', pokemon = pokemon)



if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
# def tinkaton :
# print(["sprites"] ["official art"],
# def pokemon ():
#     print([pokemon],["sprites"],["other"],["official artwork"])

