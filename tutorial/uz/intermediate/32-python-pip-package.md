---
layout: tutorial.njk
lang: uz
title: Python'da pip va package management
order: 32
permalink: /tutorial/uz/python-pip-package/
---

<img src="/img/tutorial/28-cara-pip-di-python.webp" alt="Python pip va packages" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

`pip` - Python uchun standart package manager. U orqali third-party kutubxonalarni o'rnatasiz, yangilaysiz va o'chirasiz.
Amaliyotda `pip` ko'pincha `venv` bilan birga ishlatiladi: dependency'lar izolyatsiya qilinadi va qayta tiklanadigan (reproducible) bo'ladi.

### Package nima?

Package - bu Python modullari va metadata'ning tarqatiladigan to'plami bo'lib, odatda [PyPI](https://pypi.org/) ga joylanadi.

### `pip` o'rnatilganini tekshirish

```bash
# Windows (py launcher)
py -m pip --version

python -m pip --version
# or
python3 -m pip --version
```

`python -m pip` ishlatish tavsiya etiladi, chunki u siz ishlatayotgan Python interpreter bilan bir xil muhitni nishonga oladi.
Imkon qadar bu buyruqlarni loyiha virtual environment'i ichida bajaring.

### Package o'rnatish

```bash
python -m pip install requests
```

Barqaror (stable) behavior kerak bo'lsa, aniq versiyani o'rnating:

```bash
python -m pip install requests==2.32.3
```

### Package yangilash

```bash
python -m pip install --upgrade requests
```

Optional extras'ni ham o'rnatish mumkin:

```bash
python -m pip install "requests[socks]"
```

### O'rnatilgan package'larni ishlatish

```python
import requests

response = requests.get("https://belajarpython.com", timeout=10)
print(response.status_code)
```

### O'rnatilgan package'larni ko'rish

```bash
python -m pip list
```

### Package o'chirish

```bash
python -m pip uninstall requests
```

### Package qidirish va tekshirish

- [PyPI](https://pypi.org/) da qidiring
- Package detallari:

```bash
python -m pip show requests
```

### Reproducible dependency'lar

```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

`pip freeze` aniq o'rnatilgan versiyalarni yozib beradi va "menda ishlaydi" muammolarini kamaytiradi.

### Ko'p uchraydigan xatolar

- `.venv` o'rniga global o'rnatib yuborish, keyin loyiha muhiti mos kelmay qolishi.
- Ilovada ishlatiladigan Python boshqa, `pip` esa boshqa o'rnatmadan ishlashi.
- Package'lar orasida version conflict (mos versiyalarni pin qilish bilan yechiladi).
- Ba'zi shell'larda extras uchun qo'shtirnoq qo'ymaslik (`"package[extra]"`).

### Keyingi qadamlar

Asosiy package boshqaruv jarayonini o'rganganingizdan so'ng quyidagilarni davom ettiring:

- Python Standard Library docs: [https://docs.python.org/3.13/library/](https://docs.python.org/3.13/library/)
- Python Language Reference: [https://docs.python.org/3.13/reference/](https://docs.python.org/3.13/reference/)
- Official Python Tutorial index: [https://docs.python.org/3.13/tutorial/](https://docs.python.org/3.13/tutorial/)

Amaliyot qilish uchun kichik loyihalar yarating, har birini `venv` bilan ajrating va dependency'larni `requirements.txt` bilan pin qiling.
