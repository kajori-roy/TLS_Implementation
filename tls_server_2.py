import socket 
import threading
import rsa
import get_public_key
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from time import sleep

def load_keys():
    # (public_k, pvt_k) = get_public_key.get_keys()
    # # with open('private_key.pem', 'rb') as p:
    # #     privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    # #     return privateKey
    # return pvt_k
    with open("private_key.pem","rb") as file:
        private_key = RSA.importKey(file.read())
    rsa_cipher = PKCS1_OAEP.new(private_key)
    return rsa_cipher

# HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!BYE BYE CLIENT!!!!"
rsa_cipher = load_keys()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:
            msg = conn.recv(4086)
            if msg:
                print("\n DATA BEFORE DECRYPTION..")
                print(msg)
                # msg_dec = rsa.decrypt(msg, priv_key).decode('ascii')
                msg_dec = rsa_cipher.decrypt(msg)

                if msg == DISCONNECT_MESSAGE:
                    connected = False

                # print(f"[{addr}] {msg_dec}")
                print("\n DATA AFTER DECRYPTION..\n")
                print(f"\n \n [{addr}] {msg_dec.decode(FORMAT)}")
                conn.send("Msg received".encode(FORMAT))

        except ValueError:
            sleep(10)

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()