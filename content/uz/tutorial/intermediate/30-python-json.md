---
layout: tutorial.njk
lang: uz
title: Python'da JSON bilan ishlash
description: "Python'da JSON'ni o'qing va yozing hamda JSON matni bilan dict va list o'rtasida o'tkazing."
order: 30
permalink: /uz/tutorial/python-json/
---

<img src="/img/tutorial/30-python-json.webp" alt="Python JSON" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

JSON (JavaScript Object Notation) - data saqlash va tashish (transport) uchun ommabop format. Dasturlashda JSON ko'pincha internetdan (API'lar) data olishda yoki ilovalar bir-biri bilan ma'lumot almashganda ishlatiladi.

Boshlovchilar uchun JSON'ni tartibli va o'qilishi oson "shopping list"ga o'xshatish mumkin: uni ham odam, ham kompyuter oson o'qiydi. Ko'rinishi Python'dagi *Dictionary* ga o'xshagani uchun, JSON o'rganish tanish tuyuladi va veb-servislar bilan bog'lanadigan yoki konfiguratsiyalarni saqlaydigan ilovalar yozishda juda foydali bo'ladi.

Quyida JSON object tuzilmasi va qisqa izohi:

![JSON tuzilmasi izohi ilustratsiyasi](/img/belajar-json-pada-python.jpg)

Python'da JSON bilan ishlash uchun standard `json` paketi bor.

### JSON modulini import qilish

Python'da JSON ishlatish uchun `json` modulini import qiling:

```python
import json
```

### JSON parse qilish (JSON -> Python)

Agar sizda JSON string bo'lsa, uni `json.loads()` yordamida parse qilishingiz mumkin. Natija Python dictionary bo'ladi.

```python
import json

# JSON ma'lumot:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# x ni parse qilish:
y = json.loads(x)

# natija Python dictionary:
print(y["age"])
```

### Python'dan JSON'ga o'tkazish (Python -> JSON)

Agar sizda Python obyekt bo'lsa, uni `json.dumps()` yordamida JSON string'ga aylantirishingiz mumkin.

```python
import json

# Python obyekt (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# JSON ga aylantirish:
y = json.dumps(x)

# natija JSON string:
print(y)
```

Quyidagi Python turlarini JSON string'ga aylantirish mumkin:
* dict
* list
* tuple
* string
* int
* float
* `True`
* `False`
* `None`

### Natijani formatlash

Yuqoridagi misolda JSON string chiqadi, lekin indentation va line break'lar bo'lmagani uchun o'qish qiyin bo'lishi mumkin.

`json.dumps()` metodida natijani o'qilishi oson qilish uchun parametrlar bor:

```python
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# natijani o'qilishi oson qilish uchun 4 ta indentdan foydalanish:
print(json.dumps(x, indent=4))
```

Separator'larni ham sozlash mumkin. Default qiymat (`, ` va `: `): object'larni vergul+bo'sh joy bilan, key-value'ni esa ikki nuqta+bo'sh joy bilan ajratadi:

```python
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# kalitlar bo'yicha tartiblab chiqarish:
print(json.dumps(x, indent=4, sort_keys=True))
```

JSON internetdan data olish (API) yoki ilovalar orasida ma'lumot almashish uchun juda ko'p ishlatiladi. Shuning uchun Python'da JSON bilan ishlashni tushunish muhim.

