class SquadsModel:
    def __init__(self):
        self.ID = 0
        self.Nome = ''
        self.Descricao = ''
        self.NumeroPessoas = 0
        self.LinguagemBackEnd = ''
        self.FrameWorkFrontEnd = ''

    def __str__(self):
        return f'{self.ID};{self.Nome};{self.Descricao};{self.NumeroPessoas};{self.LinguagemBackEnd};{self.FrameWorkFrontEnd}'
