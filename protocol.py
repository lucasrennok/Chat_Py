"""Enquadramento de mensagens sobre TCP.

TCP é um fluxo de bytes: um `recv` pode trazer meia mensagem ou várias
juntas. Para delimitar cada mensagem, mandamos um cabeçalho de 4 bytes com
o tamanho (big-endian) seguido do conteúdo em UTF-8. Isso resolve o problema
das versões antigas, que assumiam que cada mensagem chegava inteira em um
único `recv`.
"""

import socket

HEADER = 4  # bytes do prefixo de tamanho
MAX_MESSAGE = 64 * 1024


def send_message(sock: socket.socket, message: str) -> None:
    data = message.encode("utf-8")
    sock.sendall(len(data).to_bytes(HEADER, "big") + data)


def _recv_exactly(sock: socket.socket, size: int) -> bytes | None:
    """Lê exatamente `size` bytes, ou None se a conexão fechar antes."""
    chunks = bytearray()
    while len(chunks) < size:
        chunk = sock.recv(size - len(chunks))
        if not chunk:
            return None
        chunks.extend(chunk)
    return bytes(chunks)


def recv_message(sock: socket.socket) -> str | None:
    """Recebe uma mensagem enquadrada. Retorna None quando a conexão fecha."""
    header = _recv_exactly(sock, HEADER)
    if header is None:
        return None
    length = int.from_bytes(header, "big")
    if length == 0:
        return ""
    if length > MAX_MESSAGE:
        raise ConnectionError("mensagem grande demais")
    payload = _recv_exactly(sock, length)
    if payload is None:
        return None
    return payload.decode("utf-8", errors="replace")
