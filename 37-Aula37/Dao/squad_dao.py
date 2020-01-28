import MySQLdb
from Model.squad import Squad

class SquadDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"""SELECT
        FROM Nicole_Squad as s
        JOIN FN_FrameWorkFrontEnd as fm
        on s.FrameWorkFrontEnd_ID = fm.ID
        join FN_LinguagemBackEnd as l
        on s.LinguagemBackEnd_ID = l.ID
        join FN_SGBD as db
        on s.SGBD_ID = db.ID;"""
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"""SELECT s.ID, s.Nome, s.Descricao, s.NumeroPessoas
        ,fm.ID
        ,fm.FrameWorkFrontEnd
        ,l.ID
        ,l.LinguagemBackEnd
        ,db.ID
        ,db.SGBD
        FROM Nicole_Squad as s
        JOIN FN_FrameWorkFrontEnd as fm
        on s.FrameWorkFrontEnd_ID = fm.ID
        join FN_LinguagemBackEnd as l
        on s.LinguagemBackEnd_ID = l.ID
        join FN_SGBD as db
        on s.SGBD_ID = db. ID WHERE s.ID = {id}; """
        
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f"""INSERT INTO Nicole_Squad
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
            '{squad.nome}',
            '{squad.descricao}',
            {squad.numeropessoas},
            {squad.id_framework},
            {squad.id_backend},
            {squad.id_sgdb}

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squad:Squad):
        comando = f"""UPDATE Nicole_Squad 
        SET
            Nome = '{squad.nome}',
            Descricao ='{squad.descricao}',
            NumeroPessoas = {squad.numeropessoas}
            FrameWorkFrontEnd_ID = {squad.id_framework},
            LinguagemBackEnd_ID = {squad.id_backend},
            SGBD_ID = {squad.id_sgdb}

        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM Nicole_Squad WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()