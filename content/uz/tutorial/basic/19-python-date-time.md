---
layout: tutorial.njk
lang: uz
title: Python sana va vaqt
description: "datetime moduli bilan sana, vaqt va davomiylikni boshqaring: formatlash va parsing bilan."
order: 19
permalink: /uz/tutorial/python-date-time/
---

<img src="/img/tutorial/19-python-date-and-time.webp" alt="Python sana va vaqt" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python dasturlari sana va vaqt bilan bir nechta usulda ishlashi mumkin. Sana formatlari orasida o'zgartirish (conversion) kompyuterlar uchun juda keng tarqalgan vazifa. Python'dagi `time` va `calendar` modullari sana va vaqtni boshqaradi.

### Tick nima?

Time interval — sekund birliklaridagi floating-point son. Vaqtning ma'lum bir nuqtasi 1970-yil 1-yanvar, soat 00:00 dan boshlab sekundlarda ifodalanadi.

Quyida misol:

```python
import time; # time modulini import qilish

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)
```

### Python TimeTuple nima?

Ko'plab Python time funksiyalari vaqtni 9 ta sondan iborat tuple sifatida qayta ishlaydi:

| Index | Maydon | Qiymat |
| ----- | ----------------- | ----------------------------------------- |
| 0 | 4 xonali yil | 2008 |
| 1 | Oy | 1 dan 12 gacha |
| 2 | Kun | 1 dan 31 gacha |
| 3 | Soat | 0 dan 23 gacha |
| 4 | Daqiqa | 0 dan 59 gacha |
| 5 | Sekund | 0 dan 61 gacha |
| 6 | Haftaning kuni | 0 dan 6 gacha (0 — dushanba) |
| 7 | Yilning kuni | 1 dan 366 gacha |
| 8 | Daylight savings | -1, 0, 1; -1 bo'lsa kutubxona DST'ni o'zi aniqlaydi |

Yuqoridagi tuple `struct_time` tuzilmasiga teng. Bu tuzilma quyidagi atributlarga ega:

| Index | Atribut | Qiymat |
| ----- | ----------- | ----------------------------------------- |
| 0 | `tm_year` | 2008 |
| 1 | `tm_mon ` | 1 dan 12 gacha |
| 2 | `tm_mday` | 1 dan 31 gacha |
| 3 | `tm_hour` | 0 dan 23 gacha |
| 4 | `tm_min ` | 0 dan 59 gacha |
| 5 | `tm_sec ` | 0 dan 61 gacha |
| 6 | `tm_wday` | 0 dan 6 gacha (0 — dushanba) |
| 7 | `tm_yday` | 1 dan 366 gacha |
| 8 | ` tm_isdst` | -1, 0, 1; -1 bo'lsa kutubxona DST'ni o'zi aniqlaydi |

### Hozirgi vaqtni olish

Epoch'dan boshlab sekundlarda berilgan qiymatni time-tuple ko'rinishiga o'tkazish uchun float qiymatni `localtime` kabi funksiyaga bering. Funksiya 9 ta elementdan iborat tuple qaytaradi.

```python
import time;

localtime = time.localtime(time.time())
print("Current local time :", localtime)
```

### Formatlangan vaqtni olish

Vaqtni ehtiyojga qarab formatlash mumkin. O'qilishi oson ko'rinish uchun oddiy usul — `asctime()`.

```python
import time;

localtime = time.asctime(time.localtime(time.time()))
print("Current local time :", localtime)
```

### Oyning kalendarini olish

`calendar` moduli yil va oy kalendarlarini chiqarish uchun turli metodlarni beradi. Bu yerda 2008-yil yanvar kalendarini chiqaramiz.

```python
import calendar

cal = calendar.month(2008, 1)
print("Here is the calendar:")
print(cal)
```

### datetime moduli

`datetime` moduli sana, vaqt va davomiylik bilan bevosita ishlaydi — ularni yaratish, matn ko'rinishida formatlash, matnni qayta parsing qilish va arifmetik amallar bajarish. Kalendar ishlari uchun uni past darajali `time` modulidan afzal ko'ring.

```python
from datetime import datetime, timedelta

# A fixed point in time: year, month, day, hour, minute
moment = datetime(2025, 1, 15, 9, 30)
print(moment)                              # 2025-01-15 09:30:00

# Format a datetime as text with strftime
print(moment.strftime("%d/%m/%Y %H:%M"))   # 15/01/2025 09:30

# Parse text back into a datetime with strptime
parsed = datetime.strptime("2025-01-15 09:30", "%Y-%m-%d %H:%M")
print(parsed == moment)                    # True

# Durations: shift a datetime with timedelta
deadline = moment + timedelta(days=7)
print(deadline)                            # 2025-01-22 09:30:00
```

Hozirgi sana va vaqtni olish uchun `datetime.now()` ni chaqiring.

### Python'dagi time moduli

Python'da vaqt bilan ishlash va turli ko'rinishlar orasida o'zgartirish uchun `time` moduli bor. Quyida time modulidagi funksiyalar ro'yxati:

| Python funksiyasi | Izoh |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `time.altzone` | Lokal DST timezone offset'i (UTC'dan sekundlarda g'arbga). DST yo'q bo'lsa ishlatmang. |
| `time.asctime([tupletime])` | Time-tuple qabul qilib, 'Tue Dec 11 18:07:14 2008' kabi o'qilishi oson string qaytaradi. |
| `time.process_time() ` | Processor vaqtini sekundlarda float sifatida qaytaradi. Hisoblash xarajatlarini o'lchashda `time.time()` dan ko'ra foydaliroq. |
| `time.ctime([secs]) ` | `asctime(localtime(secs))` ga o'xshaydi; argument bo'lmasa `asctime()` kabi. |
| `time.gmtime([secs]) ` | Epoch'dan sekundlarda berilgan qiymatni UTC time-tuple'ga aylantiradi. Eslatma: `t.tm_isdst` doim 0. |
| `time.localtime([secs]) ` | Epoch'dan sekundlarda berilgan qiymatni lokal time-tuple'ga aylantiradi (`tm_isdst` 0 yoki 1 bo'lishi mumkin). |
| `time.mktime(tupletime) ` | Lokal time-tuple qabul qilib, epoch'dan sekundlarda float qaytaradi. |
| `time.sleep(secs) ` | Berilgan sekundlar davomida bajarilishni to'xtatadi. |
| `time.strftime(fmt[,tupletime])` | Time-tuple'ni `fmt` formatiga ko'ra string ko'rinishiga o'tkazadi. |
| `time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')` | `str` ni `fmt` bo'yicha parse qilib time-tuple qaytaradi. |
| `time.time() ` | Hozirgi vaqtni epoch'dan sekundlarda float sifatida qaytaradi. |

Time modulida yana 2 ta muhim atribut bor:

| Python atributi | Izoh |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| ` time.timezone` | DST'siz lokal timezone'ning UTC'dan offset'i (sekundlarda). |
| `time.tzname ` | Lokal timezone nomlari juftligi (DST'siz va DST bilan). |

### Python'dagi calendar moduli

`calendar` moduli kalendar bilan bog'liq funksiyalarni taqdim etadi, jumladan oy yoki yil uchun matn ko'rinishidagi kalendar chiqarish.

Standart holatda hafta dushanbadan boshlanadi, yakshanba bilan tugaydi. Buni o'zgartirish uchun `calendar.setfirstweekday()` funksiyasini chaqiring.

Quyida calendar modulidagi funksiyalar ro'yxati:

| Python funksiyasi | Izoh |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `calendar.calendar(year,w=2,l=1,c=6)` | `year` uchun uch ustunli ko'p qatorli string kalendar qaytaradi. `w` — sana kengligi, `l` — har hafta uchun qatorlar, `c` — ustunlar oralig'i. |
| `calendar.firstweekday( ) ` | Haftaning boshlanish kunini qaytaradi (standart 0, ya'ni dushanba). |
| `calendar.isleap(year) ` | `year` kabisa yili bo'lsa `True`, aks holda `False`. |
| `calendar.leapdays(y1,y2) ` | `(y1, y2)` oralig'idagi kabisa kunlar sonini qaytaradi. |
| `calendar.month(year,month,w=2,l=1) ` | Berilgan oy/yil uchun ko'p qatorli string kalendar qaytaradi. |
| `calendar.monthcalendar(year,month)` | Oy uchun haftalar ro'yxatini qaytaradi; oydan tashqaridagi kunlar 0 bo'ladi. |
| `calendar.monthrange(year,month)` | (1) oy boshidagi haftakuni kodi, (2) oydagi kunlar sonini qaytaradi. |
| `calendar.setfirstweekday(weekday)` | Haftaning birinchi kunini `weekday` ga o'rnatadi (0 — dushanba, 6 — yakshanba). |
| `calendar.timegm(tupletime) ` | `time.gmtime` ning teskarisi: time-tuple'ni epoch sekundiga o'tkazadi. |
| `calendar.weekday(year,month,day)` | Berilgan sana uchun haftakuni kodini qaytaradi. |
