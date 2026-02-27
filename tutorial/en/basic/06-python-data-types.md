---
layout: tutorial.njk
title: Python Data Types
order: 6
permalink: /tutorial/en/python-data-types/
---

<img src="/img/tutorial/6-tipe-data-pada-python.webp" alt="Python Data Types" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Data type is a medium or memory on the computer used to hold information.

Python itself has quite unique data types if we compare it with other programming languages.

Here are the data types of the Python programming language:

| Data Type | Example | Explanation |
| ----------- | ------------------------ | ------------------------------------------------------------------------------------ |
| Boolean | `True` or `False` | Declares true `True` which has value `1`, or false `False` which has value `0` |
| String | `"Let's learn Python"` | Declares characters/sentences can be numbers, letters etc. (flanked by `"` or `'`) |
| Integer | `25` or `1209` | Declares integers |
| Float | `3.14` or `0.99` | Declares numbers that have decimal points |
| Hexadecimal | `0x9a` or `0x1d3` | Declares numbers in hex format (base 16 numbers) |
| Complex | `1 + 5j ` | Declares pairs of real and imaginary numbers |
| List | `['xyz', 786, 2.23]` | Sequence data that stores various data types and its contents can be changed |
| Tuple | `('xyz', 768, 2.23)` | Sequence data that stores various data types but its contents cannot be changed |
| Set | `{'apple', 'orange'}` | Unordered collection of unique data and cannot have duplicates |
| Dictionary | `{'name': 'adi','id':2}` | Sequence data that stores various data types in the form of key and value pairs |

To try various kinds of data types, please try the Python script below.

```python
#Boolean data type
print(True)

#String data type
print("Let's learn Python")
print('Learning Python is Very Easy')

#Integer data type
print(20)

#Float data type
print(3.14)

#Hexadecimal data type
print(0x9a)

#Complex data type
print(5j)

#List data type
print([1,2,3,4,5])
print(["one", "two", "three"])

#Tuple data type
print((1,2,3,4,5))
print(("one", "two", "three"))

#Set data type
print({1,2,3,4,5})
print({"apple", "orange", "mango"})

#Dictionary data type
print({"name":"Bob", 'age':20})
#Dictionary data type checked into profile variable
profile = {"name":"Alice", 'age':21} #process initialization of profile variable
print(profile) #process printing profile variable containing Dictionary data type
print(type(profile)) #function to check data type kind. will appear <class 'dict'> which means dict is dictionary data type
```
