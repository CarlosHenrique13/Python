from tkinter import *
from config.slid import *
from config.instalador import *
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
    barraMenu.add_cascade(label='apps',command=lambda: Instlador(janela,'Armazena/Programas'))
    #configuração da janela *unico
    janela.config(menu=barraMenu)

#Interface do usuario
def Interface():
    #Criação da Janela
    janela = Tk()
    Instlador(janela,'Armazena/Programas')
    BarraMenu(janela)
    janela.title("Projeto Nome")
    janela.geometry("500x400")
    janela.mainloop()
    return True


