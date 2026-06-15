---
layout: tutorial.njk
lang: uz
title: Python'da ma'lumotlar bazasi bilan ishlash
description: "SQLite va DB-API yordamida Python'dan ma'lumotni saqlang va so'rang, xavfsiz parametrli so'rovlar bilan."
order: 26
permalink: /uz/tutorial/python-database-access/
---

<img src="/img/tutorial/26-python-database-access.webp" alt="Python database access - MySQL, SQL, Postgres" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python uchun database adapter'lar odatda DB-API 2.0 spetsifikatsiyasiga amal qiladi. Bu turli database'larda bir xil dasturlash modelini beradi: connect, cursor yaratish, SQL bajarish, row'larni olish (fetch), va commit/rollback.

Python bilan ko'p ishlatiladigan database'lar:

- SQLite (o'rnatilgan/built-in)
- PostgreSQL
- MySQL/MariaDB
- Microsoft SQL Server
- Oracle

### PyMySQL nima?

[PyMySQL](https://pymysql.readthedocs.io/en/latest/) — DB-API 2.0 ni amalga oshiradigan (implement) sof Python (pure-Python) MySQL mijozi (client).
SQLite bilan ishlasangiz, Python standart kutubxonasida (standard library) `sqlite3` allaqachon bor.

### PyMySQL o'rnatish

```bash
python -m pip install pymysql
```

### Ulanish sozlamasi (keyingi misollarda ishlatiladi)

Database kirish ma'lumotlarini (credentials) bir marta sozlab, har bir bo'limda `get_connection()` ni qayta ishlating.

```python
# non-runnable: requires external environment/setup
import pymysql

DB_CONFIG = {
    "host": "localhost",
    "user": "testuser",
    "password": "test123",
    "database": "TESTDB",
    "charset": "utf8mb4",
}

def get_connection():
    return pymysql.connect(**DB_CONFIG)
```

### Oddiy ulanish misoli

```python
# non-runnable: requires external environment/setup
with get_connection() as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print("Database version:", version)
```

### Jadval yaratish

Insert/read/update/delete qilishdan oldin schema yarating:

```python
# non-runnable: requires external environment/setup
create_sql = """
CREATE TABLE IF NOT EXISTS employee (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    age INT,
    sex CHAR(1),
    income DECIMAL(10, 2)
)
"""

with get_connection() as connection:
    with connection.cursor() as cursor:
        cursor.execute(create_sql)
    connection.commit()
```

### Ma'lumot qo'shish (parameterized query)

SQL injection oldini olish uchun placeholder ishlating.

```python
# non-runnable: requires external environment/setup
insert_sql = """
INSERT INTO employee (first_name, last_name, age, sex, income)
VALUES (%s, %s, %s, %s, %s)
"""

with get_connection() as connection:
    with connection.cursor() as cursor:
        cursor.execute(insert_sql, ("Mac", "Mohan", 20, "M", 2000.00))
    connection.commit()
```

### Ma'lumot o'qish

Ko'p row uchun `fetchall()`, bitta row uchun `fetchone()` ishlating:

```python
# non-runnable: requires external environment/setup
select_sql = "SELECT first_name, last_name, age, sex, income FROM employee WHERE income > %s"

with get_connection() as connection:
    with connection.cursor() as cursor:
        cursor.execute(select_sql, (1000,))
        rows = cursor.fetchall()

for row in rows:
    print(row)
```

### Ma'lumot yangilash

```python
# non-runnable: requires external environment/setup
update_sql = "UPDATE employee SET age = age + 1 WHERE sex = %s"

with get_connection() as connection:
    with connection.cursor() as cursor:
        cursor.execute(update_sql, ("M",))
    connection.commit()
```

### Ma'lumot o'chirish

```python
# non-runnable: requires external environment/setup
delete_sql = "DELETE FROM employee WHERE age > %s"

with get_connection() as connection:
    with connection.cursor() as cursor:
        cursor.execute(delete_sql, (20,))
    connection.commit()
```

### Transaction bo'yicha eslatmalar

- `connection.commit()` o'zgarishlarni saqlaydi.
- `connection.rollback()` saqlanmagan o'zgarishlarni bekor qiladi.
- Connection/cursor'larni doim yoping (yoki yuqoridagidek context manager ishlating).

Bir nechta yozish (write) amali ketma-ket bo'lsa, xatoda rollback qiling:

```python
# non-runnable: requires external environment/setup
with get_connection() as connection:
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE employee SET income = income + %s", (100,))
            cursor.execute("UPDATE employee SET income = income - %s WHERE id = %s", (100, 1))
        connection.commit()
    except Exception:
        connection.rollback()
        raise
```

### Ko'p uchraydigan xatolar

- `Access denied`: username/password yoki host noto'g'ri.
- `Unknown database` yoki `Table doesn't exist`: setup SQL hali bajarilmagan.
- `INSERT`/`UPDATE`/`DELETE` dan keyin `commit()`ni unutish, shuning uchun o'zgarishlar "saqlanmagandek" ko'rinadi.
- SQL'ni string formatlash bilan qurish, placeholder (`%s`) ishlatmaslik (SQL injection xavfi).

Til va kutubxonalar bo'yicha to'liq ma'lumot uchun [Python documentation](https://docs.python.org/3/) ni ko'ring.

