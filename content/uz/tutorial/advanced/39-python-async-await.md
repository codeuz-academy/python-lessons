---
layout: tutorial.njk
lang: uz
title: Python async/await
description: "Python'da Python async/await mavzusini amaliy misollar va tushunarli izohlar bilan o'rganing."
order: 39
permalink: /uz/tutorial/python-async-await/
---

<img src="/img/tutorial/39-python-async-await.webp" alt="Python async await - asynchronous programming" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

`async/await` bilan asinxron dasturlash - bu non-blocking ishlashga imkon beradigan paradigma. Bu ayniqsa ko'p I/O amallari bo'lgan ilovalar uchun foydali: HTTP so'rovlar, database access, fayl o'qish va hokazo.

### Nega asinxron?

An'anaviy sinxron dasturlashda:

```python
import time

def fetch_data_from_api():
    time.sleep(0.2)
    return "api"

def fetch_data_from_database():
    time.sleep(0.2)
    return "database"

def read_large_file():
    time.sleep(0.2)
    return "file"

start = time.perf_counter()
result1 = fetch_data_from_api()
result2 = fetch_data_from_database()
result3 = read_large_file()
elapsed = time.perf_counter() - start
print(result1, result2, result3)
print(f"Sinxron vaqt: {elapsed:.2f}s")
```

Asinxron yondashuvda:

```python
import asyncio
import time

async def fetch_data_from_api():
    await asyncio.sleep(0.2)
    return "api"

async def fetch_data_from_database():
    await asyncio.sleep(0.2)
    return "database"

async def read_large_file():
    await asyncio.sleep(0.2)
    return "file"

async def main():
    start = time.perf_counter()
    result1, result2, result3 = await asyncio.gather(
        fetch_data_from_api(),
        fetch_data_from_database(),
        read_large_file()
    )
    elapsed = time.perf_counter() - start
    print(result1, result2, result3)
    print(f"Asinxron vaqt: {elapsed:.2f}s")

asyncio.run(main())
```

### Asosiy tushunchalar

#### Coroutine

`async def` bilan yozilgan funksiya coroutine deyiladi:

```python
import asyncio

# Bu coroutine
async def greeting():
    print("Hello!")
    return "Done"

# Coroutine'ni bajarish
asyncio.run(greeting())
```

#### await

`await` coroutine yoki async operatsiya natijasini kutish uchun ishlatiladi:

```python
import asyncio

async def long_process():
    print("Start process...")
    await asyncio.sleep(2)  # Simulate async operation
    print("Process finished!")
    return "Result"

async def main():
    result = await long_process()
    print(f"Got: {result}")

asyncio.run(main())
```

### Coroutine'larni ishga tushirish

Coroutine'ni ishga tushirishning bir nechta yo'li bor:

```python
import asyncio

async def hello():
    await asyncio.sleep(1)
    return "Hello!"

# 1-usul: asyncio.run() - mustaqil skript uchun
if __name__ == "__main__":
    result = asyncio.run(hello())
    print(result)

# 2-usul: await - boshqa coroutine ichidan
async def main():
    result = await hello()
    print(result)
```

### Task'larni parallel bajarish

#### asyncio.gather()

Bir nechta coroutine'ni bir vaqtda (concurrently) bajaradi:

```python
import asyncio

async def download_file(name: str, duration: int) -> str:
    print(f"Start download {name}...")
    await asyncio.sleep(duration)
    print(f"Finished download {name}")
    return f"{name} downloaded"

async def main():
    # Hammasini bir vaqtda bajarish
    results = await asyncio.gather(
        download_file("file1.txt", 2),
        download_file("file2.txt", 3),
        download_file("file3.txt", 1),
    )
    print(f"All results: {results}")

asyncio.run(main())
# Natija:
# Start download file1.txt...
# Start download file2.txt...
# Start download file3.txt...
# Finished download file3.txt (1 soniyadan keyin)
# Finished download file1.txt (2 soniyadan keyin)
# Finished download file2.txt (3 soniyadan keyin)
# Jami vaqt: ~3 soniya (6 soniya emas)
```

#### asyncio.create_task()

Background'da ishlaydigan task yaratish:

```python
import asyncio

async def background_task():
    while True:
        print("Background task running...")
        await asyncio.sleep(1)

async def main():
    # Task yaratish (darhol bajarilmaydi)
    task = asyncio.create_task(background_task())
    
    # Boshqa ish qilish
    await asyncio.sleep(3)
    
    # Task'ni bekor qilish
    task.cancel()
    print("Task cancelled")

asyncio.run(main())
```

### Async context manager

Async resurs boshqaruvi uchun:

```python
import asyncio

class AsyncDatabaseConnection:
    async def __aenter__(self):
        print("Opening database connection...")
        await asyncio.sleep(1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection...")
        await asyncio.sleep(0.5)
    
    async def query(self, sql: str) -> list:
        await asyncio.sleep(0.5)
        return ["result1", "result2"]

async def main():
    async with AsyncDatabaseConnection() as db:
        result = await db.query("SELECT * FROM users")
        print(f"Query result: {result}")

asyncio.run(main())
```

### Async iterator

Async iteratsiya uchun:

```python
import asyncio

class AsyncCounter:
    def __init__(self, max_count: int):
        self.max_count = max_count
        self.current = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.max_count:
            raise StopAsyncIteration
        await asyncio.sleep(0.5)
        self.current += 1
        return self.current

async def main():
    async for num in AsyncCounter(5):
        print(f"Count: {num}")

asyncio.run(main())
```

### Amaliy misol: async HTTP so'rovlar

Async HTTP request uchun `aiohttp` kutubxonasidan foydalanish mumkin:

```python
# non-runnable: requires external environment/setup
import asyncio
import aiohttp

async def fetch_url(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()

async def main():
    urls = [
        "https://api.github.com/users/python",
        "https://api.github.com/users/django",
        "https://api.github.com/users/fastapi",
    ]
    
    async with aiohttp.ClientSession() as session:
        # Barcha URL'larni bir vaqtda olish
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        for result in results:
            print(f"User: {result.get('login')}")

# Avval o'rnating: pip install aiohttp
asyncio.run(main())
```

Bu yerda `aiohttp` ishlatiladi (chunki standard `requests` async'ni qo'llab-quvvatlamaydi). Tezlik uchun bitta `ClientSession` yaratiladi, so'ng har bir URL uchun task'lar ro'yxati tuziladi. `asyncio.gather(*tasks)` hammasini bir vaqtda bajaradi. 100 ta URL'dan data olish kerak bo'lsa, bu usul birma-bir olishdan ancha tez bo'ladi.

### Timeout va error handling

```python
import asyncio

async def long_operation():
    await asyncio.sleep(10)
    return "Done"

async def main():
    try:
        # 2 soniya timeout o'rnatish
        result = await asyncio.wait_for(long_operation(), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timeout!")

asyncio.run(main())
```

### Rate limiting uchun semaphore

Bir vaqtda nechta operatsiya bajarilishini cheklash:

```python
import asyncio

async def download(semaphore: asyncio.Semaphore, url: str):
    async with semaphore:  # Bir vaqtning o'zida faqat N ta so'rov
        print(f"Downloading {url}...")
        await asyncio.sleep(2)
        print(f"Finished {url}")
        return url

async def main():
    # Maksimal 3 ta bir vaqtda yuklash
    semaphore = asyncio.Semaphore(3)
    
    urls = [f"file_{i}.txt" for i in range(10)]
    tasks = [download(semaphore, url) for url in urls]
    
    await asyncio.gather(*tasks)

asyncio.run(main())
```

### Eng yaxshi amaliyotlar

1. **Async'ni I/O bound ishlar uchun ishlating** - HTTP, database, file I/O
2. **CPU bound uchun ishlatmang** - og'ir hisob-kitoblarda multiprocessing ishlating
3. **Coroutine'ni doim await qiling** - await bo'lmasa coroutine ishlamaydi
4. **Parallel uchun asyncio.gather() ishlating** - ketma-ket await'dan samaraliroq
5. **Exception'larni yaxshi boshqaring** - coroutine ichida try/except ishlating

### Qachon async ishlatish kerak?

<i class="fa-solid fa-circle-check" aria-hidden="true"></i> **Async ishlating**, agar:
- I/O operatsiyalar ko'p bo'lsa (HTTP, database, fayl)
- Web serverlar (FastAPI, aiohttp)
- Ko'p sahifali web scraping
- Chat ilovalar
- Real vaqt rejimidagi ma'lumotlarni qayta ishlash (real-time data processing)

<i class="fa-solid fa-circle-xmark" aria-hidden="true"></i> **Async ishlatmang**, agar:
- CPU ko'p ishlatadigan (CPU-intensive) vazifalar bo'lsa (multiprocessing ishlating)
- I/O kutishi yo'q oddiy operatsiyalar bo'lsa
- Bir vaqtlilik (concurrency) kerak bo'lmagan kichik skript bo'lsa
