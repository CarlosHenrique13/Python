from tkinter import *
from tkinter import ttk
import os


if not os.path.exists("Armazena/Slids"):
    os.makedirs("Armazena/Slids")


#Escrever Arquivo
def EscreverSlid(janela):
    #Cria o Arquivo e Ecrever
    def Escreve(arquivo,texto):
        arg = open(f"Armazena/Slids/{arquivo}.txt","wt+")
        arg.write(texto)
    def Exit():
        nome_label.destroy()
        arg_name.destroy()
        btn.destroy()
        escrever.destroy()
        sair.destroy()

    nome_label = Label(janela,text="Nome do Arquivo: ")
    nome_label.place(x=5,y=5)
    arg_name = Entry(janela)
    arg_name.place(x=120,y=5)
    btn = Button(janela, text="Enviar", command=lambda: Escreve(arg_name.get(),escrever.get(1.0, END)))
    btn.place(x=250,y=5)
    escrever = Text(janela,width=35,height=10)
    escrever.place(x=5,y=35)
    sair = Button(janela, text="sair", command=lambda: Exit())
    sair.place(x=5, y=200)

#Ler o Arquivo
def LeitorSlid(janela):
    def Ler(name):
        arg = open(f"Armazena/Slids/{name}","rt")
        linhas = arg.read()
        texto.insert(1.0,linhas)
    def Exit():
        label1.destroy()
        arg_name.destroy()
        btn.destroy()
        texto.destroy()
        sair.destroy()

    label1 = Label(janela, text="Nome do Arquivo: ")
    label1.place(x=5, y=5)
    arg_name = ttk.Combobox(janela,value=os.listdir("Armazena/Slids/"))
    arg_name.place(x=120, y=5)
    btn = Button(janela, text="Proximo", command=lambda: Ler(arg_name.get()))
    btn.place(x=270, y=5)
    texto = Text(janela, width=40, height=10)
    texto.place(x=5, y=35)
    sair = Button(janela, text="sair", command=lambda: Exit())
    sair.place(x=5, y=200)