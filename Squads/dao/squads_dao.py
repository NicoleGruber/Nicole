import sys
import MySQLdb
sys.path.append(r'C:\Users\900156\Desktop\Nicole\Squads')
from model.squads_model import SquadsModel

class SquadsDao():
    conexao= MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor

    def listar_todos(self):
        comando = f"SELECT * FROM Nicole_Squad"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self):
        comando = f"SELECT * FROM Nicole_Squad WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone
        return resultado

    def salvar(self):
        comando = f"""INSERT INTO Nicole_Squads 
        (Nome,
        Descricao,
        NumeroPessoas,
        LinguagemBackEnd,
        FrameWorkFrontEnd)
        VALUES 
        ({squads.nome},
        {squads.descricao},
        {squads.numeropessoas},
        {squasd.linguagembackend},
        {squads.frameworkfrontend}
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self):
        comando = f"""UPDATE Nicole_Squad SET
        Nome = '{squads.nome}'
        Descricao = '{squads.descricao}'
        NumeroPessoas = '{squads.numeropessoas}'
        LinguagemBackEnd = '{squads.linguagembackend}'
        FrameWorkFrontEnd = '{squads.frameworkfrontend}'
        WHERE ID = {squads.id}"""
        self.cursor.execute(comando)
        self.cursor.commit()
    
    def deletar(self):
        comando = f"DELETE FROM Nicole_Squad WHERE ID = {id}"
        self.cursor.execute(comando)
        self.cursor.commit
    
