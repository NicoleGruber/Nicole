import MySQLdb
import sys
sys.path.append(r'C:\Users\900156\Desktop\Nicole\Squads')
from model.squads_model import SquadsModel

class SquadsDao():
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM Nicole_Squad"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self,id):
        comando = f"SELECT * FROM Nicole_Squad WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squads : SquadsModel):
        comando = f"""INSERT INTO Nicole_Squad 
        (
            Nome,
            Descricao,
            NumeroPessoas,
            LinguagemBackEnd,
            FrameWorkFrontEnd
        )
        VALUES 
        (
            '{squads.Nome}',
            '{squads.Descricao}',
            {squads.NumeroPessoas},
            '{squads.LinguagemBackEnd}',
            '{squads.FrameWorkFrontEnd}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self , squads : SquadsModel):
        comando = f"""UPDATE Nicole_Squad SET
            Nome = '{squads.Nome}',
            Descricao = '{squads.Descricao}',
            NumeroPessoas = {squads.NumeroPessoas},
            LinguagemBackEnd = '{squads.LinguagemBackEnd}',
            FrameWorkFrontEnd = '{squads.FrameWorkFrontEnd}'
            WHERE ID = {squads.ID}"""
        self.cursor.execute(comando)
        self.conexao.commit()
    
    def deletar(self,ID):
        comando = f"DELETE FROM Nicole_Squad WHERE ID = {ID}"
        self.cursor.execute(comando)
        self.conexao.commit()
    
