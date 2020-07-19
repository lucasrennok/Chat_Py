from online import online
import threading
import time

instance = None
received = ""
timer=0

def receiving():
    global received
    while(1):
        #recebe de qualquer um
        received = instance.any_receive_mesage()
        print(received)

def sending():
    global received
    global timer
    instance.any_send_mesage("* started the chat *\n")
    while(1):
        if(received!=""):
            #envia pra todos
            instance.any_send_mesage(received)
            received=""
        if(timer%2==0):
            #envia para todos
            instance.any_send_mesage("")
            if(timer>1000):
                timer=0

#Configs
max_connections = 3
max_bytes = 1024
port = 1502

instance = online("", port, max_connections, max_bytes, True)
instance.start_server()

print('\n-Status: CHAT ON-\n')

t1 = threading.Thread(target=receiving)
t2 = threading.Thread(target=sending)
t1.start()
t2.start()

while(t1.is_alive() and t2.is_alive()):
    time.sleep(1)
    timer+=1

print("\nChat ended.")
