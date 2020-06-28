from tkinter import *
from tkinter import ttk
import os


#Escrever Arquivo
def EscreverSlid():
    #Cria o Arquivo e Ecrever
    def Escrever(arquivo,texto):
        arg = open(f"Armazena/Slids/{arquivo}.txt","wt+")
        #for c in range(0,len(texto)):
        arg.write(texto)




    janela = Tk()
    janela.geometry("300x210")
    Label(janela,text="Nome do Arquivo: ").place(x=5,y=5)
    arg_name = Entry(janela)
    arg_name.place(x=120,y=5)
    btn = Button(janela, text="Enviar", command=lambda: Escrever(arg_name.get(),escrever.get(1.0, END)))
    btn.place(x=250,y=5)
    escrever = Text(janela,width=35,height=10)
    escrever.place(x=5,y=35)
    janela.mainloop()

#Ler o Arquivo
def LeitorSlid():
    pass

#Função Principal
def Slid():
    janela = Tk()
    arg_name = Entry()
    arg_name.grid(0,0)
    escreve = Entry()
    escreve.grid(0,1)
    janela.mainloop()
