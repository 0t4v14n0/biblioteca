import tkinter as tk
from tkinter import *
from bancodedados import ConexaoBancoDeDados
import random

class meuapp:

    def __init__(self,root):

        self.root = root
        self.root.title("Biblioteca")

        self.img_menuprincipal   = PhotoImage(file="BIBLIOTECA/1.png")
        self.img_menucadtrouser  = PhotoImage(file="BIBLIOTECA/5.png")
        self.img_menucadtrouser2 = PhotoImage(file="BIBLIOTECA/6.png")
        self.img_menucadtrouser3 = PhotoImage(file="BIBLIOTECA/7.png")

        self.img_botaopesquisa   = PhotoImage(file="BIBLIOTECA/pesquisa.png")
        self.img_botaocadastroa  = PhotoImage(file="BIBLIOTECA/cadastroa.png")
        self.img_botaocadastrol  = PhotoImage(file="BIBLIOTECA/cadastrol.png")
        self.img_botaodevolucao  = PhotoImage(file="BIBLIOTECA/devolucao.png")
        self.img_botaoemprestimo = PhotoImage(file="BIBLIOTECA/emprestimo.png")

        self.imgsai= PhotoImage(file="BIBLIOTECA/botaosair.png")

        self.root.geometry("500x500")
        self.root.iconbitmap(default="BIBLIOTECA/icone.ico")
        self.root.resizable(width=1,height=1)
        self.labelfundo = tk.Label(root, image=self.img_menuprincipal)
        self.labelfundo.pack()

        botao = tk.Button(root,bd=0,image=self.img_botaopesquisa,command=self.pesquisa)
        botao.place(x=50,y=117,width=177,height=40)

        botao = tk.Button(root,bd=0,image=self.img_botaocadastrol,command=self.cadastrolivro)
        botao.place(x=50,y=177,width=177,height=40)

        botao = tk.Button(root,bd=0,image=self.img_botaocadastroa,command=self.cadastroaltor)
        botao.place(x=50,y=236,width=177,height=40)

        botao = tk.Button(root,bd=0,image=self.img_botaoemprestimo,command=self.emprestimo)
        botao.place(x=50,y=295,width=177,height=40)

        botao = tk.Button(root,bd=0,image=self.img_botaodevolucao,command=self.devolucao)
        botao.place(x=50,y=354,width=177,height=40)

        sair = tk.Button(root,bd=0,image=self.imgsai,command=root.destroy)
        sair.place(x=50,y=430,width=120,height=40)

#-----------------------------------DIMENSIONA OUTRAS JANELAS-----------------------------------------

    def janela_dimensionada(self,titulo,image):
        
        self.novajanela = tk.Toplevel(self.root)
        self.novajanela.title(titulo)

        largura_principal = self.root.winfo_width()
        altura_principal = self.root.winfo_height()

        self.novajanela.geometry(f"{largura_principal}x{altura_principal}")

        img_menupesquisa = PhotoImage(file=image)

        label_image = tk.Label(self.novajanela,image=img_menupesquisa)
        label_image.place(relwidth=1,relheight=1)

        self.novajanela.img_menupesquisa = img_menupesquisa

#----------------------------------------PESQUISA---------------------------------------------------

    def pesquisa(self):
        self.janela_dimensionada("PESQUISA","BIBLIOTECA/2.png")
        repesq = Entry(self.novajanela, bd=2, font=("Calibre", 15), justify=CENTER)
        repesq.place(width=392,height=45, x=50, y= 128)

        sair = tk.Button(self.novajanela,bd=0,image=self.imgsai,command=self.novajanela.destroy)
        sair.place(x=50,y=420,width=120,height=40)

#------------------------RECEBE OS VALORES E MANDA PARA FAZER O CADASTRO----------------------------

    def get_Livro(self):
        
        nome = self.repesq.get()
        self.repesq.delete(0, tk.END)

        autor = self.repesq2.get()
        self.repesq2.delete(0, tk.END)

        genero = self.repesq3.get()
        self.repesq3.delete(0, tk.END)

        ano = int(self.repesq4.get())
        self.repesq4.delete(0, tk.END)

        id = random.randrange(1,99)

        leva=[id,nome,autor,genero,ano]

        return ConexaoBancoDeDados.cadastrar_Livro(leva)

#---------------------------------CADASTRO DE LIVRO----------------------------------------------

    def cadastrolivro(self):

        self.janela_dimensionada("CADASTRO LIVRO","BIBLIOTECA/3.png")

        self.repesq = Entry(self.novajanela, bd=2, font=("Calibre", 15), justify=CENTER)
        self.repesq.place(width=300,height=40, x=100, y= 128)
        
        self.repesq2 = Entry(self.novajanela, bd=2, font=("Calibre", 15), justify=CENTER)
        self.repesq2.place(width=300,height=40, x=100, y= 210)

        self.repesq3 = Entry(self.novajanela, bd=2, font=("Calibre", 15), justify=CENTER)
        self.repesq3.place(width=300,height=40, x=100, y= 290)

        self.repesq4 = Entry(self.novajanela, bd=2, font=("Calibre", 15), justify=CENTER)
        self.repesq4.place(width=300,height=40, x=100, y= 380)

        sair = tk.Button(self.novajanela,bd=0,image=self.imgsai,command=self.novajanela.destroy)
        sair.place(x=50,y=450,width=120,height=40)

        self.imacadas = PhotoImage(file="BIBLIOTECA/botaocadastrar.png") 

        botaocada = tk.Button(self.novajanela,bd=0,image=self.imacadas, command= self.get_Livro)
        botaocada.place(x=330,y=450,width=120,height=40)

#------------------------------RECEBE OS VALORES DO CADASTRO DE AUTORES----------------------------------

    def get_Autor(self):
        
        nome = self.repesq.get()
        self.repesq.delete(0, tk.END)

        ano = int(self.repesq2.get())
        self.repesq2.delete(0, tk.END)

        bio = self.repesq3.get()
        self.repesq3.delete(0, tk.END)

        leva = nome,ano,bio

        return ConexaoBancoDeDados.cadastrar_Autor(leva)

#------------------------------------CADASTRO AUTOR--------------------------------------------------

    def cadastroaltor(self):

        self.janela_dimensionada("CADASTRO ALTOR","BIBLIOTECA/4.png")

        self.repesq = Entry(self.novajanela, bd=2, font=("Calibre", 15), justify=CENTER)
        self.repesq.place(width=300,height=40, x=100, y= 128)
        
        self.repesq2 = Entry(self.novajanela, bd=2, font=("Calibre", 15), justify=CENTER)
        self.repesq2.place(width=300,height=40, x=100, y= 222)

        self.repesq3 = Entry(self.novajanela, bd=2, font=("Calibre", 15), justify=CENTER)
        self.repesq3.place(width=300,height=137, x=100, y= 310)

        sair = tk.Button(self.novajanela,bd=0,image=self.imgsai,command=self.novajanela.destroy)
        sair.place(x=60,y=450,width=120,height=40)

        self.imacadas = PhotoImage(file="BIBLIOTECA/botaocadastrar.png") 

        botaocada = tk.Button(self.novajanela,bd=0,image=self.imacadas, command= self.get_Autor)
        botaocada.place(x=320,y=450,width=120,height=40)

#----------------------------------CADASTRAR PESSOA-------------------------------------------------

    def empres(self):

        print("ola")

#----------------------------------EMPRESTAR LIVRO-------------------------------------------------

    def cadaspe(self0):

        print("ola")

#-----------------------------------EMPRESTIMO------------------------------------------------------

    def emprestimo(self):

        self.janela_dimensionada("EMPRESTIMO","BIBLIOTECA/5.png")

        self.botao1 = PhotoImage(file="BIBLIOTECA/jacd.png")
        self.botao2 = PhotoImage(file="BIBLIOTECA/cadasg.png")

        sair = tk.Button(self.novajanela,bd=0,image=self.imgsai,command=self.novajanela.destroy)
        sair.place(x=50,y=420,width=120,height=40)

        botaocada = tk.Button(self.novajanela,bd=0,image=self.botao1, command= self.empres)
        botaocada.place(x=182,y=143,width=136,height=90)

        botaocada = tk.Button(self.novajanela,bd=0,image=self.botao2, command= self.cadaspe)
        botaocada.place(x=182,y=294,width=136,height=90)

#----------------------------------DEVOLUCAO-------------------------------------------------------

    def devolucao(self):
        self.janela_dimensionada("DEVOLUCAO","BIBLIOTECA/8.png")

        sair = tk.Button(self.novajanela,bd=0,image=self.imgsai,command=self.novajanela.destroy)
        sair.place(x=50,y=420,width=120,height=40)


if __name__ == "__main__":

    root = tk.Tk()
    app = meuapp(root)
    root.mainloop()
