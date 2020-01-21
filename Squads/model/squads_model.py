class SquadsModel():
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao = ''
        self.numeropessoas = 0
        self.linguagembackend = ''
        self.frameworkfrontend = ''

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeropessoas};{self.linguagembackend};{self.frameworkfrontend}'

squadsm = SquadsModel()