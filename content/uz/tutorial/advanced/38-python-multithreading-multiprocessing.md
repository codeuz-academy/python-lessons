---
layout: tutorial.njk
lang: uz
title: Python multithreading va multiprocessing
order: 38
permalink: /uz/tutorial/python-multithreading-multiprocessing/
---

<img src="/img/tutorial/33-multithreading.webp" alt="Python multithreading va multiprocessing" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Zamonaviy dasturlashda *parallelism* va *concurrency* kabi atamalar ko'p uchraydi. Python'da bir vaqtning o'zida bir nechta ishni bajarishning ikki asosiy yo'li bor: **multithreading** va **multiprocessing**.

Qaysi birini tanlash vazifangiz turiga bog'liq: u **I/O Bound**mi yoki **CPU Bound**mi.

### 1. I/O Bound va CPU Bound

- **I/O Bound**: dastur ko'proq input/output kutadi (misol: network so'rovlar, diskdan o'qish, database query). Bu paytda CPU ko'pincha bo'sh turadi.
- **CPU Bound**: dastur ko'proq hisob-kitob (matematika, og'ir data processing) qiladi. CPU 100% ishlaydi.

### 2. Multithreading (I/O Bound uchun)

Threading bitta process ichida bir nechta thread ishlatadi. Thread'lar xotirani bo'lishadi (shared memory).

Lekin Python (CPython) da **GIL (Global Interpreter Lock)** bor: u bir vaqtning o'zida ikki thread'ning bitta CPU core'da Python bytecode bajarishini cheklaydi. Shuning uchun Python multithreading **CPU-bound** ishlarni tezlashtirmaydi (hatto overhead sabab sekinlashishi ham mumkin).

Ammo **I/O bound** ishlar uchun multithreading juda foydali: bitta thread kutayotgan paytda (masalan web javobini), boshqasi ishlashi mumkin.

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

# Wait for all threads to complete
for t in threads:
    t.join()

end = time.time()
print(f"Total time: {end - start:.2f} seconds")
# Output around 2 seconds, not 6 seconds!
```

### 3. Multiprocessing (CPU Bound uchun)

Multiprocessing alohida Python process'larni yaratadi. Har bir process'ning o'z Python interpreter'i va xotira maydoni bo'ladi. Bu GIL'ni chetlab o'tadi va multi-core CPU'dan maksimal foydalanishga imkon beradi.

Og'ir hisob-kitobli vazifalar uchun shuni ishlating.

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
    
    # Create 2 processes running parallel on different CPU cores
    p1 = multiprocessing.Process(target=heavy_square_calculation, args=(1,))
    p2 = multiprocessing.Process(target=heavy_square_calculation, args=(2,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    end = time.time()
    print(f"Total time: {end - start:.2f} seconds")
```

*Eslatma: Windows'da multiprocessing ishlatganda asosiy kodni `if __name__ == "__main__":` bilan himoyalash kerak.*

### 4. Concurrent Futures (zamonaviy usul)

Python `concurrent.futures` modulini beradi. U Threading va Multiprocessing uchun yuqori darajali va ishlatish oson interfeys.

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

### Xulosa

| Xususiyat | Multithreading | Multiprocessing |
| :--- | :--- | :--- |
| **Xotira** | Shared memory (umumiy) | Separate memory (izolyatsiya) |
| **Overhead** | Past | Yuqori (process start vaqt oladi) |
| **Mos vazifa** | I/O Bound (network, file) | CPU Bound (hisob-kitob, data processing) |
| **GIL** | GIL ta'sir qiladi | GIL'dan holi |

