#!/usr/bin/env python3
"""Cliente de chat em grupo (TCP).

Uma thread recebe as mensagens e a thread principal lê o que você digita.
Digite '0' e Enter (ou Ctrl+C) para sair.

Uso:
    python client.py                       # conecta em 127.0.0.1:1500
    python client.py --host 192.168.0.10 --port 1500 --name Lucas
"""

import argparse
import socket
import threading

from protocol import recv_message, send_message


def receive_loop(sock: socket.socket, stop: threading.Event) -> None:
    while not stop.is_set():
        try:
            message = recv_message(sock)
        except (OSError, ConnectionError):
            message = None
        if message is None:
            if not stop.is_set():
                print("\n* Conexão encerrada pelo servidor *")
            stop.set()
            break
        print(message)


def main() -> None:
    parser = argparse.ArgumentParser(description="Cliente de chat em grupo.")
    parser.add_argument("--host", default="127.0.0.1", help="IP do servidor")
    parser.add_argument("--port", type=int, default=1500, help="porta (padrão: 1500)")
    parser.add_argument("--name", help="seu nome (senão será perguntado)")
    args = parser.parse_args()

    name = args.name or input("Qual é o seu nome?\n> ").strip() or "anônimo"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((args.host, args.port))
    except OSError as exc:
        print(f"Não foi possível conectar em {args.host}:{args.port} ({exc})")
        return

    send_message(sock, name)
    print("** Conectado ** — digite '0' e Enter para sair.\n")

    stop = threading.Event()
    threading.Thread(target=receive_loop, args=(sock, stop), daemon=True).start()

    try:
        while not stop.is_set():
            text = input()
            if text == "0":
                break
            if text:
                send_message(sock, text)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        stop.set()
        sock.close()
        print("Saindo do chat.")


if __name__ == "__main__":
    main()
