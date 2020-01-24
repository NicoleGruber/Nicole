import MySQLdb
from Model.squad import Squad

class SquadDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM Nicole_Squad"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM Nicole_Squad  WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f""" INSERT INTO Nicole_Squad
        (
            Nome,
            Descricao,
            NumeroPessoas,
            FrameWorkFrontEnd_ID,
            LinguagemBackEnd_ID,
            SGBD_ID
        )
        VALUES
        (
            '{squad.Nome}',
            '{squad.Descricao}',
            {squad.NumeroPessoas},
            {squad.FrameWorkFrontEnd_ID.ID},
            {squad.LinguagemBackEnd_ID.ID},
            {squad.SGBD_ID.ID}

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squad:Squad):
        comando = f""" UPDATE Nicole_Squad
        SET
            Nome = '{squad.Nome}',
            Descricao ='{squad.Descricao}',
            NumeroPessoas = {squad.NumeroPessoas}
            FrameWorkFrontEnd_ID = {squad.FrameWorkFrontEnd_ID.ID},
            LinguagemBackEnd_ID = {squad.LinguagemBackEnd_ID.ID},
            SGBD_ID = {squad.SGBD_ID.ID}

        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM Nicole_Squad WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()