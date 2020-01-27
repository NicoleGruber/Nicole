from flask import Flask, render_template, request, redirect
import sys
sys.path.append('/Felipe/15-01-19/AulasPython/37-Aula37')
from Controller.squad_controller import SquadController
from Controller.BackEnd_controller import BackEndController
from Controller.Framework_controller import FrameWorkController
from Controller.SGBD_controller import SGBDController
from Model.squad import Squad
from Model.Framework import FrameWork
from Model.BackEnd import BackEnd
from Model.SGBD import SGBD
app = Flask(__name__)
squad_controller = SquadController()
framework_controller = FrameWorkController()
backend_controller = BackEndController()
sgbd_controller = SGBDController()

nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squad = squad_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = squad)

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()
    framework = FrameWork()
    backend = BackEnd()
    sgbd = SGBD()
    
    
    squad.FrameWork = FrameWork()
    squad.BackEnd = BackEnd()
    squad.SGBD = SGBD()

    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad, framework = framework )


@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    framework_controller.deletar(id)
    backend_controller.deletar(id)
    sgbd_controller.deletar(id)
    squad_controller.deletar(id)
    
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squad = Squad()
    squad.id = request.args['id']
    squad.Nome = request.args['Nome']
    squad.Descricao = request.args['Descricao']
    squad.NumeroPessoas = request.args['NumeroPessoas']

    framework = FrameWork()
    framework.id = request.args['id']
    framework.Nome = request.args['Nome']

    backend = BackEnd()
    backend.id = request.args['id']
    backend.Nome = request.args['Nome']

    sgbd = SGBD()
    sgbd.id = request.args['id']
    sgbd.Nome = request.args['Nome']    

    squad.FrameWork = framework
    squad.BackEnd = backend 
    squad.SGBD = sgbd


    
    #if squad.id == 0:
    squad_controller.salvar(squad)
    # else:
    #     squad_controller.alterar(squad)
    return redirect('/listar')

@app.route('/salvar')
def framework_nome():
    framework = FrameWork()
    if framework.id == '0':
        framework_controller.salvar(framework)
    else:
        framework_controller.alterar(framework)
    return redirect('/listar')

@app.route('/salvar')
def backend_nome():
    backend = BackEnd()
    if backend.id == '0':
        backend_controller.salvar(backend)
    else:
        backend_controller.alterar(backend)
    return redirect('/listar')

@app.route('/salvar')
def sgbd_nome():
    sgbd = SGBD()
    if sgbd.id == '0':
        sgbd_controller.salvar(sgbd)
    else:
        sgbd_controller.alterar(sgbd)
    return redirect('/listar')

app.run(debug=True)