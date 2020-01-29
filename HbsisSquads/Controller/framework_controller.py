from Model.framework import FrameWork
from Dao.framework_dao import FrameWorkDao
class FrameWorkController:
    dao = FrameWorkDao()
    

    def listar_todos(self):
        lista_frameworks = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            framework = FrameWork()
            framework.id =  p[0]
            framework.nome = p[1]
            
            lista_frameworks.append(framework)
        return lista_frameworks

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        framework = Framework()
        framework.id =  p[0]
        framework.Nome = p[1]
      
        return framework

    def salvar(self, framework:FrameWork):
        
        return self.dao.salvar(framework)

    def alterar(self, framework:FrameWork):
        
        self.dao.alterar(framework)

    def deletar(self, id):
        self.dao.deletar(id)