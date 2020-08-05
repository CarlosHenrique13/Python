#Pacotes Enternos
from tkinter.messagebox import showinfo
from tkinter import *
#Pacotes Interno
from src.ssh import *


class Interface():
    def __init__(self):
        # Vaiaveis Globais
        self.ssh = []
        # Janela
        self.janela = Tk()
        self.janela.title("SSH")
        self.janela.geometry("500x400+50+50")
        self.janela.resizable(0, 0)
        self.conetc = Label(self.janela, text="Conectado: 127.0.0.1", font=20, fg="black")
        self.conetc.pack()
        # Host Entrada
        Label(self.janela, text="Ip ou Domínio").place(x=5, y=20)
        self.host = Entry(self.janela)
        self.host.place(x=5, y=40)
        # Usuario Entrada
        Label(self.janela, text="Usuario").place(x=150, y=20)
        self.user = Entry(self.janela)
        self.user.place(x=150, y=40)
        # Senha Entrada
        Label(self.janela, text="Senha").place(x=290, y=20)
        self.pasw = Entry(self.janela, show="*")
        self.pasw.place(x=290, y=40)
        # Saida de Dados/Exibição
        self.saida = Text(self.janela, width=60, height=20)
        self.saida.place(x=5, y=70)
        # Eventos/Execução de Comandos
        self.btn_conf = Button(self.janela, text="Conectar", command=lambda: self.onclik())
        self.btn_conf.place(x=430, y=35)
        self.janela.bind("<KeyPress>", self.env)
        self.janela.mainloop()


    #Teclas precionadas
    def env(self,p):
        if str(self.janela.focus_get()) == ".!text":
            if p.keysym == "Return":
                try:
                    Enviar(self.ssh[0],self.saida.get("1.0","end-1c"),self.saida,self.conetc)
                except(IndexError):
                    showinfo(title='SSH', message='Não foi encontrado o servido')
            if p.keysym == "Delete":
                self.saida.delete('1.0', END)
        else:
            if p.keysym == "Return":
                self.ssh.append(self.onclik())
            if p.keysym == "Delete":
                self.saida.insert(END,"\n")

    def onclik(self):
        return self.ssh.append(Conect(self.conetc, self.host.get(), self.user.get(), self.pasw.get()))

