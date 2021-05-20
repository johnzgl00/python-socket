import socket
import threading

HEADER = 64 # bite message lenght
PORT = 5050 # set port 
SERVER = socket.gethostbyname(socket.gethostname()) # get server ip address
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Set type to ip
server.bind(ADDR) # every device goes to ADDR is refearing to this socket (server)
FORMAT = 'utf-8' # decoder
DISCONNECT_MESSAGE = "!DISCONNECT" # disconnect message

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"{addr}: {msg}")
            conn.send("message received".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

print("[STARTING] Starting server....")
print(f"[LISTENING] listening on {ADDR}")
start()