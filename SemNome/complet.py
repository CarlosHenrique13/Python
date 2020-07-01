from tkinter import *
from config.slid import *
import os


#Barra de Menu
def BarraMenu(janela):
    barraMenu = Menu(janela)
    #Cria a categooria
    slid = Menu(barraMenu)
    #Itens
    slid.add_command(label="Escrever",command=lambda: EscreverSlid(janela))
    slid.add_command(label="Ler",command=lambda: LeitorSlid(janela))
    #Colocar categoria no menu
    barraMenu.add_cascade(label='Slid',menu=slid)
    #configuração da janela *unico
    janela.config(menu=barraMenu)

#Interface do usuario
def Interface():
    #Criação da Janela
    janela = Tk()
    BarraMenu(janela)
    janela.title("Projeto Nome")
    janela.geometry("500x400")
    janela.mainloop()
    return True



class Instalador:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Teste")


    def text(self,texto):
        Label(self.janela,text=texto).place(x=5,y=5)

    def loop(self):
        self.janela.mainloop()

janela = Instalador()
janela.text("oi")
os.system("python Armazena/Programas/meu_app/meu_app.py")