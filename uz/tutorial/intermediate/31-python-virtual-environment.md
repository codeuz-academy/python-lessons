---
layout: tutorial.njk
lang: uz
title: Python virtual environment'lar (venv)
order: 31
permalink: /uz/tutorial/python-virtual-environment/
---

<img src="/img/tutorial/27-tutorial-virtual-environtment-python.webp" alt="Python virtual environment" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Virtual environment - bu bitta loyiha uchun ajratilgan (isolated) Python muhiti. U turli loyihalar orasidagi dependency conflict'larni oldini oladi.
Amaliyotda har bir loyiha uchun alohida environment ishlating, shunda har bir loyiha o'zining package versiyalarini mustaqil saqlaydi.

### Nega virtual environment muhim?

Jamoa va production muhitda virtual environment - deyarli standart talab:

- **Reproducibility**: jamoa a'zolari va CI serverlar `requirements.txt` orqali aynan bir xil dependency'larni qayta tiklay oladi.
- **Isolation**: bitta loyiha uchun package o'rnatish/yangilash, o'sha kompyuterdagi boshqa loyihalarni buzmaydi.
- **Deployment**: production server'ga chiqarishda global o'rnatmalarga tayanmasdan, kerakli package'lar ro'yxatini aniq berasiz.

Virtual environment bo'lmasa, loyihalar orasidagi versiya ziddiyatlarini topish va hal qilish qiyinlashadi.

### Built-in modul: `venv`

Python standard library'da `venv` bor.
Bu default va eng portable yondashuv.

#### 1. Virtual environment yaratish

```bash
# Windows
py -m venv .venv
python -m venv .venv

# macOS / Linux
python3 -m venv .venv
```

#### 2. Environment'ni aktivlashtirish

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (cmd)
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate
```

Aktivlashtirgandan so'ng, shell odatda `(.venv)` ni ko'rsatadi.
Faol Python interpreter'ni quyidagicha tekshirish mumkin:

```bash
python -c "import sys; print(sys.executable)"
```

#### 3. Package'larni environment ichida o'rnatish

```bash
python -m pip install requests
python -m pip list
```

Doim aktivlashtirgandan keyin o'rnating, shunda package'lar global Python'ga emas, `.venv` ichiga tushadi.

#### 4. Deactivate

```bash
deactivate
```

Istalgan payt 2-qadamdagi buyruq bilan qayta aktivlashtirishingiz mumkin.

### Dependency'larni saqlash va qayta ishlatish

```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

Bu usul turli kompyuterlarda bir xil o'rnatishni qayta tiklashga yordam beradi.
`requirements.txt` ni version control'ga commit qiling, shunda jamoa a'zolari bir xil dependency set'ni o'rnatadi.

### Ixtiyoriy zamonaviy vosita: `uv`

`uv` environment va package'larni tez ishlash bilan boshqarishi mumkin.

O'rnatish (bir martalik):

```bash
python -m pip install uv
# or on Windows:
py -m pip install uv
```

Batafsil: [uv documentation](https://github.com/astral-sh/uv)

```bash
uv venv
uv pip install requests
```

`venv` - standard library'dagi rasmiy yechim, `uv` esa ixtiyoriy unumdorlik vositasi.

### Ko'p uchraydigan xatolar

- Aktivlashtirishdan oldin package o'rnatish, keyin loyiha ichida import ishlamasligi.
- `python` bilan boshqa interpreter, `pip` bilan boshqa interpreter ishlatib yuborish (shuning uchun `python -m pip` tavsiya etiladi).
- PowerShell'da execution policy sabab activation script bloklanishi.
- Python versiyasi katta yangilangandan keyin environment buzilishi; `.venv` ni o'chirib `python -m venv .venv` bilan qayta yarating.
