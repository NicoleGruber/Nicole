from flask import Flask, render_template, request, redirect

import sys
sys.path.append(r'C:\Users\Nicole\Desktop\Nicole')
from Controller.squad_controller import SquadController
from Controller.backend_controller import BackEndController
from Controller.framework_controller import FrameWorkController
from Controller.sgdb_controller import SgdbController
from Model.squad import Squad
from Model.framework import FrameWork
from Model.backend import BackEnd
from Model.sgdb import Sgdb
from Dao.framework_dao import FrameWorkDao


app = Flask(__name__)

#---- CONTROLLERS
squad_controller = SquadController()
framework_controller = FrameWorkController()
backend_controller = BackEndController()
sgdb_controller = SgdbController()

nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

#---------- CRUD SQUAD ----------

@app.route('/listar_squad')
def listar():
    squad = squad_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista_squads = squad)

@app.route('/cadastrar_squad')
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


@app.route('/excluir_squad')
def excluir():
    id = int(request.args['id'])
    squad_controller.deletar(id)
    
    return redirect('/listar')

@app.route('/salvar_squad')
def salvar():
    squad = Squad()
    squad.id = int(request.args['id'])
    squad.nome = request.args['nome']
    squad.descricao = request.args['descricao']
    squad.numeropessoas = request.args['numeropessoas']
    squad.id_framework = int(request.args['framework'])
    squad.id_backend = int(request.args['backend'])
    squad.id_sgdb = int(request.args['sgdb'])

    if squad.id == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
    return redirect('/listar')

#---------- CRUD FRAMEWORK ----------

@app.route('/listar_framework')
def listar_framework():
    framework = framework_controller.listar_todos()
    return render_template('listar_framework.html', titulo_app = nome, lista_frameworks = framework)

@app.route('/excluir_framework')
def excluir_framework():
    id = int(request.args['id'])
    framework_controller.deletar(id)
    
    return redirect('/listar_framework')

@app.route('/salvar_framework')
def salvar_framework():
    framework = FrameWork()
    framework.id = int(request.args['id'])
    framework.nome = request.args['nome']

    if framework.id == 0:
        framework_controller.salvar(framework)
    else:
        framework_controller.alterar(framework)
    return redirect('/listar_framework.html')

@app.route('/cadastrar_framework')
def cadastrar_framework():
    framework = FrameWork()
    if 'id' in request.args:
        id = request.args['id']
        framework = framework_controller.buscar_por_id(id)
    return render_template('cadastrarframework.html', titulo_app = nome,framework = framework)

#---------- CRUD BACKEND ----------

@app.route('/excluir_backend')
def excluir_backend():
    id = int(request.args['id'])
    framework_controller.deletar(id)
    
    return redirect('/listar_backend')

@app.route('/salvar_backend')
def backend_nome():
    backend = BackEnd()
    if backend.id == 0:
        backend_controller.salvar(backend)
    else:
        backend_controller.alterar(backend)
    return redirect('/listar_backend')

@app.route('/listar_backend')
def listar_backend():
    backend = backend_controller.listar_todos()
    return render_template('listar_backend.html', titulo_app = nome, lista_backends = backend)

@app.route('/cadastrar_backend')
def cadastrar_backend():
    backend = BackEnd()
    if 'id' in request.args:
        id = request.args['id']
        backend = backend_controller.buscar_por_id(id)
    return render_template('cadastrarbackend.html', titulo_app = nome,backend = backend)

#---------- CRUD SGDB ----------

@app.route('/excluir_sgdb')
def excluir_sgdb():
    id = int(request.args['id'])
    sgdb_controller.deletar(id)
    
    return redirect('/listar_sgdb')


@app.route('/salvar_sgdb')
def sgdb_nome():
    sgdb = Sgdb()
    if sgdb.id == 0:
        sgdb_controller.salvar(sgdb)
    else:
        sgdb_controller.alterar(sgdb)
    return redirect('/listar_sgdb')


@app.route('/listar_sgdb')
def listar_sgdb():
    sgdb = sgdb_controller.listar_todos()
    return render_template('listar_sgdb.html', titulo_app = nome, lista_sgdb = sgdb)

@app.route('/cadastrar_sgdb')
def cadastrar_sgdb():
    sgdb = Sgdb()
    if 'id' in request.args:
        id = request.args['id']
        sgdb = sgdb_controller.buscar_por_id(id)
    return render_template('cadastrarsgdb.html', titulo_app = nome,sgdb = sgdb)

app.run(debug=True)

