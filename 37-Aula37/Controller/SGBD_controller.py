from Dao.SGBD_dao import SGBDDao
from Model.SGBD import SGBD


class SGBDController:
    dao = SGBDDao()
    
    def listar_todos(self):
        lista_sgbd = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            sgbd = SGBD()
            sgbd.id =  p[0]
            sgbd.Nome = p[1]
            
            
            lista_sgbd.append(sgbd)
        return lista_sgbd

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        sgbd = SGBD()
        sgbd.id =  p[0]
        sgbd.Nome = p[1]
      
        return sgbd

    def salvar(self, sgbd:SGBD):
        
        return self.dao.salvar(sgbd)

    def alterar(self, sgbd:SGBD):
        
        self.dao.alterar(sgbd)

    def deletar(self, id):
        self.dao.deletar(id)