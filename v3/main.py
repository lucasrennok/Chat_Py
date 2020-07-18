from online import online
import threading
import time

instance = None
received = '1'
sent = '1'

def receiving():
    global received
    global sent
    while(received!='0' and sent!='0'):
        received = instance.any_receive_mesage()
        print("Someone: ", received)

def sending():
    global sent
    global received
    while(sent!='0' and received!='0'):
        sent = input("")
        instance.any_send_mesage(sent)

choose = input("1-Server\n Any-Client\n")
max_connections = 3
max_bytes = 1024
port = 1502
host = ""

if(choose=='1'):
    instance = online(host, port, max_connections, max_bytes, True)
    instance.start_server()
else:
    host = input("server ip: ")
    instance = online(host, port, max_connections, max_bytes, False)
    instance.start_client()

print('\n-Status: CHAT ON-\n')

t1 = threading.Thread(target=receiving)
t2 = threading.Thread(target=sending)
t1.start()
t2.start()

while(t1.is_alive() and t2.is_alive()):
    time.sleep(1)

print("\nChat ended.")
