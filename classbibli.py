
class Livro:
    def __init__(self, id, nome, genero, ano, autor):
        self.id =id
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.ano = ano

class Autor:
    def __init__(self, nome , datadena, biografia):
        self.nome = nome
        self.datadena = datadena
        self.biografia = biografia

class Pessoa:
    def __init__(self, nome, cpf, id):
        self.nome = nome
        self.cpf = cpf
        self.id = id