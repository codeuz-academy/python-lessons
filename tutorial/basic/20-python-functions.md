---
layout: tutorial.njk
title: Python Functions
order: 20
permalink: /tutorial/python-functions/
---

<img src="/img/tutorial/17-belajar-fungsi-python-programming.webp" alt="Python Functions" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

### Defining Python Functions

You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

- Function blocks begin with the keyword def followed by the function name and parentheses (()).
- Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
- The first statement of a function can be an optional statement - the documentation string of the function or docstring.
- The code block within every function starts with a colon (:) and is indented.
- The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

Example of function

```python
def printme( str ):
  "This prints a passed string into this function"
  print(str)
  return
```
