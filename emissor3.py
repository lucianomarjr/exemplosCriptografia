from socket import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import pickle


def hash_function(data):
    d_hash = SHA256.new()
    d_hash.update(data)
    d_hash = d_hash.hexdigest()
    #print(d_hash.hexdigest())

    return d_hash


def msg_format(c_msg, d_hash):
    msg = {
        "hash": d_hash,
        "msg": c_msg
    }

    msg = pickle.dumps(msg)

    return msg


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

    d_hash = hash_function(c_msg)

    print(d_hash)

    send_msg = msg_format(c_msg, d_hash)

    sock.send(send_msg)

    print('Mensagem enviada!')

    sock.close()

    print('Conexão encerrada!')


if __name__ == '__main__':
    main()