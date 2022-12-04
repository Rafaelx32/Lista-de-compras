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


#Criação da rota salvar, para salvar o nome e preço do produto
@app.route('/salvar', methods=['POST'])
#Criação da função salvar
def salvar():
    nome = request.form['nome']
    preco = request.form['preco']
    entrada_dados = []
    entrada_dados.append([uuid4(), nome, preco])

    #Ao final os dados inseridos na lista 'entrada_dados' vão ser salvos em compras.csv
    with open('compras.csv', 'a') as file_out:
        escritor = csv.writer(file_out)
        escritor.writerows(entrada_dados)

    # o arquivo compras.csv será aberto de uma forma que apenas poderá ser lido no index HTML
    with open('compras.csv','rt') as fille_in:
        compras = csv.DictReader(fille_in)
        return render_template('index.html', compras=compras)


# Criação da rota deletar produtos, que será responsável por deletar os itens de acordo com o ID
@app.route('/deletar/<id>')
#criação da função deletar
def deletar(id):
    #Abre o arquivo pelo pandas
    data = pd.read_csv('compras.csv')


    #defini o index na coluna ID
    data = data.set_index("Id")

    #remove toda row que tiver a mesma váriavel 'id' na coluna Index
    data.drop(id, axis= "index", inplace=True)

    #salva o novo data
    data.to_csv('compras.csv')

    #lê o arquivo e envia a variável para o 'index.html'
    with open('compras.csv', 'rt') as fille_in:
        compras = csv.DictReader(fille_in)
        return render_template('index.html', compras=compras)

#Criação da rota Atualizar
@app.route('/atualizar/<id>/<nome>/<preco>')
#criação da função atualizar
def atualizar(id, nome, preco):
    #Criação de uma nova lista para receber os valores de id, nome e preco
    lista = [id,nome,preco]
    return render_template('atualizar.html', lista=lista)#retorna as váriaveis para a rota 'atualizar.html'

#criação da rota guardar 
@app.route('/guardar', methods=['POST'])
#criação da função guardar
def guardar():

    #as informações inseridas no formúlario do 'atualizar.html' serão mandadas para cá
    id = request.form['id']
    nome = request.form['nome']
    preco = request.form['preco']

    #Abre o arquivo pelo pandas 
    data = pd.read_csv("compras.csv")
    #será criado um novo data frame a partir das váriaveis inseridas a cima
    novo_df = pd.DataFrame({'Id': [id], 'nome': [nome], 'preco': [preco] })

    #defini o index na coluna Id
    data = data.set_index("Id")
    novo_df = novo_df.set_index("Id")

    #atualiza os dados do antigo data com o novo
    data.update(novo_df)

    #salva o arquivo em compras.csv
    data.to_csv('compras.csv')

    #redireciona para o 'index.html'
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