import MySQLdb
from Model.framework import FrameWork

class FrameWorkDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans02', user='padawans02', passwd='fn2019')
    cursor = conexao.cursor()


    def listar_todos(self):
        comando = f"SELECT * FROM FrameWork"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM FrameWork  WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, framework:FrameWork):
        comando = f""" INSERT INTO FrameWork
        (
            Nome
            
        )
        VALUES
        (
            '{framework.nome}'
            

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, framework:FrameWork):
        comando = f""" UPDATE FrameWork
        SET
            Nome = '{framework.nome}',
           
        WHERE ID = {framework.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM FrameWork WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()