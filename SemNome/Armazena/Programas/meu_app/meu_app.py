from config.instalador import Instal
from tkinter import *

class MeuApp():
    def __init__(self):
        pass



janela = Tk()
instalador = Instal()
instalador.interface(janela,Entry(),0,0)
janela.mainloop()
