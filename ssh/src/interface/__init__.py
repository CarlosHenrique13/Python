from tkinter import *

#Janela
janela = Tk()
janela.title("SSH")
conetc = Label(janela,text="Conectado: 127.0.0.1")
conetc.pack()
#Host Entrada
Label(janela,text="Ip ou Domínio").pack()
host = Entry(janela)
host.pack()
#Usuario Entrada
user = Entry(janela)
user.pack()
#Senha Entrada
pasw = Entry(janela,show="*")
pasw.pack()
#Saida de Dados/Exibição
saida = Text(janela)
saida.pack()
janela.mainloop()