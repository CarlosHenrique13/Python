from tkinter import *
import os

#Barra de Menu
def BarraMenu(janela):
    barraMenu = Menu(janela)
    #Cria a categooria
    items1 = Menu(barraMenu)
    #Itens
    items1.add_command(label='Calculadora')
    #Colocar categoria no menu
    barraMenu.add_cascade(label='Conexão', menu=items1)
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