import MySQLdb
from Model.sgdb import Sgdb

class SgdbDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans02', user='padawans02', passwd='fn2019')
    cursor = conexao.cursor()


    def listar_todos(self):
        comando = f"SELECT * FROM SGDB"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM SGDB  WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, sgdb:Sgdb):
        comando = f""" INSERT INTO SGDB
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
        comando = f""" UPDATE SGDB
        SET
            Nome = '{sgdb.nome}',
           
        WHERE ID = {sgdb.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM SGDB WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()