#importando as bibliotecas
from flask import Flask, render_template, request
import pandas as pd
import csv
from uuid import uuid4

app = Flask(__name__)

tasks = []
#criando rota do HTML
@app.route('/')
def home():
    with open('compras.csv', 'rt') as fille_in:
        tasks== csv.DictReader(fille_in)
    # templates/home.html
    return render_template('home.html', tasks=tasks)
#Rota de criação de nome e preço dos itens 
@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    price = request.form['price']
    task = [uuid4(), name, price]
    tasks.append(task)
    return render_template('home.html', tasks=tasks)


# Rota de delatar itens
@app.route('/deletar/<id>')
def deletar():
    try:

        return 'nada por enquanto'
    except: 




app.run(debug=True)