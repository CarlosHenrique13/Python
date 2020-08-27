from tkinter import *
from config.slid import *
from config.instalador import *
from time import strftime
import os

#Documentação
def Sobre(janela):
    clear(janela)
    Label(janela,text='Link: http://syshen.epizy.com/index.html').grid(row=0,column=0)
    Label(janela,text='Criador: Carlos Henrique Alves dos Santos').grid(row=1,column=0)
    Label(janela,text='Versão: 0.0.1').grid(row=2,column=0)
    Label(janela,text='©SysHen').grid(row=2,column=1)

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
    barraMenu.add_cascade(label='Sobre',command=lambda: Sobre(janela))
    #configuração da janela *unico
    janela.config(menu=barraMenu)

#Interface do usuario
def Interface():
    # Relogio
    def tictac():
        agora = strftime('%H:%M:%S')
        if relogio['text'] != agora:
            relogio['text'] = agora
        relogio.after(100, tictac)
    #Criação da Janela
    janela = Tk()
    Instlador(janela,'Armazena/Programas')
    BarraMenu(janela)
    #Relogio na Tela
    relogio = Label(janela, text='')
    relogio['text'] = strftime('%H:%M:%S')
    relogio.place(x=450, y=0)
    tictac()
    janela.title("Projeto Nome")
    janela.geometry("500x400")
    janela.mainloop()
    return True


