import MySQLdb
from Model.squad import Squad

class SquadDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans02', user='padawans02', passwd='fn2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"""
        SELECT * FROM Squad as s
        JOIN FrameWork as fm
        on s.Frame_id = fm.id
        join BackEnd as l
        on s.Back_id = l.id
        join SGDB as db
        on s.Sgdb_id = db.id"""
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"""
        SELECT * FROM Squad as s
        JOIN FrameWork as fm
        on s.Frame_id = fm.id
        join BackEnd as l
        on s.Back_id = l.id
        join SGDB as db
        on s.Sgdb_id = db.id WHERE s.id = {id} """
        
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f"""INSERT INTO Squad
        (
            Nome,
            Descricao,
            NumeroPessoas,
            Frame_id,
            Back_id,
            Sgdb_id            
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
            NumeroPessoas = {squad.numeropessoas},
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