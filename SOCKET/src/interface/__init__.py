from tkinter import *
from src.cliente import Client
from src.servido import Server

janela = Tk()
janela.title("Socket")
janela.geometry("500x500")
janela.resizable(0, 0)
#Ip ou DNS
Label(janela,text="IP").place(x=5,y=4)
ip = Entry()
ip.place(x=5,y=20)
#Usuário
Label(janela,text="Usuário").place(x=155,y=4)
user = Entry(janela)
user.place(x=155,y=20)
#Senha
Label(janela,text="Senha").place(x=305,y=4)
pasw = Entry(janela,show="*")
pasw.place(x=305,y=20)
#Porta
Label(janela,text="Porta").place(x=460,y=4)
port = Entry(janela,width=5)
port.place(x=460,y=20)
#Are de saida de informação
text_area = Text(janela,width=60,height=25)
text_area.place(x=5,y=90)
#Butões
try:
    btn_client = Button(janela,text="Cliente", command=lambda: text_area.insert('1.0',Client(host=ip.get(), porta=int(port.get()))))
    btn_client.place(x=5, y=50)
except:
    pass
try:
    btn_server = Button(janela,text="Server",command=lambda: Server(host=ip.get(),porta=int(port.get())))
    btn_server.place(x=70,y=50)
except:
    pass
janela.mainloop()