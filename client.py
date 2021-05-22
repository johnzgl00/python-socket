import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 5050))

while True:    
    msg = client.recv(9999)
    final_msg = msg.decode('utf-8')
    if final_msg == "exit" or final_msg == "break":
        print(final_msg)
        break
    elif final_msg == "writeConf":
        infoList = []
        for i in range(4):
            info = client.recv(9999)
            final_info = info.decode('utf-8')
            #print(final_info)
            infoList.append(final_info)
            i =+ 1
        print(infoList)
        info_to_write = str(infoList)
        file=open("module.info", "a")
        file.write(info_to_write)
        file.close()
x = input()