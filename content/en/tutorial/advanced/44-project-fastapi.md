---
layout: tutorial.njk
lang: en
title: "Cookbook: Building a FastAPI Backend"
description: "Build a small FastAPI backend end to end, from routes and models to running the server."
order: 44
permalink: /en/tutorial/project-fastapi/
---

<img src="/img/tutorial/python-fastapi.webp" alt="FastAPI Backend Development" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Now that you've mastered the fundamentals of Python, data structures, algorithms, and testing, it is time to build a real-world application. In this cookbook tutorial, we will construct a high-performance REST API backend using **FastAPI**.

## Why FastAPI?

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.8+ based on standard Python type hints.

- **Fast**: It rivals Node.js and Go in performance.
- **Easy**: Automatic interactive API documentation.
- **Validation**: Automatic request body mapping and validation using Pydantic.

## 1. Setup

First, install FastAPI and an ASGI server, `uvicorn`.

```bash
python -m pip install fastapi uvicorn
```

Create a new file called `main.py`.

<div class="warning">To run this code, you need to install the dependencies first using Python's package manager.</div>

```python
# non-runnable: requires fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Run your server with:

```bash
uvicorn main:app --reload
```

## 2. Using Pydantic for Data Validation

FastAPI uses the type hints we covered earlier in the course, together with the `Pydantic` library, to validate data automatically. Let's create an endpoint that accepts data for a new user.

<div class="warning">Ensure you have <code>pydantic</code> installed as well to run the following validation code.</div>

```python
# non-runnable: requires fastapi
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Database mockup
db = []

# Define standard data schema using Pydantic
class User(BaseModel):
    id: int
    name: str
    age: int
    email: Optional[str] = None

@app.post("/users/")
def create_user(user: User):
    for u in db:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User already exists")
    db.append(user)
    return {"status": "success", "user": user}

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
```

When someone sends a POST request with missing fields or an `age` defined as `"twenty"` instead of `20`, FastAPI immediately returns an automatic 422 Unprocessable Entity error. You don't have to write validation code by hand.

## 3. The Power of Automatic Documentation

Because of the explicit type hints, FastAPI automatically generates two interactive documentation interfaces based on OpenAPI specifications:

- **Swagger UI**: Found at `http://127.0.0.1:8000/docs`
- **ReDoc**: Found at `http://127.0.0.1:8000/redoc`

Open Swagger UI in your browser to instantly test the endpoints without using Postman or `curl`.

## 4. Async Endpoints and Query Parameters

FastAPI is built on ASGI, so a path function can be declared `async def`. Use it when the handler awaits I/O (a database or an external API) — it lets the server handle other requests while waiting. See the [Async / Await](/en/tutorial/python-async-await/) tutorial for the underlying concepts.

Function arguments that are **not** part of the path become **query parameters** automatically. A parameter with a default is optional; one without is required.

```python
# non-runnable: requires fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/search/")
async def search(q: str, limit: int = 10):
    # GET /search/?q=python&limit=5
    return {"query": q, "limit": limit}
```

Here `q` is required and `limit` defaults to `10`. FastAPI also validates types: passing `limit=abc` returns a 422 error.

## 5. Testing Your API

FastAPI provides a `TestClient` (built on `httpx`) so you can test endpoints with `pytest` — no running server needed. This ties together everything from the testing tutorials.

```python
# non-runnable: requires fastapi
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

## Conclusion

FastAPI perfectly fuses Python's type annotations and asynchronous capabilities into an enterprise-ready framework. From here, you can connect your FastAPI backend to a real database using an ORM like `SQLAlchemy` and protect paths using standard OAuth2 security protocols.
