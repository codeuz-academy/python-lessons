---
layout: tutorial.njk
title: Python File I/O
order: 23
permalink: /tutorial/python-file-io/
---

<img src="/img/tutorial/19-dasar-dasar-io-python.webp" alt="Python File I/O" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Here we will learn all the basic I/O functions available in Python 3. If you want to learn more details, check out standard Python documentation.

### Print

The simplest way to produce output is using the print statement where you can pass zero or more expressions separated by commas. This function converts the expressions you pass into a string and writes the result to standard output as follows:

```python
print("Python is a great programming language")
```

### Reading Keyboard Input

Python 2 has two built-in functions to read data from standard input, which by default comes from the keyboard. These functions are input() and raw_input()

In Python 3, raw_input() function is deprecated. Moreover, input() functions read data from keyboard as string, irrespective of whether it is enclosed with quotes ('' or "") or not.

### Python Input Function

The input([prompt]) function is equivalent to raw_input, except that it assumes the input is a valid Python expression and returns the evaluated result to you.

```python
>>> x = input("something:")
>>> something:10

>>> x
>>> '10'

>>> x = input("something:")
>>> something:'10' #entered data treated as string with or without ''

>>> x
>>> "'10'"
```
