from flask import Flask, render_template, request

app = Flask(__name__)

tasks = [
    {'name': 'Bolo de aniversário', 'price': '5,00'},
    {'name': 'Arroz 500g', 'price': '2,00'},
    {'name': 'Bolacha', 'price': '6,50'}
]

@app.route('/')
def home():
    # templates/home.html
    return render_template('home.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    price = request.form['price']
    task = {'name': name, 'price': price}
    tasks.append(task)
    return render_template('home.html', tasks=tasks)

@app.route('/delete')
def delete():
    return 'não tem nada aqui ainda aaaaa'

@app.route('/bye')
def bye():
    return 'Bye'

app.run(debug=True)