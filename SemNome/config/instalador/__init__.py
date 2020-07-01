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
    pass

