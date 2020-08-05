from tkinter import END
from tkinter.messagebox import showinfo
from paramiko import SSHClient
import paramiko


def Conect(text,host,user,pasw):
    """
    -> Conexão SSH
    :param saida: Tela para informação
    :param host: ip ou domínio para coneção
    :param user: Usuario que for se conectar
    :param pasw: Senha corespondente ao usuario
    :return: OS dddos da conexão ssh
    """
    try:
        #Montagem da exibição
        p = ""
        for c in range(0, len(pasw)):
            p += "*"
        #Conexão
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=pasw)
        text["text"] = f"Host: {host} User: {user} Passowd: {p}\n"
        text["fg"] = "green"
        #Envio de Comando
        return ssh
    except:
        showinfo(title='SSH', message='Não foi possivel se conectar')


def Enviar(ssh,cmd,retorno,texto):
    try:
        entrada, saida, erro = ssh.exec_command(cmd)
        retorno.insert(0.0,saida.readlines())
        retorno.insert(0.0,erro.readlines())
        if cmd == "exit\n":
            texto["text"] = "Conectado: 127.0.0.1"
            texto["fg"] = "black"
            ssh.close()
            retorno.delete('1.0',END)
            print("fim")
    except:
        pass

def Cmd(host,user,pasw):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=pasw)
    while True:
        cmd = str(input("ssh>> "))
        entrada, saida, erro = ssh.exec_command(cmd)
        print(saida.readlines())
        print(erro.readlines())
        if cmd == "exit":
            ssh.close()
            break
    print("Finalizado")