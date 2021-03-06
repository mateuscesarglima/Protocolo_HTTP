import socket
import _thread as thread
from datetime import datetime


def comunicarComCliente(socketDoCliente):
    linha = ""

    while True:
        data = socketDoCliente.recv(10)
        linha += data.decode("UTF-8")

        if linha.endswith("\r\n"):
            now = datetime.now()
            horaAtual = now.strftime("%d/%m/%Y %H:%M:%S")

            socketDoCliente.send(linha.encode("UTF-8"))
            socketDoCliente.send(horaAtual.encode("UTF-8"))

            print(linha)
            break

    socketDoCliente.close()


def main():
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("criou o socket")

    socketTCP.bind(('', 8080))
    print("vinculou a porta 8080")

    socketTCP.listen()
    print("escutando novas conexões")

    while True:
        print("aguardando nova conexão...")
        novoSocketDaConexao, enderecoDoCliente = socketTCP.accept()
        print("nova conexão do cliente: ", enderecoDoCliente)

        thread.start_new_thread(comunicarComCliente,
                                tuple([novoSocketDaConexao]))


main()
