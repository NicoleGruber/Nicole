from Model.backend import BackEnd
from Dao.backend_dao import BackEndDao

class BackEndController:
    dao = BackEndDao()

    def listar_todos(self):
        lista_backends = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            backend = BackEnd()
            backend.id =  s[0]
            backend.nome = s[1]
            
            lista_backends.append(backend)
        return lista_backends

    def buscar_por_id(self, id):
        s = self.dao.buscar_por_id(id)
        backend = BackEnd()
        backend.id =  s[0]
        backend.nome = s[1]
      
        return backend

    def salvar(self, backend:BackEnd):
        
        return self.dao.salvar(backend)

    def alterar(self, backend:BackEnd):
        
        self.dao.alterar(backend)

    def deletar(self, id):
        self.dao.deletar(id)