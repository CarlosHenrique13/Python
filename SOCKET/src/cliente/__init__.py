import socket

def Client(self,host,porta=8585):
        """
        -> Cliente TCP
        :param host: Ip de destino
        :param porta: porta de comunicação
        :return: None
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, porta))
            dados = s.recv(1024)
            print(dados.decode('ascii'))
        except(ConnectionRefusedError):
            print("[-][TCP]Nenhuma conexão pôde ser feita porque a máquina de destino as recusou ativamente")
        except():
            pass
            
            