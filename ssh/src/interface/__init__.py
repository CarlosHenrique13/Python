#Pacotes Enternos
from tkinter import *

#Pacotes Interno
from src.ssh import *

#Janela
janela = Tk()
janela.title("SSH")
janela.geometry("500x300+50+50")
conetc = Label(janela,text="Conectado: 127.0.0.1")
conetc.pack()
#Host Entrada
Label(janela,text="Ip ou Domínio").place(x=5,y=20)
host = Entry(janela)
host.place(x=5,y=40)
#Usuario Entrada
Label(janela,text="Usuario").place(x=150,y=20)
user = Entry(janela)
user.place(x=150,y=40)
#Senha Entrada
Label(janela,text="Senha").place(x=290,y=20)
pasw = Entry(janela,show="*")
pasw.place(x=290,y=40)
#Saida de Dados/Exibição
saida = Text(janela)
saida.place(x=5,y=70)
#Eventos/Execução de Comandos
btn_conf = Button(janela,text="Conectar",command=lambda: Conect(saida,host.get(),user.get(),pasw.get()))
btn_conf.place(x=430,y=35)
janela.mainloop()