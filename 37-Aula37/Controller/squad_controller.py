from Dao.squad_dao import SquadDao
from Model.squad import Squad


class SquadController:
    dao = SquadDao()
    

    def listar_todos(self):
        lista_squads = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            squad = Squad()
            squad.id =  p[0]
            squad.Nome = p[1]
            squad.Descricao = p[2]
            squad.NumeroPessoas = p[3]
            
            squad.BackEnd = p[4]
            squad.FrameWork = p[5]
            
            lista_squads.append(squad)
        return lista_squads

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id =  p[0]
        squad.Nome = p[1]
        squad.Descricao = p[2]
        squad.NumeroPessoas = p[3]
        
        squad.BackEnd = p[4]
        squad.FrameWork = p[5]
        return squad

    def salvar(self, squad:Squad):
        
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)