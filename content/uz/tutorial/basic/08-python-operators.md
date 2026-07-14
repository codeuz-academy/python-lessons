---
layout: tutorial.njk
lang: uz
title: Python operatorlar
description: "Arifmetik, taqqoslash, mantiqiy va belgilash operatorlari hamda ko'pchilikni adashtiradigan ustuvorlik qoidalari."
order: 8
permalink: /uz/tutorial/python-operators/
---

<img src="/img/tutorial/8-python-operators.webp" alt="Python operatorlari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Operatorlar operand (qiymat)lar ustida amallar bajarishga xizmat qiladigan konstruksiyalardir.

Masalan, 3 + 2 = 5 amali. Bu yerda `3` va `2` — operandlar, `+` esa operator.

Python dasturlash tili turli operatorlarni qo'llab-quvvatlaydi, jumladan:

- [Arifmetik operatorlar](#arithmetic-operators)
- [Taqqoslash (relational) operatorlari](#comparison-operators)
- [Tayinlash (assignment) operatorlari](#assignment-operators)
- [Mantiqiy operatorlar](#logical-operators)
- [Bitwise operatorlar](#bitwise-operators)
- [A'zolik operatorlari](#membership-operators)
- [Identity operatorlar](#identity-operators)

### Arifmetik operatorlar <a name="arithmetic-operators"></a>

| Operator | Misol | Izoh |
| -------------------- | ------------- | ---------------------------------------------------------------------------------------------------------- |
| Qo'shish `+` | `1 + 3 = 4` | Operand qiymatlarini qo'shadi |
| Ayirish `-` | `4 - 1 = 3` | Chap operand qiymatidan o'ng operand qiymatini ayiradi |
| Ko'paytirish `*` | `2 * 4 = 8` | Operandlarni ko'paytiradi |
| Bo'lish `/` | `10 / 5 = 2.0` | Chap operandni o'ng operandga bo'ladi |
| Qoldiq `%` | `11 % 2 = 1` | Bo'lishdan qolgan qoldiqni qaytaradi |
| Daraja `**` | `8 ** 2 = 64` | Chap operandni o'ng operand darajasiga ko'taradi |
| Floor bo'lish `//` | `10 // 3 = 3` | Bo'lish, lekin kasr qismi tashlab yuboriladi |

**Qo'shish** (`+`)

```python
print(13 + 2)
apple = 7
orange = 9
fruit = apple + orange
print(fruit)
```

**Ayirish** (`-`)

```python
debt = 10000
pay = 5000
remaining_debt = debt - pay
print("Qolgan qarz:", remaining_debt)
```

**Ko'paytirish** (`*`)

```python
length = 15
width = 8
area = length * width
print("Yuza:", area)
```

**Bo'lish** (`/`)

```python
cake = 16
children = 4
cake_per_child = cake / children
print("Har bir bolaga:", cake_per_child)
```

**Qoldiq** (`%`)

```python
print(14 % 5)
print(10 % 3)
print(20 % 4)
```

**Daraja** (`**`)

```python
print(8 ** 2)
print(2 ** 10)
print(5 ** 3)
```

**Floor bo'lish** (`//`)

```python
print(10 // 3)
print(7 // 2)
print(-10 // 3)
```

### Taqqoslash (relational) operatorlari <a name="comparison-operators"></a>

Taqqoslash operatorlari har bir operand qiymatini solishtirish uchun ishlatiladi.

| Operator | Misol | Izoh |
| --------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------- |
| Teng `==` | `1 == 1` | Operandlar qiymati teng bo'lsa `True` bo'ladi. |
| Teng emas `!=` | `2 != 2` | Teng bo'lmasa `True`, teng bo'lsa `False`. |
| Katta `>` | `5 > 3` | Chap operand o'ng operanddan katta bo'lsa `True`. |
| Kichik `<` | `5 < 3` | Chap operand o'ng operanddan kichik bo'lsa `True`. |
| Katta yoki teng `>=` | `5 >= 3` | Chap operand katta yoki teng bo'lsa `True`. |
| Kichik yoki teng `<=` | `5 <= 3` | Chap operand kichik yoki teng bo'lsa `True`. |

Quyida Python'da taqqoslash operatorlaridan foydalanish misoli:

```python
# Teng
print(1 == 1)  # True
print(1 == 2)  # False

# Teng emas
print(2 != 2)  # False
print(2 != 3)  # True

# Katta
print(5 > 3)   # True

# Kichik
print(5 < 3)   # False

# Katta yoki teng
print(5 >= 3)  # True

# Kichik yoki teng
print(5 <= 3)  # False
```

### Tayinlash (assignment) operatorlari <a name="assignment-operators"></a>

Tayinlash operatorlari o'zgaruvchiga qiymat berish yoki uni yangilash uchun ishlatiladi.

| Operator | Misol | Izoh |
| --------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Teng `=` | `a = 1` | O'ng tomondagi qiymatni chap tomondagi o'zgaruvchiga beradi. |
| Qo'shib tayinlash `+=` | `a += 2` | O'zgaruvchiga o'z qiymati + o'ng tomondagi qiymatni beradi. |
| Ayirib tayinlash `-=` | `a -= 2` | O'zgaruvchiga o'z qiymatidan o'ng tomondagi qiymat ayirilgan natijani beradi. |
| Ko'paytirib tayinlash `*=` | `a *= 2` | O'zgaruvchiga o'z qiymati * o'ng tomondagi qiymatni beradi. |
| Bo'lib tayinlash `/=` | `a /= 4` | O'zgaruvchiga o'z qiymati / o'ng tomondagi qiymatni beradi. |
| Qoldiq bilan tayinlash `%=` | `a %= 3` | O'zgaruvchiga bo'lishdan qolgan qoldiq qiymatini beradi. |
| Darajaga tayinlash `**=` | `a **= 3` | O'zgaruvchiga o'z qiymatini darajaga ko'tarilgan holatini beradi. |
| Floor bo'lib tayinlash `//=` | `a //= 3` | Floor bo'lish natijasini chap operandga qayta tayinlaydi. |

```python
x = 10
print("x =", x)

x += 5
print("x += 5 ->", x)

x -= 3
print("x -= 3 ->", x)

x *= 2
print("x *= 2 ->", x)

x //= 4
print("x //= 4 ->", x)
```

### Mantiqiy operatorlar <a name="logical-operators"></a>

Mantiqiy operatorlar shartli ifodalarni birlashtirish uchun ishlatiladi.

| Operator | Misol | Izoh |
| -------- | --------------------- | ------------------------------------------------------------ |
| `and` | `True and False` | Ikkala shart ham `True` bo'lsa `True` qaytaradi |
| `or` | `True or False` | Kamida bitta shart `True` bo'lsa `True` qaytaradi |
| `not` | `not True` | Natijani teskarisiga o'zgartiradi |

```python
print(True and False)
print(True or False)
print(not True)

x = 10
print(x > 5 and x < 20)
print(x > 5 or x > 20)
print(not(x > 5 and x < 20))
```

### Bitwise operatorlar <a name="bitwise-operators"></a>

Bitwise operatorlar butun sonlarning alohida bitlari ustida amallar bajaradi.

| Operator | Nomi | Misol | Izoh |
| -------- | ----------- | ----------- | ------------------------------------------------- |
| `&` | AND | `10 & 4` | Ikkala bit ham 1 bo'lsa 1 qo'yadi |
| `\|` | OR | `10 \| 4` | Kamida bitta bit 1 bo'lsa 1 qo'yadi |
| `^` | XOR | `10 ^ 4` | Faqat bitta bit 1 bo'lsa 1 qo'yadi |
| `~` | NOT | `~10` | Barcha bitlarni teskari qiladi |
| `<<` | Chapga surish | `10 << 2` | Bitlarni chapga suradi |
| `>>` | O'ngga surish | `10 >> 2` | Bitlarni o'ngga suradi |

```python
a = 10  # ikkilik: 1010
b = 4   # ikkilik: 0100

print(a & b)    # 0 (AND)
print(a | b)    # 14 (OR)
print(a ^ b)    # 14 (XOR)
print(~a)       # -11 (NOT)
print(a << 2)   # 40 (chapga surish)
print(a >> 2)   # 2 (o'ngga surish)
```

### A'zolik operatorlari <a name="membership-operators"></a>

A'zolik operatorlari qiymat ketma-ketlikda (`string`, `list`, `tuple`) mavjudligini tekshirish uchun ishlatiladi.

| Operator | Misol | Izoh |
| ---------- | ----------------------- | ---------------------------------------------------------------- |
| `in` | `"a" in "apple"` | Qiymat ketma-ketlikda topilsa `True` qaytaradi |
| `not in` | `"b" not in "apple"` | Qiymat ketma-ketlikda **topilmasa** `True` qaytaradi |

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("mango" in fruits)
print("mango" not in fruits)
```

### Identity operatorlar <a name="identity-operators"></a>

Identity operatorlar ikki o'zgaruvchi xotirada bir xil obyektga ishora qilishini tekshiradi (faqat qiymat emas, balki obyektning o'zi).

| Operator | Misol | Izoh |
| ---------- | ----------- | ---------------------------------------------------------------- |
| `is` | `a is b` | Ikkala o'zgaruvchi bir xil obyektga ishora qilsa `True` qaytaradi |
| `is not` | `a is not b`| Ikkala o'zgaruvchi **turli** obyektlarga ishora qilsa `True` qaytaradi |

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a == c)
print(a is not c)
```

### Python'da operatorlar ustuvorligi

Yuqoridagi operatorlarning har birida ustuvorlik (prioritet) bor: avval yuqori prioritetdagilar bajariladi, keyin qolganlari.

| Operator | Tavsif |
| --------------------------------- | ------------------------ |
| `**` | Arifmetik |
| `~, +, -` | Bitwise |
| `*, /, %, //` | Arifmetik |
| `+, -` | Arifmetik |
| `>>, <<` | Bitwise |
| `&` | Bitwise |
| `^` | Bitwise |
| `<=, <, >, >=` | Taqqoslash |
| `==, !=` | Taqqoslash |
| `=, %=, /=, //=, -=, +=, *=, **=` | Tayinlash |
| `is, is not` | Identity |
| `in, not in` | A'zolik |
| `not, or, and` | Mantiqiy |
