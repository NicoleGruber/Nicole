from flask import Flask, render_template, request, redirect
import sys
sys.path.append(r'C:\Users\900156\Desktop\Nicole\37-Aula37')
from Controller.squad_controller import SquadController
from Controller.backend_controller import BackEndController
from Controller.framework_controller import FrameWorkController
from Controller.sgdb_controller import SgdbController
from Model.squad import Squad
from Model.framework import FrameWork
from Model.backend import BackEnd
from Model.sgdb import Sgdb
app = Flask(__name__)
squad_controller = SquadController()
framework_controller = FrameWorkController()
backend_controller = BackEndController()
sgdb_controller = SgdbController()

nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squad = squad_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista_squads = squad)

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()
    framework = FrameWork()
    backend = BackEnd()
    sgdb = Sgdb()
    
    
    squad.FrameWork = FrameWork()
    squad.BackEnd = BackEnd()
    squad.sgdb = Sgdb()

    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad, framework = framework, backend = backend, sgdb = sgdb )


@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    framework_controller.deletar(id)
    backend_controller.deletar(id)
    sgdb_controller.deletar(id)
    squad_controller.deletar(id)
    
    return redirect('/listar')

@app.route('/squad.salvar')
def salvar():
    squad = Squad()
    squad.id = int(request.args['id'])
    squad.nome = request.args['Nome']
    squad.descricao = request.args['Descricao']
    squad.numeropessoas = request.args['NumeroPessoas']
    squad.id_framework = int(request.args['FrameWork'])
    squad.id_backend = int(request.args['LinguagemBackEnd'])
    squad.id_sgdb = int(request.args['Sgdb'])

    if squad.id == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
        print()
    return redirect('/listar')

@app.route('/framework.salvar')
def framework_nome():
    framework = FrameWork()
    if framework.id == '0':
        framework_controller.salvar(framework)
    else:
        framework_controller.alterar(framework)
    return redirect('/listar')

@app.route('/backend.salvar')
def backend_nome():
    backend = BackEnd()
    if backend.id == '0':
        backend_controller.salvar(backend)
    else:
        backend_controller.alterar(backend)
    return redirect('/listar')

@app.route('/sgdb.salvar')
def sgbd_nome():
    sgdb = SGBD()
    if sgdb.id == '0':
        sgdb_controller.salvar(sgdb)
    else:
        sgdb_controller.alterar(sgdb)
    return redirect('/listar')

app.run(debug=True)

