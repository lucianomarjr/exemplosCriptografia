from socket import *
import pickle

host = 'localhost'
port = 60001

sock = socket(AF_INET, SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

while True:
    print('Esperando conexão...')
    connection, address = sock.accept()
    print('Conexão estabelecida com o host {} na porta {}'.format(address[0], address[1]))
    received_msg = connection.recv(1024)
    msg = pickle.loads(received_msg)

    print('A mensagem recebida foi: {}'.format(msg))