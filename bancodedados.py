import sqlite3

class ConexaoBancoDeDados:

    def cadastrar_Livro(id,nome,genero,autor,ano):

        conn = sqlite3.connect('meu_banco_de_dados.db')
        c = conn.cursor()

        c.execute("INSERT INTO Livro (id,nome,genero,ano,autor) VALUES (?,?,?,?,?)",(id,nome,genero,autor,ano))
        conn.commit()

        conn.close()
