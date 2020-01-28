from Dao.sgdb_dao import SgdbDao 
from Dao.framework_dao import FrameWorkDao
from Dao.backend_dao import BackEndDao
from Dao.squad_dao import SquadDao

from Model.backend import BackEnd
from Model.framework import FrameWork
from Model.sgdb import Sgdb
from Model.squad import Squad

class SquadController:
    dao = SquadDao()

    def listar_todos(self):
        lista_squads = []
        lista_tuplas = self.dao.listar_todos()
        print(lista_tuplas)
        for p in lista_tuplas:
            squad = Squad()
            squad.id =  p[0]
            squad.nome = p[1]
            squad.descricao = p[2]
            squad.numeropessoas = p[3]
            squad.backend.nome = p[8]
            if squad.backend.nome == 'None':
                squad.backend.nome = 'Não Definido'
            else:
                pass
            squad.framework.nome = p[10]
            if squad.framework.nome == 'None':
                squad.framework.nome = 'Não Definido'
            else:
                pass
            squad.sgdb.nome = [12]
            if squad.sgdb.nome == 'None':
                squad.sgdb.nome = 'Não Definido'
            else:
                pass
        
            lista_squads.append(squad)
        return lista_squads

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id =  p[0]
        squad.nome = p[1]
        squad.descricao = p[2]
        squad.numeropessoas = p[3]
        
        squad.FrameWorkFrontEnd_ID = p[4]
        squad.LinguagemBackEnd_ID = p[5]
        squad.SGBD_ID
        return squad

    def salvar(self, squad:Squad):
        
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)