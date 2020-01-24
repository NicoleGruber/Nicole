import MySQLdb
from Model.BackEnd import BackEnd

class BackEndDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()


    def listar_todos(self):
        comando = f"SELECT * FROM FN_LinguagemBackEnd"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM FN_LinguagemBackEnd  WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, backend:BackEnd):
        comando = f""" INSERT INTO FN_LinguagemBackEnd
        (
            Nome
            
        )
        VALUES
        (
            '{backend.Nome}'
            

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, backend:BackEnd):
        comando = f""" UPDATE FN_LinguagemBackEnd
        SET
            Nome = '{backend.Nome}',
           
        WHERE ID = {backend.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM FN_LinguagemBackEnd WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()