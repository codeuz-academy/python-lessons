---
layout: tutorial.njk
title: Python Installation
order: 2
permalink: /tutorial/en/python-installation/
---

<img src="/img/tutorial/2-panduan-cepat-instalasi-python-windows-linux-mac.webp" alt="Python Installation Guide" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Before writing Python programs, install Python and verify that your terminal can run it.

This tutorial targets **Python 3.13**.

### Linux

Most Linux distributions already include Python 3. Check first:

```bash
python3 --version
```

If Python is missing or too old, install from your distro package manager or from [python.org source releases](https://www.python.org/downloads/source/).

Common package-manager examples:

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Fedora
sudo dnf install python3 python3-pip

# Arch Linux
sudo pacman -S python python-pip
```

### Windows

1. Open [Python releases for Windows](https://www.python.org/downloads/windows/).
2. Download a Python 3.13 installer (64-bit unless you need 32-bit).
3. Run the installer.
4. **Enable "Add python.exe to PATH"** before clicking Install.

Verify installation in Command Prompt or PowerShell:

```bash
python --version
```

### macOS

1. Open [Python releases for macOS](https://www.python.org/downloads/macos/).
2. Download and run the Python 3.13 installer.
3. Complete the installation wizard.

Verify installation in Terminal:

```bash
python3 --version
```

If you use Homebrew, you can also install Python with:

```bash
brew install python
```

### Verify `pip`

`pip` is usually installed with Python. Check with:

```bash
python -m pip --version
# or
python3 -m pip --version
```

If both Python and pip commands work, your environment is ready for the next tutorial.
