class BackEnd:
    def __init__(self):
        self.id = 0
        self.Nome = ''
        
        
    def criar(self,Nome,id=0):
        self.id = id
        self.Nome = Nome
        
        print('\n**'*10,self.__str__())

    def __str__(self):
        return f'{self.id};{self.Nome}'

backend = BackEnd()