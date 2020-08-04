#Pacotes Enternos
from tkinter.messagebox import showinfo
from tkinter import *
#Pacotes Interno
from src.ssh import *

#Vaiaveis Globais
ssh = []

#Teclas precionadas
def env(p):
    if str(janela.focus_get()) == ".!text":
        if p.keysym == "Return":
            try:
                Enviar(ssh[0],saida.get("1.0","end-1c"))
            except(IndexError):
                showinfo(title='SSH', message='Não foi encontrado o servido')
        if p.keysym == "Delete":
            saida.delete('1.0', END)
    else:
        if p.keysym == "Return":
            ssh.append(onclik())
        if p.keysym == "Delete":
            saida.insert(END,"\n")

def onclik():
    return Conect(conetc, host.get(), user.get(), pasw.get())

#Janela
janela = Tk()
janela.title("SSH")
janela.geometry("500x400+50+50")
janela.resizable(0,0)
conetc = Label(janela,text="Conectado: 127.0.0.1",font=20,fg="black")
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
saida = Text(janela,width=60,height=20)
saida.place(x=5,y=70)
#Eventos/Execução de Comandos
btn_conf = Button(janela,text="Conectar",command=lambda: onclik())
btn_conf.place(x=430,y=35)
janela.bind("<KeyPress>",env)
janela.mainloop()