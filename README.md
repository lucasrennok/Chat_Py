# :floppy_disk: Chat

Versions of a chat in python. I think all these versions are interesting to keep here, due to they have their differences and are good at specific moments.

## :arrow_forward: V1
Simple Version. The server receive and client send and after client receive and server send.

> To use: *python simple_client.py* or *python simple_server.py*, it depends if you want to host or not and if you want to be the first to send a mesage.

## :arrow_forward: V2
The same as the first version, but there is the "online" class that can do all the process of receiving and sending a mesage.

> To use: *python main.py* and you decide if you want to be the server or the client.

## :arrow_forward: V3
This version uses threads to receive and send mesages at the same time. It works to a private chat(with only 2 people).

> To use: *python main.py* and you decide if you want to be the server or the client. 

## :arrow_forward: V4
This version uses threads to receive and send mesages at the same time. It works to a group of friends or a private chat.
It uses a server to receive the mesages and send to all the people connected. The people can leave the server whatever they want, typing '0'.

> To use: *python main_client.py* to connect to a server or *python main_server.py* to create a server.

## :no_entry: To End the Connection
Type '0' and press Enter. In version V3 after someone send '0' the other one has only one mesage left (because the threads are waiting for an input(at one node) and for a mesage(at the other node)).
