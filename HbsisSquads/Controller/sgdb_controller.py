from Model.sgdb import Sgdb
from Dao.sgdb_dao import SgdbDao

class SgdbController:
    dao = SgdbDao()
    
    def listar_todos(self):
        lista_sgdb = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            sgdb = Sgdb()
            sgdb.id =  s[0]
            sgdb.nome = s[1]
            
            
            lista_sgdb.append(sgdb)
        return lista_sgdb

    def buscar_por_id(self, id):
        s = self.dao.buscar_por_id(id)
        sgdb = Sgdb()
        sgdb.id =  s[0]
        sgdb.nome = s[1]
      
        return sgdb

    def salvar(self, sgdb:Sgdb):
        
        return self.dao.salvar(sgdb)

    def alterar(self, sgdb:Sgdb):
        
        self.dao.alterar(sgdb)

    def deletar(self, id):
        self.dao.deletar(id)