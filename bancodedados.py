import sqlite3

class ConexaoBancoDeDados:

    def pesquisa():
        print

    def cadastrar_Livro(leva):

        id,nome,autor,genero,ano = leva
        conn = sqlite3.connect('meu_banco_de_dados.db')
        c = conn.cursor()

        c.execute("INSERT INTO Livro (id,nome,genero,ano,autor) VALUES (?,?,?,?,?)",(id,nome,genero,ano,autor))
        conn.commit()

        conn.close()

    def cadastrar_Autor(leva):

        nome,ano,bio=leva
        conn = sqlite3.connect('meu_banco_de_dados.db')
        c = conn.cursor()

        c.execute("INSERT INTO Autor (nome,datadena,biografia) VALUES (?,?,?)",(nome,ano,bio))
        conn.commit()

        conn.close()

    def cadastrar_Pessoa(leva):

        conn = sqlite3.connect('meu_banco_de_dados.db')
        c = conn.cursor()

        id,nome,cpf = leva

        c.execute("INSERT INTO Pessoa (nome,cpf,id) VALUES (?,?,?)",(nome,cpf,id))
        conn.commit()

        conn.close()

    def pegar_emprestado(leva):

        try:
            print("deu")

        except:
            print("erro")

    def devolver():

        conn = sqlite3.connect('meu_banco_de_dados.db')
        c = conn.cursor()

        codl,cpf = leva

        c.execute("",())
        conn.commit()

        conn.close()
