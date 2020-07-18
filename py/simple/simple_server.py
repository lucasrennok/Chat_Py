import socket

HOST = ""
PORT = 1500
MAX_CONNECTIONS = 3
MAX_BYTES = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(MAX_CONNECTIONS)

print("Online Server")
(client_socket, address) = server_socket.accept()
print("Connected\n")

mesage = ''
print("Waiting for data...\n")
while(mesage!='0'):
    receive = client_socket.recv(MAX_BYTES)
    mesage = receive.decode() 
    if(mesage=='0'):
        break
    print("Received mesage: ", mesage)
    msg = input("Answer: ")
    client_socket.send(msg.encode())
    print("Mesage Sent!") 


server_socket.close()
