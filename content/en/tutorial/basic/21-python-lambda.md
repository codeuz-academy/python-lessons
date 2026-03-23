---
layout: tutorial.njk
lang: en
title: Python Lambda
description: "Learn Python Lambda in Python with practical examples and clear explanations."
order: 21
permalink: /en/tutorial/python-lambda/
---

<img src="/img/tutorial/21-python-lambda.webp" alt="Python Lambda" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Lambda is a short way to create anonymous functions (functions without a name) in Python. Lambda is very useful for simple operations that only need to be used once, especially as arguments for functions like `map()`, `filter()`, and `sorted()`.

### Basic Syntax

```python
# Syntax: lambda arguments: expression

# Normal function
def square(x):
    return x ** 2

# Equivalent lambda
square = lambda x: x ** 2

print(square(5))  # Output: 25
```

Lambda can only contain one expression and automatically returns the result.

### `lambda` with Multiple Arguments

```python
# One argument
double = lambda x: x * 2
print(double(5))  # 10

# Two arguments
add = lambda a, b: a + b
print(add(3, 5))  # 8

# Three arguments
volume = lambda p, l, t: p * l * t
print(volume(2, 3, 4))  # 24

# No arguments
random_greeting = lambda: "Hello!"
print(random_greeting())  # Hello!
```

### `lambda` with Default Arguments

```python
# Default argument
power = lambda x, n=2: x ** n
print(power(3))     # 9 (power of 2)
print(power(3, 3))  # 27 (power of 3)

# Multiple defaults
greet = lambda name, formal=False: f"Good Morning, {name}" if formal else f"Hi, {name}!"
print(greet("Bob"))            # Hi, Bob!
print(greet("Bob", formal=True))  # Good Morning, Bob
```

### `lambda` with Conditional Expression

```python
# Ternary in lambda
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(4))  # Even
print(check_even(7))  # Odd

# Multiple conditions
letter_grade = lambda n: "A" if n >= 90 else "B" if n >= 80 else "C" if n >= 70 else "D"
print(letter_grade(95))  # A
print(letter_grade(75))  # C
```

### `lambda` with Built-in Functions

#### map() - Transform every element

```python
numbers = [1, 2, 3, 4, 5]

# Square every number
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Convert to string
str_numbers = list(map(lambda x: str(x), numbers))
print(str_numbers)  # ['1', '2', '3', '4', '5']

# Map with two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_lists = list(map(lambda x, y: x + y, list1, list2))
print(sum_lists)  # [5, 7, 9]
```

#### filter() - Filter elements based on condition

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter numbers greater than 5
large = list(filter(lambda x: x > 5, numbers))
print(large)  # [6, 7, 8, 9, 10]

# Filter empty strings
words = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda x: x, words))
print(non_empty)  # ['hello', 'world', 'python']
```

#### `sorted()` - Sorting with Custom Key

```python
# Sort by absolute value
numbers = [-5, 2, -3, 1, -4]
sorted_nums = sorted(numbers, key=lambda x: abs(x))
print(sorted_nums)  # [1, 2, -3, -4, -5]

# Sort list of tuples
students = [("Alice", 85), ("Bob", 92), ("Carol", 78)]
by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(by_score)  # [('Bob', 92), ('Alice', 85), ('Carol', 78)]

# Sort list of dictionaries
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Carol", "age": 30}
]
by_age = sorted(data, key=lambda x: x["age"])
print(by_age)
# [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Carol', 'age': 30}]

# Sort string by length
words = ["python", "go", "javascript", "c"]
by_length = sorted(words, key=lambda x: len(x))
print(by_length)  # ['c', 'go', 'python', 'javascript']
```

#### reduce() - Aggregate into one value

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Multiply all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5
```

### `lambda` in Data Structures

```python
# Dictionary of functions
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "Error"
}

print(operations["add"](10, 5))  # 15
print(operations["multiply"](10, 5))    # 50

# List of lambdas
transformations = [
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x + 10
]

number = 5
for t in transformations:
    print(t(number))  # 10, 25, 15
```

### Immediately Invoked `lambda`

Lambda that is executed immediately:

```python
# Immediately invoked function expression
result = (lambda x, y: x + y)(3, 5)
print(result)  # 8

# Useful for one-time operations
data = (lambda: {"config": "value", "debug": True})()
print(data)  # {'config': 'value', 'debug': True}
```

### `lambda` vs Regular Functions

| Aspect | Lambda | def Function |
|-------|--------|--------------|
| Name | Anonymous | Must have a name |
| Lines | Single expression | Multiple statements |
| Readability | For simple operations | For complex logic |
| Docstring | Cannot | Can |
| Type hints | Cannot | Can |

```python
# When to use lambda
data = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, data))  # Good for simple disposable logic

# When to use def
def calculate_tax(salary, allowance=0, deduction=0):
    """
    Calculates income tax.
    
    Args:
        salary: Basic salary
        allowance: Total allowance
        deduction: Total deduction
        
    Returns:
        Tax amount to be paid
    """
    taxable_income = salary + allowance - deduction
    if taxable_income <= 50000000:
        return taxable_income * 0.05
    elif taxable_income <= 250000000:
        return taxable_income * 0.15
    else:
        return taxable_income * 0.25
```

### Practical Example

```python
# 1. Sorting complex data
products = [
    {"name": "Laptop", "price": 15000000, "rating": 4.5},
    {"name": "Mouse", "price": 250000, "rating": 4.8},
    {"name": "Keyboard", "price": 750000, "rating": 4.2}
]

# Sort by price(ascending)
by_price = sorted(products, key=lambda p: p["price"])

# Sort by rating(descending)
by_rating = sorted(products, key=lambda p: p["rating"], reverse=True)

# 2. Data transformation pipeline
data = ["  Hello  ", "WORLD", "  python  "]
cleaned = list(map(lambda s: s.strip().lower(), data))
print(cleaned)  # ['hello', 'world', 'python']

# 3. Event handlers(pseudo-code)
button_actions = {
    "save": lambda: print("Saving..."),
    "delete": lambda: print("Deleting..."),
    "export": lambda: print("Exporting...")
}

action = "save"
button_actions[action]()  # Saving...
```

### Tips and Best Practices

1. **Use lambda for simple operations** - If logic is more than one line, use `def`
2. **Don't overdo it** - Code should remain readable
3. **Avoid nested lambdas** - Hard to read and debug
4. **Consider list comprehension** - Often more readable than map+lambda

```python
# Lambda + map
data = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, data))
print(result)  # [2, 4, 6, 8, 10]

# List comprehension(more pythonic)
result = [x * 2 for x in data]
print(result)  # [2, 4, 6, 8, 10]
```
