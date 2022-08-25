import pickle
from socket import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256


def decryption(key, c_msg):
    key = RSA.importKey(key)
    cipher_rsa = PKCS1_OAEP.new(key)
    msg = cipher_rsa.decrypt(c_msg)

    return msg


def hash_verification(c_msg, h_msg):
    d_hash = SHA256.new()
    d_hash.update(c_msg)
    d_hash = d_hash.hexdigest()

    if d_hash == h_msg:
        msg = "Integridade OK!"
        return msg
    else:
        msg = "Descarte a mensagem!"
        return msg


def main():
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

        received_msg = pickle.loads(received_msg)

        c_msg = received_msg["msg"]
        d_hash = received_msg["hash"]

        h_verification = hash_verification(c_msg, d_hash)

        print(h_verification)

        with open("privateKey.bin", "rb") as f:
            key = f.read()

        msg = decryption(key, c_msg)
        msg = msg.decode()

        print('A mensagem recebida foi: {}'.format(msg))


if __name__ == "__main__":
    main()