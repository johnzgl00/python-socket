import socket

HEADER = 64 # bite message lenght
PORT = 5050 # set port 
SERVER = "192.168.68.16"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8' # decoder
DISCONNECT_MESSAGE = "!DISCONNECT" # disconnect message

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def sent(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

sent("hello wolrd")
sent("activate")
sent(DISCONNECT_MESSAGE)