from flask import Flask,render_template,request,redirect
import sys
sys.path.append(r'C:\Users\900156\Desktop\Nicole\Squads')
from controller.squads_controller import SquadsController
from model.squads_model import SquadsModel

app = Flask(__name__)
squads_controller = SquadsController()
nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squads = squads_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = pessoas)

@app.route('/cadastrar')
def cadastrar():
    squads = SquadsModel()
    if 'id' in request.args:
        id = request.args['id']
        squad = squads_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squad = Squad )

@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    id_end = request.args['id_end']
    squads_controller.deletar(id)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squads = Squads()
    squads.id = request.args['id']
    squads.nome = request.args['nome']
    squads.descricao = request.args['descricao']
    squads.numeropessoas = request.args['numeropessoas'],
    squads.linguagembackend = request.args['linguagembackend']
    squads.frameworkfrontend = request.args['frameworkfrontend']

    if pessoa.id == 0:
        pessoa_controller.salvar(pessoa)
    else:
        pessoa_controller.alterar(pessoa)
    return redirect('/listar')

app.run(debug=True)