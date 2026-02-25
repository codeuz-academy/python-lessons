---
layout: tutorial.njk
title: Python Modules
order: 22
permalink: /tutorial/python-modules/
---

<img src="/img/tutorial/18-modul-python.webp" alt="Python Modules" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Modules allow you to organize your Python code logically. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference.

Simply put, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.

Here is an example of a simple Python module:

```python
def print_func(par):
  print("Hello : ", par)
  return
```

### Import Statement

You can use any Python source file as a module by executing an import statement in some other Python source file. The import has the following syntax:

When the interpreter encounters an import statement, it imports the module if the module is present in the search path. A search path is a list of directories that the interpreter searches before importing a module. For example, to import the module hello.py, you need to put the following command at the top of the script:

```python
# Import module support
import support

# You can call defined function as follows
support.print_func("Andy")
```
