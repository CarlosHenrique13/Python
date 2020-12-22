from tkinter import *
from src.cliente import *

class Interface():
    def __init__(self):
        self.ftp = FTP_()

        janela = Tk()
        janela.title("Ciente FTP")
        janela.geometry("800x500")
        janela.resizable(0,0,)
        # IP ou DNS
        Label(janela,text="IP").place(x=5,y=4)
        self.ip = Entry(janela)
        self.ip.insert(0,"10.0.0.104")
        self.ip.place(x=5,y=20)
        # Usuario Name
        Label(janela,text="Usuário").place(x=150,y=4)
        self.user = Entry(janela)
        self.user.insert(0,"henrique")
        self.user.place(x=150,y=20)
        # Usuario Senha
        Label(janela,text="Senha").place(x=300,y=4)
        self.pasw = Entry(janela,show="*")
        self.pasw.place(x=300,y=20)
        self.pasw.insert(0,"123")
        # Porta
        Label(janela,text="Porta").place(x=450,y=4)
        self.port = Entry(janela,width=5)
        self.port.insert(0,"21")
        self.port.place(x=450,y=20)


        # Meu Pc Dados
        Label(janela,text="Diretorias do Computador").place(x=5,y=96)
        self.pc_dir = Text(janela,width=20,height=17,bg="orange",fg="black",font=10)
        self.pc_dir.place(x=5,y=100)

        # Servido Dados
        Label(janela,text="Diretorias do Servidor").place(x=200,y=96)
        #server_dir = Text(janela,width=20,height=17,bg="black",fg="white",font=10)
        #server_dir.place(x=200,y=100)

        self.server_dir = Listbox(janela,height=16,bg="black",fg="white",font=10)
        self.server_dir.place(x=200,y=100)

        # Tranferencias
        self.saida = Text(janela,width=50,height=4,bg="blue",fg="white",font=10)
        self.saida.place(x=5,y=420)


        # Botões
        btn_conecta = Button(janela,text="Conectar",command=lambda: self.Conectar())
        btn_conecta.place(x=5,y=50)
        btn_dow = Button(janela,text="Download",command=lambda: self.Donwload())
        btn_dow.place(x=80,y=50)
        btn_up = Button(janela,text="Upload",command=lambda: self.Conectar())
        btn_up.place(x=160,y=50)
        btn_del = Button(janela,text="Deleta",command=lambda: self.Conectar())
        btn_del.place(x=240,y=50)

        janela.mainloop()
    def Conectar(self):
    # Conectar ao Servido
    self.server, self.resut = self.ftp.Client(ip=self.ip.get(), login=self.user.get(), password=self.pasw.get(), port=int(self.port.get()))
    self.saida.insert('1.0',self.resut)
    self.itens = self.ftp.ListDirectories(self.server)
    for values in self.itens:
        self.server_dir.insert(END, values)
