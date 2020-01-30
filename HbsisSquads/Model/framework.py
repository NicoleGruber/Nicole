class FrameWork:
    def __init__(self):
        self.id = 0
        self.nome = ''

    def __str__(self):
        return f'{self.id};{self.nome}'

framework = FrameWork()