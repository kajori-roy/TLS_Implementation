import socket
import rsa 
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from time import sleep

def load_keys():
    with open('public_key.pem', 'rb') as file:
        publicKey = RSA.importKey(file.read())
        rsa_cipher = PKCS1_OAEP.new(publicKey)
        return rsa_cipher

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!!! BYE BYE CLIENT :("
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    pubkey = load_keys()
    message = pubkey.encrypt(msg.encode())
    # print(message)
    client.send(message)
    print(client.recv(4086).decode(FORMAT))

send("Transport Layer Security (TLS) is a cryptographic protocol.")
sleep(1)
send("The protocol is widely used in applications such as email, instant messaging, and voice over IP, but its use in securing HTTPS remains the most publicly visible.")
sleep(1)
send("The TLS protocol aims primarily to provide security, including privacy (confidentiality), integrity, and authenticity through the use of cryptography.")
sleep(1)
send("It runs in the presentation layer and is itself composed of two layers: the TLS record and the TLS handshake protocols.")


send(DISCONNECT_MESSAGE)