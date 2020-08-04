from paramiko import SSHClient
import paramiko

def Conect(saida,host,user,pasw):
    p = ""
    for c in range(0, len(pasw)):
        p += "*"
    saida.insert(0.0,f"Host:{host} User: {user} Passowd: {p}")
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


