---
layout: tutorial.njk
lang: uz
title: Python type hint'lar (type annotations)
order: 33
permalink: /tutorial/uz/python-type-hints/
---

Type hints (type annotations) - Python'dagi imkoniyat bo'lib, o'zgaruvchilar, funksiya parametrlar va return qiymatlar uchun kutilayotgan data turini ko'rsatishga yordam beradi. Python 3.5 da kiritilgan type hint'lar zamonaviy Python development'da tobora muhim bo'lib boryapti.

### Nega type hint ishlatish kerak?

Type hint'lar bir nechta foyda beradi:

- **Yaxshiroq dokumentatsiya** - kod o'zi "hujjat" bo'lib qoladi
- **Xatoni erta topish** - IDE va vositalar runtime'dan oldin bug'larni topishi mumkin
- **Aniqroq autocomplete** - IDE aniqroq tavsiyalar beradi
- **Maintainability** - boshqa dasturchilar uchun tushunish osonroq bo'ladi
- **Xavfsiz refactoring** - kod o'zgarishlarini tekshirish osonlashadi

**Muhim:** Python'da type hint'lar ixtiyoriy (optional) va runtime'ga ta'sir qilmaydi. Python baribir dinamik typed tildir.

### Asosiy sintaksis

```python
# Variable annotation
name: str = "Bob"
age: int = 25
height: float = 175.5
active: bool = True

# Function parameter and return type annotation
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

# Function without return value
def print_info(message: str) -> None:
    print(message)

print_info("Type hints are useful!")
```

### Asosiy data turlari

```python
# Primitive types
x: int = 10
y: float = 3.14
z: str = "hello"
flag: bool = True
data: bytes = b"hello"

# None type
result: None = None
```

### Collection turlari

Collection turlari uchun Python < 3.9 da `typing` moduli ishlatiladi, Python 3.9+ da esa built-in generic'lar (`list[int]`) ishlatish mumkin:

```python
# Python 3.9+ (recommended)
numbers: list[int] = [1, 2, 3]
name_age: dict[str, int] = {"Alice": 25, "Bob": 30}
coordinates: tuple[float, float] = (3.14, 2.71)
unique: set[str] = {"apple", "orange"}

# Python 3.5 - 3.8 (use typing)
from typing import List, Dict, Tuple, Set

numbers: List[int] = [1, 2, 3]
name_age: Dict[str, int] = {"Alice": 25}
coordinates: Tuple[float, float] = (3.14, 2.71)
unique: Set[str] = {"apple", "orange"}
```

### Optional va Union

`None` bo'lishi mumkin bo'lgan yoki bir nechta turdan biri bo'lishi mumkin bo'lgan qiymatlar uchun:

```python
from typing import Optional, Union

# Optional - can be None or a specific type
def find_user(id: int) -> Optional[str]:
    if id == 1:
        return "Alice"
    return None

# Union - can be one of several types
def process(data: Union[str, int]) -> str:
    return str(data)

# Python 3.10+ syntax(recommended)
def find_user(id: int) -> str | None:
    if id == 1:
        return "Alice"
    return None

def process(data: str | int) -> str:
    return str(data)
```

### Callable (funksiyani parametr sifatida olish)

```python
from typing import Callable

# Function that accepts another function as parameter
def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

def double(x: int) -> int:
    return x * 2

result = apply_twice(double, 5)  # 20

# Callable with multiple arguments
def operation(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
```

### Any turi

Tur "istalgan narsa bo'lishi mumkin" bo'lsa:

```python
from typing import Any

def process_anything(data: Any) -> Any:
    return data
```

### Type alias'lar

Murakkab turlar uchun alias yaratish:

```python
from typing import TypeAlias

# Type alias
UserId: TypeAlias = int
UserData: TypeAlias = dict[str, str | int]

def get_user(user_id: UserId) -> UserData:
    return {"name": "Alice", "age": 25}

# For more complex types
Matrix: TypeAlias = list[list[float]]

def transpose(matrix: Matrix) -> Matrix:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
```

### Generic turlar

Turli turlar bilan ishlay oladigan funksiyalar uchun:

```python
from typing import TypeVar

T = TypeVar('T')

def first_element(items: list[T]) -> T:
    return items[0]

# Can be used with list of any type
number = first_element([1, 2, 3])        # int
word = first_element(["a", "b", "c"])   # str
```

### Literal turlar

Qiymat faqat aniq variantlardan biri bo'lishi kerak bo'lsa:

```python
from typing import Literal

def set_status(status: Literal["active", "inactive", "pending"]) -> None:
    print(f"Status: {status}")

set_status("active")    # OK
set_status("unknown")   # Type error(detected by type checker)

# Useful for limited options
Mode = Literal["read", "write", "append"]

def open_file(path: str, mode: Mode) -> None:
    pass
```

### TypedDict

Tuzilishi qat'iy bo'lgan dictionary'lar uchun:

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str

def create_user(data: User) -> None:
    print(f"Creating user: {data['name']}")

# Type checker will validate validity
user: User = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}

create_user(user)
```

### Class uchun annotation'lar

```python
class Student:
    name: str
    id: str
    gpa: float
    
    def __init__(self, name: str, id: str) -> None:
        self.name = name
        self.id = id
        self.gpa = 0.0
    
    def set_gpa(self, gpa: float) -> None:
        self.gpa = gpa
    
    def get_info(self) -> str:
        return f"{self.name} ({self.id}): GPA {self.gpa}"
```

### Type hint bilan `@dataclass`

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    stock: int = 0
    
    def total_value(self) -> float:
        return self.price * self.stock

product = Product("Laptop", 15000000, 10)
print(product.total_value())  # 150000000
```

### Type checking uchun vositalar

Type hint'lar runtime'da tekshirilmaydi. Buning uchun quyidagi vositalardan foydalaning:

#### 1. mypy

```bash
pip install mypy
mypy script.py
```

#### 2. pyright (VS Code Pylance)

VS Code'da Pylance extension orqali allaqachon integratsiya qilingan.

#### 3. pytype (Google)

```bash
pip install pytype
pytype script.py
```

### To'liq misol

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Address:
    street: str
    city: str
    zip_code: str

@dataclass  
class Employee:
    name: str
    email: str
    salary: float
    address: Optional[Address] = None
    
    def full_info(self) -> str:
        info = f"{self.name} - {self.email}"
        if self.address:
            info += f" ({self.address.city})"
        return info

def calculate_total_salary(employee_list: list[Employee]) -> float:
    return sum(k.salary for k in employee_list)

def find_employee(
    employee_list: list[Employee], 
    name: str
) -> Employee | None:
    for k in employee_list:
        if k.name.lower() == name.lower():
            return k
    return None

# Usage
address = Address("5th Avenue", "New York", "12190")
e1 = Employee("Alice", "alice@email.com", 10000000, address)
e2 = Employee("Bob", "bob@email.com", 12000000)

all_employees = [e1, e2]
print(calculate_total_salary(all_employees))  # 22000000
```
