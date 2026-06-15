---
layout: tutorial.njk
lang: uz
title: Python modullar (modules)
description: "Kodni modullar va paketlarga bo'ling va import ularni aslida qanday topishini tushuning."
order: 22
permalink: /uz/tutorial/python-modules/
---

<img src="/img/tutorial/22-python-modules.webp" alt="Python modullari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Modul - bu Python fayli (`.py`) bo'lib, ichida funksiyalar, class'lar va o'zgaruvchilar bo'ladi. Siz ularni boshqa fayllarda qayta ishlatishingiz mumkin.
Modullar katta dasturlarni kichik, aniq vazifali fayllarga bo'lishga yordam beradi va takroriy kodni kamaytiradi.

### Oddiy modul yaratish

`support.py` faylini yarating:

```python
def print_func(name):
    print(f"Hello: {name}")
```

Modul nomlarini sodda qiling (`support.py`, `math_utils.py`) va fayl nomida tire/bo'sh joy ishlatmang.

### Import operatori

Modulni yuklash uchun `import` dan foydalaning:

```python
# non-runnable: requires external environment/setup
import support

support.print_func("Andy")
```

`import support` orqali chaqiriladigan funksiyalar `support.` prefiksi ostida qoladi (nomlar makoni / namespace) va har bir funksiya qayerdan kelganini aniq ko'rsatadi.

### Keng tarqalgan import variantlari

```python
# non-runnable: requires external environment/setup
from support import print_func
print_func("Bob")

import support as sp
sp.print_func("Carol")
```

Faqat bir nechta nom kerak bo'lsa `from module import name` ishlating. `from x import *` (yulduzcha bilan import) dan qoching, chunki u kodni o'qish va nosozliklarni topishni (debug) qiyinlashtiradi.

### Modul qidirish yo'li (module search path)

`import module_name` ishlaganda Python quyidagilardan qidiradi:

1. Hozirgi skript papkasi
2. `PYTHONPATH` dagi yo'llar
3. Standard library (standart kutubxona) va site-packages

Joriy qidirish yo'llarini (path) ko'rish:

```python
import sys
print(sys.path)
```

Agar `ModuleNotFoundError` ko'rsangiz, skriptni loyiha ildiz papkasidan (root) ishga tushiring va modul fayli shu yo'llardan birida borligini tekshiring.

### `__name__ == "__main__"`

Modul to'g'ridan-to'g'ri ishga tushirilganda va import qilinganda turlicha ishlashi mumkin:

```python
def main():
    print("Run as script")

if __name__ == "__main__":
    main()
```

- To'g'ridan-to'g'ri ishga tushirish: `python support.py` -> `main()` ishlaydi
- Boshqa fayldan import qilinganda: `main()` avtomatik ishga tushmaydi

### Paketlar (packages)

Paket - bog'liq modullarni bitta papka ichida guruhlash usuli.

Masalan:

```text
project/
  app.py
  helpers/
    __init__.py
    math_utils.py
```

Ishlatish:

```python
# non-runnable: requires external environment/setup
from helpers.math_utils import add
```

`__init__.py` papkani paket (package) sifatida belgilaydi va import'larni barqaror aniqlashga (resolve) yordam beradi.

### Modul a'zolarini ko'rish

Moduldagi export qilingan nomlarni ko'rish uchun `dir()` dan foydalaning:

```python
import math
print(dir(math))
```

### Ko'p uchraydigan xatolar

- `ModuleNotFoundError`: noto'g'ri ishchi papka (working directory) yoki modul yo'li (path).
- `ImportError`: aylanma import (circular import) yoki kerakli nom export qilinmagan.
- Nom to'qnashuvi: faylingiz standart/uchinchi tomon modul nomi bilan bir xil (masalan `random.py`).
