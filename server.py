#!/usr/bin/env python3
"""Servidor de chat em grupo (TCP).

Aceita vários clientes e repassa cada mensagem recebida para todos os outros.
Cada cliente roda em sua própria thread.

Uso:
    python server.py                 # escuta em 0.0.0.0:1500
    python server.py --host 127.0.0.1 --port 5000
"""

import argparse
import socket
import threading

from protocol import recv_message, send_message


class ChatServer:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.clients: dict[socket.socket, str] = {}
        self.lock = threading.Lock()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def broadcast(self, message: str, exclude: socket.socket | None = None) -> None:
        """Envia a mensagem para todos os clientes, menos `exclude`."""
        with self.lock:
            targets = [s for s in self.clients if s is not exclude]
        for sock in targets:
            try:
                send_message(sock, message)
            except OSError:
                self.remove_client(sock)

    def remove_client(self, sock: socket.socket) -> None:
        with self.lock:
            name = self.clients.pop(sock, None)
        sock.close()
        if name:
            print(f"- {name} saiu")
            self.broadcast(f"* {name} saiu do chat *")

    def handle_client(self, sock: socket.socket, address) -> None:
        try:
            name = recv_message(sock)
        except (OSError, ConnectionError):
            sock.close()
            return
        if not name:
            sock.close()
            return

        with self.lock:
            self.clients[sock] = name
        print(f"+ {name} entrou ({address[0]}:{address[1]})")
        self.broadcast(f"* {name} entrou no chat *", exclude=sock)

        try:
            while True:
                message = recv_message(sock)
                if message is None:  # cliente desconectou
                    break
                print(f"{name}: {message}")
                self.broadcast(f"{name}: {message}", exclude=sock)
        except (OSError, ConnectionError):
            pass
        finally:
            self.remove_client(sock)

    def start(self) -> None:
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Servidor ouvindo em {self.host}:{self.port} (Ctrl+C para encerrar)")
        try:
            while True:
                sock, address = self.server_socket.accept()
                threading.Thread(
                    target=self.handle_client, args=(sock, address), daemon=True
                ).start()
        except KeyboardInterrupt:
            print("\nEncerrando servidor...")
        finally:
            with self.lock:
                socks = list(self.clients)
            for sock in socks:
                sock.close()
            self.server_socket.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Servidor de chat em grupo.")
    parser.add_argument("--host", default="0.0.0.0", help="IP para escutar")
    parser.add_argument("--port", type=int, default=1500, help="porta (padrão: 1500)")
    args = parser.parse_args()
    ChatServer(args.host, args.port).start()


if __name__ == "__main__":
    main()
