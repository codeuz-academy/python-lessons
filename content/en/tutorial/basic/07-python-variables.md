---
layout: tutorial.njk
lang: en
title: Python Variables
description: "How Python variables work as names bound to objects, plus naming rules and assignment shortcuts."
order: 7
permalink: /en/tutorial/python-variables/
---

<img src="/img/tutorial/7-python-variables.webp" alt="Python Variables" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

A variable is a name that points to a value stored in memory. When you assign a value to a variable, Python sets aside space for it, and you can read or change that value as the program runs.

Python variables are dynamically typed: you don't declare a type up front, and the same name can point to a number now and a string later.

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
