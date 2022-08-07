"""
    Esse é um exemplo de utilização da biblioteca PyCryptoDome, implementando criptografia
    de chave pública RSA, com chave armazenada em variáveis locais.
    Fonte: https://pycryptodome.readthedocs.io/en/latest/src/examples.html
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def key_generator():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.public_key().export_key()

    keys = [private_key, public_key]

    return keys


def encryption(msg, public_key):
    msg = msg.encode()
    key = RSA.importKey(public_key)
    cipher_rsa = PKCS1_OAEP.new(key)
    c_msg = cipher_rsa.encrypt(msg)

    return c_msg


def decryption(c_msg, private_key):
    key = RSA.importKey(private_key)
    cipher_rsa = PKCS1_OAEP.new(key)
    msg = cipher_rsa.decrypt(c_msg)

    return msg.decode()


def main():

    msg = input('Digite sua mensagem: ')

    keys = key_generator()

    private_key = keys[0]
    public_key = keys[1]

    enc_msg = encryption(msg, public_key)

    print('Essa é a mensagem criptografada: {}.'.format(enc_msg))

    dec_msg = decryption(enc_msg, private_key)

    print('Essa é a mensagem descriptografada: "{}"'.format(dec_msg))


if __name__ == '__main__':
    main()
