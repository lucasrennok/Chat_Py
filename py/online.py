from server import server
from client import client

class online:
    def __init__(self, host, port, max_connections, max_bytes, sv):
        if(sv == False):
            self.node = client(host,port, max_bytes)
        elif(sv == True):
            self.node = server("",port,max_connections,max_bytes)

    def start_server(self):
        self.node.accept_connections()

    def start_client(self):
        self.node.connect_to_server()

    def any_receive_mesage(self):
        mesage = self.node.receive_mesage()
        return mesage

    def any_send_mesage(self,mesage):
        self.node.send_mesage(mesage)

    def close_multiplayer(self):
        self.node.close_connection()
