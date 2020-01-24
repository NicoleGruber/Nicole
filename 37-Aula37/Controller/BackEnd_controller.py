from Dao.BackEnd_dao import BackEndDao
from Model.BackEnd import BackEnd

class BackEndController:
    dao = BackEndDao()

    def listar_todos(self):
        lista_backends = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            backend = BackEnd()
            backend.id =  p[0]
            backend.Nome = p[1]
            
            lista_backends.append(backend)
        return lista_backends

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        backend = BackEnd()
        backend.id =  p[0]
        backend.Nome = p[1]
      
        return backend

    def salvar(self, backend:BackEnd):
        
        return self.dao.salvar(backend)

    def alterar(self, backend:BackEnd):
        
        self.dao.alterar(backend)

    def deletar(self, id):
        self.dao.deletar(id)