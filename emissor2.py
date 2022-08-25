from socket import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def encryption(key, msg):
    key = RSA.importKey(key)
    cipher_rsa = PKCS1_OAEP.new(key)
    c_msg = cipher_rsa.encrypt(msg)

    return c_msg


def main():
    host = 'localhost'
    port = 60001

    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    print('Conexão com receptor estabelecida!')

    msg = 'Essa é uma mensagem secreta!'

    with open("publicKey.bin", "rb") as f:
        key = f.read()

    msg = msg.encode()

    c_msg = encryption(key, msg)

    sock.send(c_msg)

    print('Mensagem enviada!')

    sock.close()

    print('Conexão encerrada!')


if __name__ == '__main__':
    main()