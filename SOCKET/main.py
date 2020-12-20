from src.cliente import *
from src.servido import*
from src.interface import *


if __name__ == '__main__':
    try:
        Interfce()
    except:
        r = str(input("[C] Conectar aao Cliente [S] Ser um Servidor: ").upper())
        if r == "C":
            try:
                Client(host=str(input("Ip: ")),porta=int(input("Porta: ")))
            except:
                print("[-] Valores Incorestos")
        elif r == "S":
            try:
                Server(host=str(input("Ip:")),porta=int(input("Porta: ")))
            except:
                print("[-] Valores Incorestos")