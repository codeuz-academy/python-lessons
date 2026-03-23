---
layout: tutorial.njk
lang: en
title: Pip & Package Management Python
description: "Learn Pip & Package Management Python in Python with practical examples and clear explanations."
order: 32
permalink: /en/tutorial/python-pip-package/
---

<img src="/img/tutorial/32-python-pip-packages.webp" alt="Python Pip and Packages" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

`pip` is the standard package manager for Python. You use it to install, upgrade, and remove third-party libraries.
In day-to-day work, `pip` is used together with `venv` so project dependencies stay isolated and reproducible.

### What is a Package?

A package is a distributable set of Python modules and metadata, usually published on [PyPI](https://pypi.org/).

### Check if `pip` is Installed

```bash
# Windows (py launcher)
py -m pip --version

python -m pip --version
# or
python3 -m pip --version
```

Using `python -m pip` is recommended because it targets the same Python interpreter you run.
Run these commands inside your project virtual environment whenever possible.

### Installing Packages

```bash
python -m pip install requests
```

Install a specific version when you need stable behavior:

```bash
python -m pip install requests==2.32.3
```

### Upgrading Packages

```bash
python -m pip install --upgrade requests
```

You can also install optional extras:

```bash
python -m pip install "requests[socks]"
```

### Using Installed Packages

<div class="warning">This snippet requires the <code>requests</code> package to be installed first.</div>

```python
# non-runnable: requires external environment/setup
import requests

response = requests.get("https://belajarpython.com", timeout=10)
print(response.status_code)
```

### Viewing Installed Packages

```bash
python -m pip list
```

### Removing Packages

```bash
python -m pip uninstall requests
```

### Searching and Inspecting Packages

- Search at [PyPI](https://pypi.org/)
- Inspect package details:

```bash
python -m pip show requests
```

### Reproducible Dependencies

```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

`pip freeze` captures exact installed versions, which helps avoid "works on my machine" issues.

### Common Errors

- Installing globally instead of in `.venv`, causing project mismatch later.
- Running `pip` from a different Python installation than the one used to run the app.
- Version conflicts between packages (resolve by pinning compatible versions).
- Missing quotes for extras in some shells (`"package[extra]"`).

### What Now?

After learning basic packaging workflow, continue with:

- Python Standard Library docs: [https://docs.python.org/3.13/library/](https://docs.python.org/3.13/library/)
- Python Language Reference: [https://docs.python.org/3.13/reference/](https://docs.python.org/3.13/reference/)
- Official Python Tutorial index: [https://docs.python.org/3.13/tutorial/](https://docs.python.org/3.13/tutorial/)

Keep practicing by building small projects, isolating each project with `venv`, and pinning dependencies with `requirements.txt`.
