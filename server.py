import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Set type to ip
server.bind((socket.gethostname(), 5050))
FORMAT = 'utf-8' # decoder
DISCONNECT_MESSAGE = "!DISCONNECT" # disconnect message
server.listen(5)

print(f"Starting on {(socket.gethostbyname(socket.gethostname()), 5050)}")

clientsocket, address = server.accept()
print(f"[NEW CONNECTION:] {address}")

while True:
    command = str(input("confithon:>>> "))
    if command == "exit":
        clientsocket.send(bytes("exit", "utf-8"))
        print("Disconnecting...")
        clientsocket.close()
    elif command == "break":
        try:
            clientsocket.send(bytes("break", "utf-8"))
        except Exception:
            pass
        break
    elif command == "write conf":
        clientsocket.send(bytes("writeConf", "utf-8"))
        name = str(input("NAME: "))
        version = str(input("VERSION: "))
        board = str(input("BOARD: "))
        number = str(input("NUMBER: "))
        clientsocket.send(bytes(f"NAME: {name}", "utf-8"))
        time.sleep(1)
        clientsocket.send(bytes(f"VERSION: {version}", "utf-8"))
        time.sleep(1)
        clientsocket.send(bytes(f"BOARD: {board}", "utf-8"))
        time.sleep(1)
        clientsocket.send(bytes(f"NUMBER: {number}", "utf-8"))
        time.sleep(1)
        print()
        print("{Configuration Sent}")
    elif  command == "show options":
        print("    'exit'       :  used to disconnect")
        print("    'break'      :  used to stop program")
        print("'show options'   :  used to show available options")

print("Exiting...")
time.sleep(2)