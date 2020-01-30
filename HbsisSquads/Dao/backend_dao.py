import MySQLdb
from Model.backend import BackEnd

class BackEndDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans02', user='padawans02', passwd='fn2019')
    cursor = conexao.cursor()


    def listar_todos(self):
        comando = f"SELECT * FROM BackEnd"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM BackEnd  WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, backend:BackEnd):
        comando = f""" INSERT INTO BackEnd
        (
            Nome
        )
        VALUES
        (
            '{backend.nome}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, backend:BackEnd):
        comando = f""" UPDATE BackEnd
        SET
            Nome = '{backend.nome}'
           
        WHERE ID = {backend.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM BackEnd WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()