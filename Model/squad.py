from Model.backend import BackEnd
from Model.framework import FrameWork
from Model.sgdb import Sgdb
class Squad:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao= ''
        self.numeropessoas = 0
        self.id_framework = 0
        self.id_backend = 0
        self.id_sgdb = 0 
        self.framework = FrameWork()
        self.backend = BackEnd()
        self.sgdb = Sgdb()

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeropessoas};{self.id_framework};{self.id_backend};{self.id_sgdb}'
