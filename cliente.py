import socket

def main():
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("criou o socket")

    socketTCP.connect(('192.168.0.156', 8080))
    print("conexão estabelecida")

    socketTCP.send(b"o rato roeu a roupa do rei de roma\r\n")
    print("mensagem enviada")

    linha = ""
    while True:
        data = socketTCP.recv(10)
        linha += data.decode("UTF-8")

        if linha.endswith("\r\n"):
            break
    
    print("mensagem recebida do servidor: ", linha)

main()
