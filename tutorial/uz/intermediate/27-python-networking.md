---
layout: tutorial.njk
lang: uz
title: Python networking (tarmoq)
order: 27
permalink: /tutorial/uz/python-networking/
---

<img src="/img/tutorial/23-tutorial-networking-python.webp" alt="Python networking darsi" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python past darajali (low-level) va yuqori darajali (high-level) networking modullarini taqdim etadi.

- Low-level: TCP/UDP client va serverlar uchun `socket`
- High-level: `urllib`, `http.client`, `smtplib`, `imaplib`, `ftplib` va boshqalar

Avval socket bilan asoslarni tushunib oling, keyin production ilovalar uchun yuqori darajali kutubxonalardan foydalaning.

### Socket nima?

Socket - bu dasturlar orasida ikki tomonga aloqa (two-way communication) uchun endpoint.
Socket'lar bir xil kompyuterda ishlayotgan process'lar orasida ham, tarmoq orqali boshqa kompyuterlarda ham ishlashi mumkin.

### Socket moduli

Socket yaratish:

`socket.socket(family=AF_INET, type=SOCK_STREAM)`

- `AF_INET` IPv4 uchun
- `SOCK_STREAM` TCP uchun
- `SOCK_DGRAM` UDP uchun

`SOCK_STREAM` (TCP) ishonchli va tartibli (ordered). `SOCK_DGRAM` (UDP) tezroq, lekin yetib borishni kafolatlamaydi.

### Server socket metodlari

| Metod | Izoh |
| ---------- | ----------------------------------------------------------------------------------------- |
| `bind()` | `(host, port)` manzilini socket'ga bog'laydi |
| `listen()` | Kiruvchi TCP ulanishlarini kutishni boshlaydi |
| `accept()` | Kiruvchi ulanishni qabul qilib `(conn, addr)` qaytaradi |

### Client socket metodlari

| Metod | Izoh |
| ----------- | ----------------------------------------------------- |
| `connect()` | TCP server'ga ulanadi |

### Umumiy socket metodlari

| Metod | Izoh |
| -------------------- | --------------------------------- |
| `recv()` | Byte'larni qabul qilish |
| `sendall()` | Barcha byte'larni yuborish |
| `recvfrom()` | UDP paketni qabul qilish |
| `sendto()` | UDP paketni yuborish |
| `close()` | Socket'ni yopish |

### Oddiy TCP server

Bu minimal server bitta client ulanishini qabul qiladi, bir marta javob yuboradi va chiqadi.

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

### Oddiy TCP client

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

Avval server'ni ishga tushiring, keyin boshqa terminal'dan client'ni ishga tushiring.

### Python'dagi keng tarqalgan internet modullari

| Protokol | Default port | Python moduli |
| -------- | ------------ | ----------------------------- |
| HTTP | 80 | `urllib.request`, `http.client` |
| HTTPS | 443 | `urllib.request`, `http.client` |
| FTP | 21 | `ftplib` |
| SMTP | 25 / 587 | `smtplib` |
| POP3 | 110 | `poplib` |
| IMAP4 | 143 | `imaplib` |
| NNTP | 119 | `nntplib` |
| XML-RPC | (over HTTP) | `xmlrpc.client` |

Production tizimlarda imkon qadar yuqori darajali kutubxonalarni tanlang va doim timeout qo'shing.

### Ko'p uchraydigan xatolar

- `ConnectionRefusedError`: server ishlamayapti yoki host/port noto'g'ri.
- Client `recv()`da osilib qoladi: timeout yo'q va server data yubormaydi.
- `OSError: [Errno 98] Address already in use`: oldingi process portni band qilgan.
- `str` va `bytes`ni aralashtirish: socket byte yuboradi/qabul qiladi, shuning uchun encode/decode ni aniq qiling.

