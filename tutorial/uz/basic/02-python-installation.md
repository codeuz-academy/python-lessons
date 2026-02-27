---
layout: tutorial.njk
lang: uz
title: Python o'rnatish
order: 2
permalink: /tutorial/uz/python-installation/
---

<img src="/img/tutorial/2-panduan-cepat-instalasi-python-windows-linux-mac.webp" alt="Python o'rnatish bo'yicha qo'llanma" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python dasturlarini yozishdan oldin Pythonni o'rnating va terminalingiz uni ishga tushira olishini tekshiring.

Bu dars **Python 3.13** ga mo'ljallangan.

### Linux

Ko'pgina Linux tizimlarida Python 3 allaqachon o'rnatilgan bo'ladi. Avval tekshirib ko'ring:

```bash
python3 --version
```

Agar Python o'rnatilmagan bo'lsa yoki juda eski bo'lsa, distributivingiz paket menejeri orqali yoki [python.org source releases](https://www.python.org/downloads/source/) orqali o'rnating.

Paket menejeri uchun keng tarqalgan misollar:

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

1. [Python releases for Windows](https://www.python.org/downloads/windows/) sahifasini oching.
2. Python 3.13 installer'ini yuklab oling (32-bit kerak bo'lmasa, 64-bit).
3. Installer'ni ishga tushiring.
4. Install bosishdan oldin **"Add python.exe to PATH"** ni yoqing.

Command Prompt yoki PowerShell'da o'rnatilishni tekshiring:

```bash
python --version
```

### macOS

1. [Python releases for macOS](https://www.python.org/downloads/macos/) sahifasini oching.
2. Python 3.13 installer'ini yuklab oling va ishga tushiring.
3. O'rnatish ustasini yakunlang.

Terminal'da o'rnatilishni tekshiring:

```bash
python3 --version
```

Agar Homebrew ishlatsangiz, Pythonni quyidagicha ham o'rnatishingiz mumkin:

```bash
brew install python
```

### `pip`ni tekshirish

`pip` odatda Python bilan birga o'rnatiladi. Quyidagicha tekshiring:

```bash
python -m pip --version
# or
python3 -m pip --version
```

Agar Python va pip buyruqlari ishlasa, muhitingiz keyingi darsga tayyor.
