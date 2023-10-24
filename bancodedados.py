import sqlite3
#from interfacegrafica import 

class ConexaoBancoDeDados:

    def pesquisa(leva):

        try:
            conn = sqlite3.connect('meu_banco_de_dados.db')
            c = conn.cursor()
            c.execute("SELECT * FROM Livro")
            resu = c.fetchall()
            a = 0
            for linha in resu:
                print(linha)
                for i in range(0,5):
                    if linha[i] == leva:
                        gua[a] = linha[i]
                        a+=1
                        print("encontrado")
                    else:
                        print("não encontrado")
            conn.close()

        except sqlite3.Error as e:

            print(f"Erro de banco de dados: {e}")

    def cadastrar_Livro(leva):

        try:
            id,nome,autor,genero,ano = leva
            conn = sqlite3.connect('meu_banco_de_dados.db')
            c = conn.cursor()
            c.execute("INSERT INTO Livro (id,nome,genero,ano,autor) VALUES (?,?,?,?,?)",(id,nome,genero,ano,autor))
            conn.commit()
            conn.close()

        except sqlite3.Error as e:

            print(f"Erro de banco de dados: {e}")

    def cadastrar_Autor(leva):

        try:
            nome,ano,bio=leva
            conn = sqlite3.connect('meu_banco_de_dados.db')
            c = conn.cursor()
            c.execute("INSERT INTO Autor (nome,datadena,biografia) VALUES (?,?,?)",(nome,ano,bio))
            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            
            print(f"Erro de banco de dados: {e}")

    def cadastrar_Pessoa(leva):

        try:
            conn = sqlite3.connect('meu_banco_de_dados.db')
            c = conn.cursor()
            id,nome,cpf = leva
            c.execute("INSERT INTO Pessoa (nome,cpf,id) VALUES (?,?,?)",(nome,cpf,id))
            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            
            print(f"Erro de banco de dados: {e}")

    def pegar_emprestado(leva):

        try:
            print("deu")

        except sqlite3.Error as e:
            
            print(f"Erro de banco de dados: {e}")

    def devolver(leva):

        try:
            conn = sqlite3.connect('meu_banco_de_dados.db')
            c = conn.cursor()

            codl,cpf = leva

            c.execute("",())
            conn.commit()

            conn.close()

        except sqlite3.Error as e:
            
            print(f"Erro de banco de dados: {e}")
