---
layout: tutorial.njk
title: Python Networking
order: 27
permalink: /tutorial/en/python-networking/
---

<img src="/img/tutorial/23-tutorial-networking-python.webp" alt="Python Networking Tutorial" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python provides low-level and high-level networking modules.

- Low-level: `socket` for TCP/UDP clients and servers
- High-level: `urllib`, `http.client`, `smtplib`, `imaplib`, `ftplib`, and others

Start with low-level sockets to understand the basics, then use higher-level libraries for production applications.

### What is Socket?

A socket is an endpoint for two-way communication between programs.
Sockets can communicate between processes on the same machine or across different machines on a network.

### Socket Module

Create a socket with:

`socket.socket(family=AF_INET, type=SOCK_STREAM)`

- `AF_INET` for IPv4
- `SOCK_STREAM` for TCP
- `SOCK_DGRAM` for UDP

`SOCK_STREAM` (TCP) is reliable and ordered. `SOCK_DGRAM` (UDP) is faster but does not guarantee delivery.

### Server Socket Methods

| Method | Explanation |
| ---------- | ----------------------------------------------------------------------------------------- |
| `bind()` | Bind address `(host, port)` to socket |
| `listen()` | Start listening for incoming TCP connections |
| `accept()` | Accept incoming connection and return `(conn, addr)` |

### Client Socket Methods

| Method | Explanation |
| ----------- | ----------------------------------------------------- |
| `connect()` | Connect to TCP server |

### General Socket Methods

| Method | Explanation |
| -------------------- | --------------------------------- |
| `recv()` | Receive bytes |
| `sendall()` | Send all bytes |
| `recvfrom()` | Receive UDP packet |
| `sendto()` | Send UDP packet |
| `close()` | Close socket |

### Simple TCP Server

This minimal server accepts one client connection, sends a response once, and exits.

```python
import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        conn.sendall(b"Thank you for connecting")
```

### Simple TCP Client

```python
import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(5)  # seconds
    s.connect((HOST, PORT))
    data = s.recv(1024)

print(data.decode("utf-8"))
```

Run server first, then run client from another terminal.

### Common Python Internet Modules

| Protocol | Default Port | Python Module |
| -------- | ------------ | ----------------------------- |
| HTTP | 80 | `urllib.request`, `http.client` |
| HTTPS | 443 | `urllib.request`, `http.client` |
| FTP | 21 | `ftplib` |
| SMTP | 25 / 587 | `smtplib` |
| POP3 | 110 | `poplib` |
| IMAP4 | 143 | `imaplib` |
| NNTP | 119 | `nntplib` |
| XML-RPC | (over HTTP) | `xmlrpc.client` |

For production systems, prefer higher-level libraries when appropriate and always add timeout handling.

### Common Errors

- `ConnectionRefusedError`: server is not running or wrong host/port.
- Client hangs on `recv()`: no timeout configured and server sends no data.
- `OSError: [Errno 98] Address already in use`: previous process still holds the port.
- Mixing `str` and `bytes`: sockets send/receive bytes, so encode/decode explicitly.
