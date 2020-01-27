from Model.Framework import FrameWork
from Model.BackEnd import BackEnd 
from Model.SGBD import SGBD
class Squad:
    def __init__(self):
        self.ID = 0
        self.Nome = ''
        self.Descricao= ''
        self.NumeroPessoas = 0
        self.FrameWorkFrontEnd_ID = 0
        self.FrameWork = FrameWork()
        self.BackEnd = BackEnd()
        self.SGBD = SGBD()


    def criar(self,Nome,Descricao,NumeroPessoas,FrameWork,BackEnd, SGBD,id=0):
        self.id = id
        self.Nome = Nome
        self.Descricao = Descricao
        self.NumeroPessoas = NumeroPessoas
        self.FrameWork = FrameWork()
        self.BackEnd = BackEnd()
        self.SGBD = SGBD()

        print('\n**'*10,self.__str__())

    def __str__(self):
        return f'{self.id};{self.Nome};{self.Descricao};{self.NumeroPessoas};{self.BackEnd};{self.FrameWork};{self.SGBD}'

squad = Squad()