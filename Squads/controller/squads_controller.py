import sys
sys.path.append(r'C:\Users\900156\Desktop\Nicole\Squads')
from dao.squads_dao import SquadsDao
from model.squads_model import SquadsModel

class SquadsController():
    dao = SquadsDao()
    def listar_todos(self):
        lista = []
        tupla = self.dao.listar_todos()
        for s in tupla:
            squads = SquadsModel()
            squads.id = s[0]
            squads.nome = s[1]
            squads.descricao = s[2]
            squads.numeropessoas = s[3]
            squads.linguagembackend = s[4]
            squads.frameworkfrontend = s[5]
            lista.append(squads)
        return lista
    
    def buscar_por_id(self,id):
        s = self.dao.buscar_por_id(id)
        squads = SquadsModel
        squads.id = s[0]
        squads.nome = s[1]
        squads.descricao = s[2]
        squads.numeropessoas = s[3]
        squads.linguagembackend = s[4]
        squads.frameworkfrontend = s[5]
        return squads

    def salvar(self,squads = SquadsModel):
        squads = salvar.squads
        return self.dao.salvar(squads)

    def alterar(self,squads = SquadsModel):
        self.alterar(squads)
        self.dao.alterar(squads)

    def deletar(self,id):
        self.dao.deletar(id)
