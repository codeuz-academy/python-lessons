---
layout: tutorial.njk
title: Python Variables
order: 7
permalink: /tutorial/en/python-variables/
---

<img src="/img/tutorial/7-variabel-pada-python.webp" alt="Python Variables" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Variables are memory locations reserved to store values. This means that when you create a variable you reserve some space in memory. Variables store data carried out during program execution, where later the contents of these variables can be changed by certain operations on the program that uses variables.

Variables can store various kinds of data types. In Python programming, variables have dynamic properties, meaning Python variables do not need to be declared with a specific data type and Python variables can be changed when the program runs.

Writing Python variables itself also has certain rules, namely:

1. The first character must be a letter or underscore `_`
2. The next character can be a letter, underscore `_` or number
3. Characters in variable names are case-sensitive. This means lowercase and uppercase letters are distinguished. For example, the variable `firstName` and `firstname` are different variables.

To start creating variables in Python it is very easy, you simply write the variable then fill it with a value by adding an equal sign `=` followed by the value you want to enter.

Below is an example of using variables in the Python programming language:

```python
#process of entering data into variable
name = "John Doe"
#process of printing variable
print(name)

#value and data type in variable can be changed
age = 20 #initial value
print(age) #print age value
type(age) #check age data type
age = "twenty one" #value after changed
print(age) #print age value
type(age) #check age data type

firstName = "Bob"
lastName = "Smith"
name = firstName + " " + lastName
age = 22
hobby = "Swimming"
print("Profile\n", name, "\n", age, "\n", hobby)

#other variable examples
thisisvariable = "Hello"
this_is_also_variable = "Hi"
_thisisvariablealso = "Hi"
thisisvariable222 = "Bye"

length = 10
width = 5
area = length * width
print(area)
```
