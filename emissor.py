from socket import *
import pickle

host = 'localhost'
port = 60001

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((host, port))
print('Conexão com emissor estabelecida!')

msg = 'Rangel não acredita em mim... Menos um ponto pra ele'

msg = pickle.dumps(msg)

sock.send(msg)

print('Mensagem enviada!')

sock.close()

print('Conexão encerrada!')
