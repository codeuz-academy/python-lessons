---
layout: tutorial.njk
lang: uz
title: Python operatorlari
order: 8
permalink: /uz/tutorial/python-operators/
---

<img src="/img/tutorial/8-operator-pada-python.webp" alt="Python operatorlari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Operatorlar operand (qiymat)lar ustida amallar bajarishga xizmat qiladigan konstruksiyalardir.

Masalan, 3 + 2 = 5 amali. Bu yerda `3` va `2` - operandlar, `+` esa operator.

Python dasturlash tili turli operatorlarni qo'llab-quvvatlaydi, jumladan:

- [Arifmetik operatorlar](#arithmetic-operators)
- [Taqqoslash (relational) operatorlari](#comparison-operators)
- [Tayinlash (assignment) operatorlari](#assignment-operators)
- [Mantiqiy operatorlar](#logical-operators)
- [Bitwise operatorlar](#bitwise-operators)
- [Membership operatorlar](#membership-operators)
- [Identity operatorlar](#identity-operators)

### Arifmetik operatorlar <a name="arithmetic-operators"></a>

| Operator | Misol | Izoh |
| -------------------- | ------------- | ---------------------------------------------------------------------------------------------------------- |
| Qo'shish `+` | `1 + 3 = 4` | Operand qiymatlarini qo'shadi |
| Ayirish `-` | `4 - 1 = 3` | Chap operand qiymatidan o'ng operand qiymatini ayiradi |
| Ko'paytirish `*` | `2 * 4 = 8` | Operandlarni ko'paytiradi |
| Bo'lish `/` | `10 / 5 = 2` | Chap operandni o'ng operandga bo'ladi |
| Qoldiq `%` | `11 % 2 = 1` | Bo'lishdan qolgan qoldiqni qaytaradi |
| Daraja `**` | `8 ** 2 = 64` | Chap operandni o'ng operand darajasiga ko'taradi |
| Floor bo'lish `//` | `10 // 3 = 3` | Bo'lish, lekin kasr qismi tashlab yuboriladi |

Quyida Python'da arifmetik operatorlardan foydalanish misoli:

```python
#ARITHMETIC OPERATORS

#Addition
print(13 + 2)
apple = 7
orange = 9
fruit = apple + orange #
print(fruit)

#Subtraction
debt = 10000
pay = 5000
remainingDebt = debt - pay
print("Your remaining debt is ", remainingDebt)

#Multiplication
length = 15
width = 8
area = length * width
print(area)

#Division
cake = 16
child = 4
cakePerChild = cake / child
print("Each child will get cake parts as much as ", cakePerChild)

#Modulus
number1 = 14
number2 = 5
result = number1 % number2
print("Remainder of division from number ", number1, " and ", number2, " is ", result)

#Exponent
number3 = 8
number4 = 2
resultExponent = number3 ** number4
print(resultExponent)

#Floor Division
print(10//3)
#10 divided by 3 is 3.3333. Because it is rounded down it will produce value 3
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
# EQUAL TO
print(1 == 1) # Result will be True because one equals one
print(1 == 2) # Result will be False because one does not equal two

# NOT EQUAL TO
print(2 != 2) # Result will be False because two should be equal to two
print(2 != 3) # Result will be True because two is not equal to three

# GREATER THAN
print(5 > 3) # Result will be True because five is greater than three

# LESS THAN
print(5 < 3) # Result will be False because five is not smaller than three

# GREATER THAN OR EQUAL TO
print(5 >= 3) # Result will be True because five is greater than or equal to three

# LESS THAN OR EQUAL TO
print(5 <= 3) # Result will be False because five is not smaller than or equal to three
```

### Tayinlash (assignment) operatorlari <a name="assignment-operators"></a>

Tayinlash operatorlari o'zgaruvchiga qiymat berish yoki uni yangilash uchun ishlatiladi.

| Operator | Misol | Izoh |
| --------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Teng `=` | `a = 1` | O'ng tomondagi qiymatni chap tomondagi o'zgaruvchiga beradi. |
| Qo'shib tayinlash `+=` | `a += 2` | O'zgaruvchiga o'z qiymati + o'ng tomondagi qiymatni beradi. |
| Ayirib tayinlash `-=` | `a -= 2` | O'zgaruvchiga o'z qiymati - o'ng tomondagi qiymatni beradi. |
| Ko'paytirib tayinlash `*=` | `a *= 2` | O'zgaruvchiga o'z qiymati * o'ng tomondagi qiymatni beradi. |
| Bo'lib tayinlash `/=` | `a /= 4` | O'zgaruvchiga o'z qiymati / o'ng tomondagi qiymatni beradi. |
| Qoldiq bilan tayinlash `%=` | `a %= 3` | O'zgaruvchiga bo'lishdan qolgan qoldiq qiymatini beradi. |
| Darajaga tayinlash `**=` | `a **= 3` | O'zgaruvchiga o'z qiymatini darajaga ko'tarilgan holatini beradi. |
| Floor bo'lib tayinlash `//=` | `a //= 3` | Floor bo'lish natijasini chap operandga qayta tayinlaydi. |

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
| `in, not in` | Membership |
| `not, or, and` | Mantiqiy |

