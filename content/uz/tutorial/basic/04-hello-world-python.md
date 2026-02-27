---
layout: tutorial.njk
lang: uz
title: Hello World (Python)
order: 4
permalink: /uz/tutorial/hello-world-python/
---

<img src="/img/tutorial/4-hello-world-python.webp" alt="Hello World (Python)" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Birinci Python dasturi odatda bitta `print()` chaqiruvidan iborat bo'ladi. `print()` funksiyasi matnni standart chiqishga (terminal yoki konsolga) chiqaradi.

### Asosiy sintaksis

```python
print("Hello World")
```

Yuqoridagi skriptni ishga tushirsangiz, Python quyidagini chiqaradi:

`Hello World`

Qavs ichidagi qiymat **argument** deyiladi. String argumentlar qo'shtirnoq ichida bo'lishi kerak: yoki bir tirnoq (`'...'`), yoki qo'sh tirnoq (`"..."`). Ikkalasi ham bir xil:

```python
print('Hello World')
print("Hello World")
```

Shuningdek, sonlar va ifodalarni qo'shtirnoqsiz ham chiqarish mumkin:

```python
print(42)
print(10 + 5)
```

### Indentatsiya

Python kod bloklarini indentatsiya (qator boshidagi bo'sh joy) bilan belgilaydi. Ko'plab tillardagi `{}` qavslar o'rniga Python bir xil indentatsiyaga tayanadi:

```python
if True:
    print("This is indented")
```

Indentatsiya noto'g'ri bo'lsa, `IndentationError` chiqadi.

### Python katta-kichik harflarni farqlaydi

Python case-sensitive. `print()` ishlaydi, lekin `Print()` yoki `PRINT()` `NameError` beradi.

Bu qoida o'zgaruvchi nomlari va funksiya nomlariga ham tegishli. Masalan, `name` va `Name` - ikki xil o'zgaruvchi.

