import MySQLdb
from Model.Framework import FrameWork

class FrameWorkDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()


    def listar_todos(self):
        comando = f"SELECT * FROM FN_FrameWorkFrontEnd"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM FN_FrameWorkFrontEnd  WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, framework:FrameWork):
        comando = f""" INSERT INTO FN_FrameWorkFrontEnd
        (
            Nome
            
        )
        VALUES
        (
            '{framework.Nome}'
            

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, framework:FrameWork):
        comando = f""" UPDATE FN_FrameWorkFrontEnd
        SET
            Nome = '{framework.Nome}',
           
        WHERE ID = {framework.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM FN_FrameWorkFrontEnd WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()