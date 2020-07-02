import os
from tkinter import *


class Instal():
    def __init__(self):
        local = os.getcwd()
        print(local)

    def interface(self,janela,objeto,x=0,y=0):
        item = objeto
        item.place(x=x,y=y)
        janela.update()



def Tela(janela):
    janela_interface = janela


def InstalardorInic(janela):
    apps  = os.listdir("Armazena/Programas")
    programas = []
    for c in range(0,len(apps)):
        programas.append(f"Armazena\Programas\{apps[c]}")    
    
    for c in range(0,len(apps)):
        print(f"{programas[c]}\{apps[c]}")
        btn = Button(janela,text=apps[c],command=lambda: os.startfile(f"{os.getcwd()}\{programas[c]}\{apps[c]}"))
        btn.grid(row=0,column=c)