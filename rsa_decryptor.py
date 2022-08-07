from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def decryption(key, c_msg):
    key = RSA.importKey(key)
    cipher_rsa = PKCS1_OAEP.new(key)
    msg = cipher_rsa.decrypt(c_msg)

    return msg


def main():
    with open("privateKey.bin", "rb") as f:
        key = f.read()

    with open("c_msg.bin", "rb") as f:
        c_msg = f.read()

    msg = decryption(key, c_msg).decode()

    print("A mensagem é: {}". format(msg))


if __name__ == "__main__":
    main()