#importando as bibliotecas
from flask import Flask, render_template, request
import pandas as pd
import csv
from uuid import uuid4

app = Flask(__name__)
#criando rota do HTML
@app.route('/')
def home():

    #Abrindo os dados que estão salvos no csv no HTML
    with open('compras.csv', 'rt') as fille_in:
        compras = csv.DictReader(fille_in)
        return render_template('index.html', compras=compras)# templates/index.html

#criando a rota de HTML que será responsável por receber os itens que o cliente colocará
@app.route('/create')
def create():
    return render_template('create.html')


#Rota de criação de nome e preço dos itens 
@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    preco = request.form['preco']
    entrada_dados = []
    entrada_dados.append([uuid4(), nome, preco])


    with open('compras.csv', 'a') as file_out:
        escritor = csv.writer(file_out)
        escritor.writerows(entrada_dados)


    with open('compras.csv','rt') as fille_in:
        compras = csv.DictReader(fille_in)
        return render_template('index.html', compras=compras)


# Rota de delatar itens
@app.route('/deletar/<id>')
def deletar(id):
    data = pd.read_csv('compras.csv')
    data = data.set_index("Id")
    data.drop(id, axis= "index", inplace=True)
    data.to_csv('compras.csv')


    with open('compras.csv', 'rt') as fille_in:
        compras = csv.DictReader(fille_in)
        return render_template('index.html', compras=compras)


@app.route('/atualizar/<id>/<nome>/<preco>')
def atualizar(id, nome, preco):
    lista = [id,nome,preco]
    return render_template('atualizar.html', lista=lista)


@app.route('/guardar', methods=['POST'])
def guardar():
    id = request.form['id']
    nome = request.form['nome']
    preco = request.form['preco']
    data = pd.read_csv("compras.csv")
    novo_df = pd.DataFrame({'Id': [id], 'nome': [nome], 'preco': [preco] })
    data = data.set_index("Id")
    novo_df = novo_df.set_index("Id")
    data.update(novo_df)
    data.to_csv('compras.csv')


    with open('compras.csv', 'rt') as fille_in:
        compras = csv.DictReader(fille_in)
        return render_template('index.html', compras=compras)
        
            
app.run(debug=True)


# CLIENTE -- SERVIDOR
# Navegador -- AWS (Flask)

# Client -> REQUEST (Mensagem HTTP) -> Server 
# Server -> RESPONSE (Mensagem HTTP) -> CLIENTE

# HTTP (HyperText Transfer Protocol)
# HTML (HyperText Markup Language)

# Mensagem HTTP: 
# Header
# Body
# METHOD (GET, POST), Métodos suportados pelos navegadores.
# GET -> DADOS PELA URL
# POST -> OCULTO OS DADOS (NÃO MOSTRA NA URL)

# METHOD (API = GET, POST, PUT, DELETE, PATCH, OPTIONS)

# API REST
# POST   (C)REATE
# GET    (R)EAD
# PUT    (U)PDATE
# PATCH  (U)PDATE PARCIAL
# DELETE (D)ELETE