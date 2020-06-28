from tkinter import *
from config.slid import *
import os

#Barra de Menu
def BarraMenu(janela):
    barraMenu = Menu(janela)
    #Cria a categooria
    items1 = Menu(barraMenu)
    slid = Menu(barraMenu)
    #Itens
    items1.add_command(label='Calculadora')
    slid.add_command(label="Escrever",command=lambda: EscreverSlid())
    slid.add_command(label="Ler",command=lambda: LeitorSlid())
    #Colocar categoria no menu
    barraMenu.add_cascade(label='Conexão', menu=items1)
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