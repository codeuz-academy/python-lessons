---
layout: tutorial.njk
lang: uz
title: Python shartlari (if/else)
order: 9
permalink: /uz/tutorial/python-conditions/
---

<img src="/img/tutorial/9-kondisi-if-else-python.webp" alt="Python if else shartlari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

### If sharti

Shartlar (if condition) dastur bajarilishi davomida yuzaga keladigan holatlarni tekshirish va shu holatga qarab qanday amal bajarilishini tanlash uchun ishlatiladi.

Python'da bir nechta shart operatorlari bor: `if`, `else` va `elif`. `if` sharti shart `True` bo'lsa kodni bajaradi.

Agar shart `False` bo'lsa, `if` bloki bajarilmaydi.

Quyida Python'da `if` shartidan foydalanish misoli:

```python
#If condition is a condition that will be executed by program if it is true or TRUE

score = 9

#if condition is true/TRUE then program will execute command below it
if(score > 7):
    print("Nine is Greater Than Seven") # True Condition, Executed

#if condition is false/FALSE then program will not execute command below it
if(score > 10):
    print("Nine is Greater Than Ten") # False Condition, Not Executed
```

Yuqoridagi misolda dastur ishga tushirilsa, birinchi `if` `True` bo'lgani uchun `"Nine is Greater Than Seven"` matni bir marta chiqariladi. Ikkinchi `if` esa `False`, shuning uchun u yerdagi `print(...)` bajarilmaydi.

### If else sharti

If else sharti nafaqat shartga mos bo'lsa nima bajarilishini, balki shartga mos bo'lmasa qaysi kod bajarilishini ham belgilaydi.

If else shartida: shart `True` bo'lsa `if` ichidagi kod ishlaydi, aks holda (`False`) `else` ichidagi kod ishlaydi.

Quyida Python'da if else shartidan foydalanish misoli:

```python
# If else condition is if condition is TRUE then it will be executed generally in if,
# but if it is FALSE then it will be executed code in else

score = 3
# If statement in if is TRUE then if will be executed,
# but if FALSE code in else will be executed.
if(score > 7):
    print("Congratulations You Passed")
else:
    print("Sorry You Did Not Pass")
```

Yuqoridagi misolda `if` sharti `False` bo'lgani uchun dastur `"Sorry You Did Not Pass"` matnini chiqaradi.

### Elif sharti

`elif` - bu `if` shartining davomidir. `elif` orqali bir nechta ehtimoliy holatlardan birini tanlaydigan kod yozish mumkin. `else` bilan o'xshash, farqi shundaki, `elif` bir nechta bo'lishi mumkin.

Quyida Python'da `elif` shartidan foydalanish misoli:

```python
#Example of using elif condition

today = "Sunday"

if(today == "Monday"):
    print("I will go to college")
elif(today == "Tuesday"):
    print("I will go to college")
elif(today == "Wednesday"):
    print("I will go to college")
elif(today == "Thursday"):
    print("I will go to college")
elif(today == "Friday"):
    print("I will go to college")
elif(today == "Saturday"):
    print("I will go to college")
elif(today == "Sunday"):
    print("I will be on vacation")
```

Yuqoridagi misolda dastur `"I will be on vacation"` matnini chiqaradi.

### Match case (Python 3.10+)

Python 3.10 dan boshlab `match-case` orqali **Structural Pattern Matching** mavjud. Bu boshqa tillardagi `switch-case` ga o'xshaydi va uzun `elif` zanjirlarini almashtirish uchun qulay.

```python
# Create match-case example(Python 3.10+)

today = "Sunday"

match today:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("I will go to college")
    case "Saturday":
        print("I will do homework")
    case "Sunday":
        print("I will be on vacation")
    case _:
        print("Invalid day")
```

Pattern matching yanada murakkab ma'lumot tuzilmalarini ham moslashtirish (match) uchun ishlatilishi mumkin:

```python
# Match with data structure
def process_command(command):
    match command.split():
        case ["quit"]:
            print("Exit program")
        case ["hello", name]:
            print(f"Hello, {name}!")
        case ["add", x, y]:
            print(f"Result: {int(x) + int(y)}")
        case _:
            print("Unknown command")

process_command("hello Bob")  # Output: Hello, Bob!
process_command("add 5 3")  # Output: Result: 8
```

### Ternary operator (bir qatorli shart)

Python shartni bir qatorga yozish (conditional expression, ternary operator) ni ham qo'llab-quvvatlaydi:

```python
# Ternary operator
age = 20
status = "Adult" if age >= 18 else "Child"
print(status)  # Output: Adult

# Another example
score = 85
result = "Pass" if score >= 60 else "Fail"
print(result)  # Output: Pass
```

