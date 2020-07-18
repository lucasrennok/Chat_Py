from online import online

choose = input("1-Server\n Any-Client\n")
max_connections = 3
max_bytes = 1024
port = 1502
host = ""
received = '1'

if(choose!='1'):
    host = input("server ip: ")
print('Status: ON')

if(choose=='1'):
    instance = online(host, port, max_connections, max_bytes, True)
    instance.start_server()
    while(received!='0'):
        received = instance.any_receive_mesage()
        if(received=='0'):
            break
        print("Mesage received: ", received)
        received = input("Mesage to sent: ")
        instance.any_send_mesage(received)
else:
    instance = online(host, port, max_connections, max_bytes, False)
    instance.start_client()
    while(received!='0'):
        received = input("Mesage to sent: ")
        instance.any_send_mesage(received)
        if(received=='0'):
            break
        received = instance.any_receive_mesage()
        print("Mesage received: ", received)

print("\nChat ended.")