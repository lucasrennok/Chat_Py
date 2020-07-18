import socket

HOST_SERVER = input("Server: ")
PORT_SERVER = 1500

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

client_socket.connect((HOST_SERVER,PORT_SERVER))
print("Connected\n")

mesage = ''
while(mesage!='0'):
    mesage = input("Answer: ")
    client_socket.send(mesage.encode()) 
    print("Mesage Sent!") 
    if(mesage=='0'):
        break
    mesage = client_socket.recv(1024)
    print("Received mesage: ",mesage.decode())

client_socket.close()