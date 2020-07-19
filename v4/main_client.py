from online import online
import threading
import time

instance = None
received = '1'
sent = '1'
name = input("What's your name?\n> ")

def receiving():
    global received
    global sent
    while(sent!='0'):
        received = instance.any_receive_mesage()
        if(received!=""):
            print(received)

def sending():
    global sent
    global received
    global name
    instance.any_send_mesage("*"+name+" joined the chat*\n")
    while(sent!='0'):
        sent = input("")
        if(sent=="0"):
            instance.any_send_mesage("*"+name+" left the chat*\n> Type Enter to Quit\n")
            break
        instance.any_send_mesage(name+": "+sent)

#Configs
max_bytes = 1024
port = 1502

host = input("Chat IP: ")
instance = online(host, port, 0, max_bytes, False)
instance.start_client()

print('\n-Status: CHAT ON-\n*Type \'0\' and \'Enter\' to quit the chat*\n')

t1 = threading.Thread(target=receiving)
t2 = threading.Thread(target=sending)
t1.start()
t2.start()

while(t1.is_alive() and t2.is_alive()):
    time.sleep(1)

print("\nChat ended.")
