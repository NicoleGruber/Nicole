import MySQLdb
from Model.sgdb import Sgdb

class SgdbDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()


    def listar_todos(self):
        comando = f"SELECT * FROM FN_SGBD"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM FN_SGBD  WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, sgdb:Sgdb):
        comando = f""" INSERT INTO FN_SGBD
        (
            Nome
            
        )
        VALUES
        (
            '{sgdb.nome}'
            

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, sgdb:Sgdb):
        comando = f""" UPDATE FN_SGBD
        SET
            Nome = '{sgdb.nome}',
           
        WHERE ID = {sgdb.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM FN_SGBD WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()