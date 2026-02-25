---
layout: tutorial.njk
title: Pip & Package Management Python
order: 32
permalink: /tutorial/python-pip-package/
---

<img src="/img/tutorial/28-cara-pip-di-python.webp" alt="Python Pip and Packages" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Pip is the standard package manager for Python. Imagine Pip like an "App Store" (App Store or Play Store) specifically for Python programming language, where you can download and install thousands of additional modules created by the Python community worldwide.

For beginners, Pip is the gateway to Python's greatness. For example, if you want to create beautiful charts, perform complex data analysis, or even create a website, you don't need to write everything from scratch. You simply use Pip to install ready-made "packages", and you can immediately focus on building your application.

### What is a Package?

A Package contains all the files you need for a module. A module is a Python code library that you can include in your project.

### Check if Pip is Installed

Pip is usually installed along with Python. To check if pip is installed, run the following command in terminal:

```bash
pip --version
```

### Installing Packages

Installing packages is very easy. Simply use the `install` command followed by the package name. For example we will install a popular package named `requests`:

```bash
pip install requests
```

### Using Packages

Once the package is installed, you can use it in your Python code with the `import` command:

```python
import requests

x = requests.get('https://belajarpython.com')
print(x.status_code)
```

### Viewing Installed Packages List

Use the `list` command to see all packages that already exist in your system or environment:

```bash
pip list
```

### Removing Packages

If you no longer need a package, you can uninstall it:

```bash
pip uninstall requests
```

### Searching Packages on PyPI

All Python packages are centrally managed at the [PyPI (Python Package Index)](https://pypi.org/) site. You can search for thousands of useful packages there before installing them using Pip.
