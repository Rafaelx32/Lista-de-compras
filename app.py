#importando as bibliotecas
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

tasks = []
#criando rota do HTML
@app.route('/')
def home():
    # templates/home.html
    return render_template('home.html', tasks=tasks)
#Rota de criação de nome e preço dos itens 
@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    price = request.form['price']
    task = {'name': name, 'price': price}
    tasks.append(task)
    return render_template('home.html', tasks=tasks)
# Rota de delatar itens
@app.route('/deletar/<>')
def deletar():
    try:

        return 'nada por enquanto'
    except: 


@app.route('/bye')
def bye():
    return 'Bye'

app.run(debug=True)