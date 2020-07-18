# Chat

Versions of a chat in python. I think all these versions are interesting to keep here, due to they have their differences and are good at specific moments.

## V1
Simple Version. The server receive and client send and after client receive and server send.

To use: *python simple_client.py* or *python simple_server.py*, it depends if you want to host or not.
And if you want to be the first to send a mesage.

## V2
The same as the first version, but there is the "online" class that can do all the process of receiving and sending a mesage.

To use: *python main.py* and you decide if you want to be the server or the client.

## V3
This version uses threads to receive and send mesages at the same time.

To use: *python main.py* and you decide if you want to be the server or the client. 

## To End the Connection
Type '0' and press Enter. In version V3 after someone send '0' the other one has only one mesage left (because the threads are waiting for an input(at one node) and for a mesage(at the other node)).
