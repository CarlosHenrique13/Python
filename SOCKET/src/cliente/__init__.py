import socket

def Client(host="127.0.0.1",porta=8585):
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
            return str(dados.decode('utf-8')+"\n")
        except(ConnectionRefusedError):
            return ("[-][TCP]Nenhuma conexão pôde ser feita porque a máquina de destino as recusou ativamente \n")
        except():
            pass
            
