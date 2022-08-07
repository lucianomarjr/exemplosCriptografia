from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def encryption(key, msg):
    key = RSA.importKey(key)
    cipher_rsa = PKCS1_OAEP.new(key)
    c_msg = cipher_rsa.encrypt(msg.encode())

    return c_msg


def main():
    msg = input("Digite sua mensagem: ")

    with open("publicKey.bin", "rb") as f:
        key = f.read()

    c_msg = encryption(key, msg)

    with open("c_msg.bin", "wb") as f:
        f.write(c_msg)

    print("The message was encrypted!")


if __name__ == '__main__':
    main()
