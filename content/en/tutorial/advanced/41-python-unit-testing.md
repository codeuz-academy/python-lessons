---
layout: tutorial.njk
lang: en
title: Python Unit Testing
description: "Write and run automated tests with unittest so changes don't quietly break working code."
order: 41
permalink: /en/tutorial/python-unit-testing/
---

<img src="/img/tutorial/41-python-unit-testing.webp" alt="Python Unit Testing" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Unit Testing is a software testing method where individual units of source code (such as functions, methods, or classes) are tested to determine whether they are working correctly.

"But my code works now!"
Maybe it works now, but what if 6 months later you change one line of code and break other features? Unit tests are your safety net.

In Python, there are two main testing frameworks: `unittest` (built-in) and `pytest` (third-party, but very popular).

### 1. Using `unittest` (Built-in)

`unittest` is inspired by JUnit (Java). It uses Class-based approach.

Suppose we have a simple function:
```python
# calc.py
def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
```

We create the test file:
<div class="warning">This test assumes you have created the <code>calc.py</code> file described above.</div>

```python
# non-runnable: requires external environment/setup
# test_calc.py
import unittest
from calc import add, divide

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        
        # Test exception
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

Run with: `python test_calc.py`

#### Common `unittest` Assertions

`TestCase` provides specialized assertion methods that print helpful messages on failure:

| Method | Checks that |
| ------------------------------ | ---------------------------------- |
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `x` is truthy |
| `assertFalse(x)` | `x` is falsy |
| `assertIs(a, b)` | `a is b` (same object) |
| `assertIsNone(x)` | `x is None` |
| `assertIn(a, b)` | `a in b` |
| `assertRaises(Error)` | the block raises `Error` |
| `assertAlmostEqual(a, b)` | `a` and `b` are equal to 7 decimals |

#### Setup and Teardown

`setUp()` runs before **every** test method and `tearDown()` runs after each one. Use them to build and clean up fixtures so tests don't repeat themselves:

```python
# non-runnable: requires external environment/setup
import unittest

class TestList(unittest.TestCase):
    def setUp(self):
        self.items = [1, 2, 3]      # fresh data for each test

    def tearDown(self):
        self.items = None           # cleanup after each test

    def test_length(self):
        self.assertEqual(len(self.items), 3)

    def test_append(self):
        self.items.append(4)
        self.assertIn(4, self.items)
```

### 2. Using `pytest` (Modern Recommendation)

`pytest` is much more concise, powerful, and "Pythonic". It uses regular functions (not classes) and standard `assert` keyword.

Installation:
```bash
python -m pip install pytest
```

Writing tests with pytest:
<div class="warning">You also need to install <code>pytest</code> and have <code>calc.py</code> in the same directory.</div>

```python
# non-runnable: requires external environment/setup
# test_calc_pytest.py
import pytest
from calc import add, divide

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

Run simply by typing: `pytest` in terminal. Pytest will automatically look for files starting with `test_`.

#### Parametrized Tests

Instead of repeating a test for each input, `@pytest.mark.parametrize` runs the same test once per row of data — each case is reported separately:

```python
# non-runnable: requires external environment/setup
import pytest
from calc import add

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 7),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### 3. Mocking Concept

Mocking is a technique of replacing parts of the system being tested with mock objects. This is useful when your code depends on external systems like API, Database, or File System.

Example: We want to test a function that makes an API request, but we don't want to actually make the request (because it's slow and needs internet).

Using `unittest.mock`:

```python
# non-runnable: requires requests
from unittest.mock import Mock, patch
import requests

# Function to test
def get_user_data(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    return None

# Test with Mock
@patch('requests.get')
def test_get_user_data(mock_get):
    # Setup mock
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Bob"}
    
    # Put mock response into mock_get
    mock_get.return_value = mock_response
    
    # Run function
    result = get_user_data("http://fakeurl.com")
    
    # Assert
    assert result["name"] == "Bob"
    # Ensure requests.get is actually called with correct URL
    mock_get.assert_called_with("http://fakeurl.com")
```

### 4. Code Coverage

How much of your code is tested? Coverage tools can tell you which lines have not been touched by tests.

Install:
```bash
python -m pip install pytest-cov
```

Run:
```bash
pytest --cov=my_project
```

### Conclusion
- **Unit Test** is mandatory for serious applications.
- **pytest** is preferred because of its clean syntax.
- **Mocking** is used to isolate units from external dependencies.
- Get used to writing tests before code (TDD - Test Driven Development) or at least along with the code.
