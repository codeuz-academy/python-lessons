---
layout: tutorial.njk
lang: en
title: Pytest Fixtures Deep Dive
description: "Share setup, teardown, and test data cleanly with pytest fixtures, scopes, and parametrization."
order: 43
permalink: /en/tutorial/pytest-fixtures/
---

<img src="/img/tutorial/python-pytest.webp" alt="Pytest Fixtures" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

In our introductory testing tutorial, we learned how to write basic tests using `pytest`. However, real-world applications require establishing state before tests run (like connecting to a database or creating dummy data) and cleaning up afterwards. In `pytest`, this is elegantly handled by **Fixtures**.

## What is a Fixture?

A fixture is a function that `pytest` runs before (and optionally after) your actual test functions. You request a fixture simply by adding its name as an argument to your test function.

```python
# non-runnable: requires pytest
import pytest

@pytest.fixture
def sample_user():
    return {"id": 1, "username": "jane_doe", "role": "admin"}

def test_user_is_admin(sample_user):
    # pytest automatically injects the return value of sample_user here
    assert sample_user["role"] == "admin"
```

## Setup and Teardown (Yield)

Fixtures aren't just for returning data; they are for managing resources. If you use the `yield` keyword instead of `return`, the code before `yield` is the setup, and the code after `yield` is the teardown (cleanup) which runs after the test finishes.

```python
# non-runnable: requires pytest
import pytest

@pytest.fixture
def database_connection():
    # Setup
    db = connect_to_database()
    print("Database connected")
    
    yield db  # This is where the testing happens
    
    # Teardown
    db.close()
    print("Database connection closed")

def test_insert_user(database_connection):
    database_connection.insert("dummy user")
    assert database_connection.count() == 1
```

## Fixture Scopes

By default, a fixture runs once **per test** function (`scope="function"`). If a fixture is expensive to run (like starting a docker container), you can change its scope to run less often.

- `scope="function"`: (Default) Run once per test.
- `scope="class"`: Run once per test class.
- `scope="module"`: Run once per file.
- `scope="session"`: Run once per test suite execution.

```python
# non-runnable: requires pytest
@pytest.fixture(scope="session")
def expensive_api_client():
    # This will only be executed once, even if 100 tests request it
    client = ExpensiveAPIClient()
    client.authenticate()
    yield client
    client.logout()
```

## Using Multiple Fixtures

Tests can request multiple fixtures.

```python
# non-runnable: requires pytest
@pytest.fixture
def user():
    return User(name="Alice")

@pytest.fixture
def shopping_cart():
    return Cart()

def test_add_to_cart(user, shopping_cart):
    shopping_cart.add(user, "Laptop")
    assert "Laptop" in shopping_cart.items
```

## The `conftest.py` file

If you want fixtures to be available across multiple test files without importing them manually, define them in a file named `conftest.py` at the root of your test directory. Pytest magically discovers it.

## Parametrizing Fixtures

A fixture can be run once for **each** value in a list by passing `params`. Every test that uses the fixture runs once per parameter, so you cover many inputs without duplicating the test. The current value is available through `request.param`.

```python
# non-runnable: requires pytest
import pytest

@pytest.fixture(params=["sqlite", "postgres", "mysql"])
def database(request):
    return connect(request.param)

def test_connection(database):
    # This test runs three times — once per database backend
    assert database.is_connected()
```

## Useful Built-in Fixtures

Pytest ships with fixtures you can request without defining anything:

| Fixture | Purpose |
| ------------ | ------------------------------------------------- |
| `tmp_path` | A unique temporary directory (a `Path`) per test. |
| `monkeypatch` | Safely patch attributes, env vars, or `dict` items. |
| `capsys` | Capture text written to `stdout` / `stderr`. |
| `caplog` | Capture log records emitted during the test. |

```python
# non-runnable: requires pytest
def test_writes_file(tmp_path):
    target = tmp_path / "out.txt"
    target.write_text("hello")
    assert target.read_text() == "hello"

def test_uses_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "test-key")
    assert get_api_key() == "test-key"
```

## Conclusion

Fixtures are the heart of `pytest`. They promote reusability, separate setup logic from test logic, and make managing external resources incredibly safe and intuitive using the `yield` pattern.
