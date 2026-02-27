---
layout: tutorial.njk
lang: en
title: Python Variables
order: 7
permalink: /en/tutorial/python-variables/
---

<img src="/img/tutorial/7-variabel-pada-python.webp" alt="Python Variables" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Variables are memory locations reserved to store values. This means that when you create a variable you reserve some space in memory. Variables store data carried out during program execution, where later the contents of these variables can be changed by certain operations on the program that uses variables.

Variables can store various kinds of data types. In Python programming, variables have dynamic properties, meaning Python variables do not need to be declared with a specific data type and Python variables can be changed when the program runs.

Writing Python variables itself also has certain rules, namely:

1. The first character must be a letter or underscore `_`
2. The next character can be a letter, underscore `_` or number
3. Characters in variable names are case-sensitive. This means lowercase and uppercase letters are distinguished. For example, the variable `firstName` and `firstname` are different variables.

To start creating variables in Python it is very easy, you simply write the variable then fill it with a value by adding an equal sign `=` followed by the value you want to enter.

**Creating and printing a variable**

```python
name = "John Doe"
print(name)
```

**Changing value and data type**

Variables can change their value and even their type during execution:

```python
age = 20
print(age)
print(type(age))

age = "twenty one"
print(age)
print(type(age))
```

**Combining variables**

```python
first_name = "Bob"
last_name = "Smith"
full_name = first_name + " " + last_name

age = 22
hobby = "Swimming"

print("Name:", full_name)
print("Age:", age)
print("Hobby:", hobby)
```

**Valid variable names**

```python
my_variable = "Hello"
_private = "Hi"
count2 = 100
print(my_variable, _private, count2)
```

**Using variables in calculations**

```python
length = 10
width = 5
area = length * width
print("Area:", area)
```
