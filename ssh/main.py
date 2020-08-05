from src.ssh import *
from src.interface import *

try:
    interface = Interface()
except:
    Cmd(str(input("host:")),str(input("Usuario: ")),str(input("Senha: ")))