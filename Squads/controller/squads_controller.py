import sys
sys.path.append(r'C:\Users\900156\Desktop\Nicole\Squads')
from dao.squads_dao import SquadsDao
from model.squads_model import SquadsModel

class SquadsController():
    dao = SquadsDao()
    def listar_todos(self):
        lista_sq = []
        tupla = self.dao.listar_todos()
        for sq in tupla:
            squads = SquadsModel()
            squads.ID = sq[0]
            squads.Nome = sq[1]
            squads.Descricao = sq[2]
            squads.NumeroPessoas = sq[3]
            squads.LinguagemBackEnd = sq[4]
            squads.FrameWorkFrontEnd = sq[5]
            lista_sq.append(squads)
        return lista_sq
    
    def buscar_por_id(self,id):
        s = self.dao.buscar_por_id(id)
        squads = SquadsModel()
        squads.ID = s[0]
        squads.Nome = s[1]
        squads.Descricao = s[2]
        squads.NumeroPessoas = s[3]
        squads.LinguagemBackEnd = s[4]
        squads.FrameworkFrontEnd = s[5]
        return squads

    def salvar(self,squads : SquadsModel):
        return self.dao.salvar(squads)

    def alterar(self, squads : SquadsModel):
        self.dao.alterar(squads)

    def deletar(self,ID):
        self.dao.deletar(ID)
