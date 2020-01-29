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
        for s in lista_tuplas:
            squad = Squad()
            squad.id =  s[0]
            squad.nome = s[1]
            squad.descricao = s[2]
            squad.numeropessoas = s[3]
            squad.backend.nome = s[8]
            if squad.backend.nome == 'None':
                squad.backend.nome = 'Não Definido'
            else:
                pass
            squad.framework.nome = s[10]
            if squad.framework.nome == 'None':
                squad.framework.nome = 'Não Definido'
            else:
                pass
            squad.sgdb.nome = s[12]
            if squad.sgdb.nome == 'None':
                squad.sgdb.nome = 'Não Definido'
            else:
                pass
        
            lista_squads.append(squad)
        return lista_squads

    def buscar_por_id(self, id):
        s = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id =  s[0]
        squad.nome = s[1]
        squad.descricao = s[2]
        squad.numeropessoas = s[3]
        squad.framework.id = s[4]
        squad.backend.id = s[5]
        squad.sgdb.id = s[6]

        return squad

    def salvar(self, squad:Squad):
        
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)