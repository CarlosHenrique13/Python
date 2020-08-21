from tkinter import *

class Interface():
    def __init__(self,Widt,Height):
        self.width = str(Widt)
        self.height = str(Height)
        self.janela = Tk()
        self.janela.geometry(f"{self.width} x {self.height}")
        self.janela.mainloop()

    def Buton(self,text_button,pos,func):
        """
        -> Criar Buttons 
        :param text_button: Titulo para o butão
        :param pos: Posição do botão
        :param func: Função que o botão vai ter
        :return: None
        """
        name_button = Button(self.janela,text=text_button,command=lambda: func )
        name_button.place(x=pos[0],y=pos[1])


