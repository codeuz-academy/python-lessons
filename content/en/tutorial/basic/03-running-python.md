---
layout: tutorial.njk
lang: en
title: Running Python
description: "Learn Running Python in Python with practical examples and clear explanations."
order: 3
permalink: /en/tutorial/running-python/
---

<img src="/img/tutorial/3-running-python.webp" alt="How to Run Python" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python can be run in two common ways:

1. **Interactive mode (REPL)** for quick experiments.
2. **Script mode** for running `.py` files.

> <i class="fa-solid fa-circle-info" aria-hidden="true"></i> **Note:** You can also run and edit Python code directly on this website in every code snippet interactively.

### Quickstart (By OS)

#### Linux / macOS

1. Open **Terminal**.
2. Check Python is installed:

   ```bash
   python3 --version
   ```

3. Start interactive mode (REPL):

   ```bash
   python3
   ```

4. Run a script file:

   ```bash
   python3 hello.py
   ```

#### Windows

1. Open **PowerShell** or **Command Prompt**.
2. Check Python is installed (try one of these):

   ```bash
   py --version
   # or
   python --version
   ```

3. Start interactive mode (REPL):

   ```bash
   py
   # or
   python
   ```

4. Run a script file:

   ```bash
   py hello.py
   # or
   python hello.py
   ```

### Run Python Interactive Mode (REPL)

Start Python:

```bash
# Linux/macOS
python3

# Windows (recommended if available)
py
```

You will see the `>>>` prompt. Example:

<div class="note">This snippet demonstrates Python's interactive mode (REPL). It will raise a SyntaxError if run as a standard Python script.</div>

```pycon
>>> print("Welcome to Python")
Welcome to Python
>>> 2 + 3
5
```

`>>>` is the REPL prompt, not part of Python syntax. Do not type `>>>` into a `.py` file or the website code editor.

Use this version in files/editors:

```python
print("Welcome to Python")
print(2 + 3)
```

Exit REPL with:

- `exit()`
- <kbd>Ctrl</kbd>+<kbd>D</kbd> (Linux/macOS)
- <kbd>Ctrl</kbd>+<kbd>Z</kbd> then <kbd>Enter</kbd> (Windows)

### Run Python Script File

Create `hello.py`:

```python
print("Learn Python")
print("at belajarpython.com")
```

Run it from terminal:

```bash
# Linux/macOS
python3 hello.py

# Windows
py hello.py
# or: python hello.py
```

### Optional: Run with IDLE on Windows

If you prefer a GUI editor:

1. Open **IDLE (Python 3.x)** from the Start menu.
2. Use the shell window for quick commands (`>>>`).
3. For script files, click **File > New File**.
4. Save the file as `.py`, then run it with **Run > Run Module (F5)**.

![Python Shell Windows](/img/menjalankan-python-windows.png 'Python Shell Windows')

![Python Editor Windows](/img/menjalankan-python-windows-editor.png 'Python Editor Windows')

### Command-Line Arguments

Python passes command-line arguments through `sys.argv`:

```python
import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
```

Run:

```bash
# Linux/macOS
python3 app.py one two

# Windows
py app.py one two
```

### Other Ways to Run Python

Python has a few useful command-line options:

> <i class="fa-solid fa-circle-info" aria-hidden="true"></i> **Note:** In the examples below, replace `python` with `python3` on Linux/macOS, or `py` on Windows.

- Run a short command:

  ```bash
  python -c "print('Hello from -c')"
  ```

- Run a module as a script (recommended pattern):

  ```bash
  python -m pip --version
  python -m venv .venv
  python -m http.server 8000
  ```

- Run a script and stay in interactive mode afterwards:

  ```bash
  python -i app.py
  ```

> <i class="fa-solid fa-lightbulb" aria-hidden="true"></i> **Tip:** On Windows, the `py` launcher can select a specific version:

```bash
py -3.13 --version
py -3.13 -m pip --version
```

### Interactive Editing and History

In many terminals, the REPL supports command history and basic editing:

- Previous commands: Up/Down arrow
- Move cursor in line: Left/Right arrow

### Executable Scripts (Unix-like)

You can make a script directly executable:

```python
#!/usr/bin/env python3
print("Hello from executable script")
```

Then:

```bash
chmod +x hello.py
./hello.py
```

### Source File Encoding

Python 3 uses UTF-8 by default. You can still declare encoding explicitly.

The encoding cookie must be on the **first or second line** of the file. If you use a shebang, put the encoding cookie on line 2:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
name = "learn python"
print(name)
```

Without a shebang, you can keep it on the first line:

```python
# -*- coding: utf-8 -*-
name = "learn python"
print(name)
```
