import socket
import threading
import time

buffer = ""
mesage = ""
name = input("What's your name?\n> ")
HOST_SERVER = input("Server: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receiveMesage():
    global client_socket
    global HOST_SERVER
    global mesage
    buffer_history = ""
    timer = 0
    while(1):
        if(mesage=='0'):
            break
        elif(timer%5==0):
            timer=0
            msg = ""
            client_socket.sendto(msg.encode(), (HOST_SERVER,1500)) 
            buffer,server = client_socket.recvfrom(2048)
            if(buffer.decode()!=buffer_history):
                print(buffer.decode())
                print(">--------<")
            buffer_history = buffer.decode()
        time.sleep(1)
        timer+=1

t = threading.Thread(target=receiveMesage)
t.start()

join = "*"+name+" joined the chat*"
left = "*"+name+" left the chat*"
client_socket.sendto(join.encode(),(HOST_SERVER,1500))
while(mesage!='0'):
    mesage = input("")    
    if(mesage=='0'):
        break
    mesage=name+": "+mesage
    client_socket.sendto(mesage.encode(),(HOST_SERVER,1500)) 
client_socket.sendto(left.encode(),(HOST_SERVER,1500))

client_socket.close()