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
    return render_template('listar.html', titulo_app = nome, lista_sq = squads)

@app.route('/cadastrar')
def cadastrar():
    squad = SquadsModel()
    if 'id' in request.args:
        ID = request.args['id']
        squad = squads_controller.buscar_por_id(ID)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad )

@app.route('/excluir')
def excluir():
    ID = int(request.args['id'])
    squads_controller.deletar(ID)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squads = SquadsModel()
    
    squads.ID = int(request.args['id'])
    squads.Nome = request.args['nome']
    squads.Descricao = request.args['descricao']
    squads.NumeroPessoas = int(request.args['numeropessoas'])
    squads.LinguagemBackEnd = request.args['linguagembackend']
    squads.FrameWorkFrontEnd = request.args['frameworkfrontend']

    if squads.ID == '0':
        squads_controller.salvar(squads)
    else:
        squads_controller.alterar(squads)
    return redirect('/listar')
app.run(debug=True)
