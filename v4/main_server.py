import socket
import threading
import time

time_1 = 0
time_clean = 3
chat_cancel = False
buffer = "\n\n\n\n\n\n\n*CHAT STARTS HERE*\n\n"
host_server = input("-> Host IP: ")

def clean_buffer():
    global time_1
    global time_clean
    global buffer
    global chat_cancel
    while(chat_cancel==False):
        time.sleep(1)
        time_1+=1
        if(time_1>=time_clean):
            if(len(buffer)>1024):
                buffer="\n\n\n\n\n\n\n*CHAT STARTS HERE*\n\n..."+buffer[524:]

def can_cancel():
    global chat_cancel
    global host_server
    while(chat_cancel==False):
        print("\n--If you want to close the server: Type \'0\' and Enter.--")
        opt = input("")
        if(opt=='0'):
            chat_cancel = True
            print("-- Closing --")
            close = "__Close__"
            server_socket.sendto(close.encode(), (host_server,1500))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local = ("",1500)
server_socket.bind(local)
mesage = ""

t1 = threading.Thread(target=clean_buffer)
t1.start()

t2 = threading.Thread(target=can_cancel)
t2.start()

print("\n\nOnline Server")
print("Waiting for data...\n")
while(chat_cancel==False):
    receive,client = server_socket.recvfrom(2048)
    mesage = receive.decode() 
    if(mesage==""):
        server_socket.sendto(buffer.encode(), client)
    else:
        buffer+="\n"+mesage
        print(buffer)

print("\n\n** Server Closed **")

print("\nClosing in 5 secs...")
time.sleep(5)

server_socket.close()
