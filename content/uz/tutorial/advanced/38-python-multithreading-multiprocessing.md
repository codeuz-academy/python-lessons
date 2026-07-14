---
layout: tutorial.njk
lang: uz
title: Python multithreading va multiprocessing
description: "Ishni parallel bajaring va GIL atrofida qachon thread, qachon process tanlashni biling."
order: 38
permalink: /uz/tutorial/python-multithreading-multiprocessing/
---

<img src="/img/tutorial/38-python-multithreading.webp" alt="Python multithreading va multiprocessing" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Zamonaviy dasturlashda *parallelism* va *concurrency* kabi atamalar ko'p uchraydi. Python'da bir vaqtning o'zida bir nechta ishni bajarishning ikki asosiy yo'li bor: **multithreading** va **multiprocessing**.

Qaysi birini tanlash vazifangiz turiga bog'liq: u **I/O Bound**mi yoki **CPU Bound**mi.

### 1. I/O Bound va CPU Bound

- **I/O Bound**: dastur ko'proq kirish/chiqish (`input/output`) amallarini kutadi (masalan, tarmoq so'rovlari, diskdan o'qish, ma'lumotlar bazasi so'rovi). Bu paytda CPU ko'pincha bo'sh turadi.
- **CPU Bound**: dastur ko'proq hisob-kitob qiladi (matematika, og'ir ma'lumot qayta ishlash). CPU asosiy yukni bajaradi.

### 2. Multithreading (I/O Bound uchun)

Threading bitta process ichida bir nechta thread ishlatadi. Thread'lar umumiy xotirani baham ko'radi (`shared memory`).

Lekin Python (CPython) da **GIL (Global Interpreter Lock)** bor: u bir vaqtning o'zida ikki thread'ning bitta CPU core'da Python bytecode bajarishini cheklaydi. Shuning uchun Python multithreading **CPU-bound** ishlarni tezlashtirmaydi (hatto overhead sabab sekinlashishi ham mumkin).

Ammo **I/O bound** ishlar uchun multithreading juda foydali: bitta thread kutayotgan paytda (masalan, veb javobini), boshqasi ishlashi mumkin.

```python
import threading
import time

def download_page(url):
    print(f"Start downloading {url}...")
    time.sleep(2) # Simulate network delay
    print(f"Finished downloading {url}")

start = time.time()

threads = []
urls = ["web1", "web2", "web3"]

for url in urls:
    t = threading.Thread(target=download_page, args=(url,))
    threads.append(t)
    t.start()

# Barcha thread'lar tugashini kutish
for t in threads:
    t.join()

end = time.time()
print(f"Umumiy vaqt: {end - start:.2f} soniya")
# Natija taxminan 2 soniya, 6 soniya emas!
```

### 3. Multiprocessing (CPU Bound uchun)

Multiprocessing alohida Python process'larni yaratadi. Har bir process'ning o'z Python interpreter'i va xotira maydoni bo'ladi. Bu GIL'ni chetlab o'tadi va multi-core CPU'dan maksimal foydalanishga imkon beradi.

Og'ir hisob-kitobli vazifalar uchun shu yondashuvni tanlang.

```python
import multiprocessing
import time

def heavy_square_calculation(number):
    print(f"Process {number} starts...")
    result = sum(i * i for i in range(10**7)) # Heavy calculation
    print(f"Process {number} finished.")
    return result

if __name__ == "__main__":
    start = time.time()

    # Turli CPU core'larda parallel ishlaydigan 2 ta process yaratish
    p1 = multiprocessing.Process(target=heavy_square_calculation, args=(1,))
    p2 = multiprocessing.Process(target=heavy_square_calculation, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print(f"Umumiy vaqt: {end - start:.2f} soniya")
```

*Eslatma: Windows'da multiprocessing ishlatganda asosiy kodni `if __name__ == "__main__":` bilan himoyalash kerak.*

### 4. Concurrent Futures (zamonaviy usul)

Python `concurrent.futures` modulini beradi. U threading va multiprocessing uchun yuqori darajali, ishlatish oson interfeys.

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(1)
    return f"Task {n} finished"

start = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3])

    for result in results:
        print(result)

print(f"Time: {time.time() - start:.2f} seconds")
```
Multiprocessing'ga o'tmoqchi bo'lsangiz `ThreadPoolExecutor` o'rniga `ProcessPoolExecutor` ishlating.

### 5. Thread xavfsizligi va Lock'lar

Thread'lar xotirani baham ko'rgani uchun, ikkita thread bir vaqtda bitta o'zgaruvchini yangilasa, uni buzishi mumkin — bu **race condition**. `Lock` bir vaqtning o'zida faqat bitta thread kritik qismga kirishini ta'minlaydi.

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000):
        with lock:          # bir vaqtda faqat bitta thread yangilaydi
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)   # 200000  (lock tufayli to'g'ri)
```

`Lock` bo'lmasa, oxirgi qiymat ko'pincha 200000 dan kam bo'lardi, chunki ikkala thread ham yozishdan oldin bir xil eski qiymatni o'qishi mumkin.

> <i class="fa-solid fa-circle-info" aria-hidden="true"></i> **Eslatma:** I/O bilan bog'liq ishda bir tredli concurrency uchun `asyncio` ko'pincha thread'lardan ko'ra mosroq. [Async / Await](/uz/tutorial/python-async-await/) darsiga qarang.

### Xulosa

| Xususiyat | Multithreading | Multiprocessing |
| :--- | :--- | :--- |
| **Xotira** | Umumiy xotira (`shared memory`) | Alohida xotira (`separate memory`) |
| **Overhead** | Past | Yuqori (process boshlanishi vaqt oladi) |
| **Mos vazifa** | I/O Bound (tarmoq, fayl) | CPU Bound (hisob-kitob, ma'lumot qayta ishlash) |
| **GIL** | GIL ta'sir qiladi | GIL'dan holi |
