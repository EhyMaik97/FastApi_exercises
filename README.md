# FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

*Uvicorn is an ASGI web server implementation for Python.*

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install fastapi.

```bash
pip install fastapi
```

```bash
pip install "uvicorn[standard]"
```


## Usage

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome": "Hi!"}
```

## Run it

Run the server with:

```bash
uvicorn main:app --reload
```

## Check it

Open your browser at http://127.0.0.1:8000/