import socket
import threading
import time

time_1 = 0
time_clean = 3
buffer = "\n\n\n\n\n\n\n*CHAT STARTS HERE*\n\n"

def clean_buffer():
    global time_1
    global time_clean
    global buffer
    while(1):
        time.sleep(1)
        time_1+=1
        if(time_1>=time_clean):
            if(len(buffer)>1024):
                buffer="\n\n\n\n\n\n\n*CHAT STARTS HERE*\n\n"+buffer[512:]+"\n..."

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local = ("",1500)
server_socket.bind(local)
print("Online Server")
print("Waiting for data...\n")
mesage = ""

t1 = threading.Thread(target=clean_buffer)
t1.start()

while(1):
    receive,client = server_socket.recvfrom(2048)
    mesage = receive.decode() 
    if(mesage==""):
        server_socket.sendto(buffer.encode(), client)
    else:
        buffer+="\n"+mesage
        print(buffer)

server_socket.close()
