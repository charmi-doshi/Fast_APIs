```markdown
# FastAPI Backend

This repository contains a simple FastAPI backend application providing basic API endpoints.

## Features

- `/`: Returns a "Hello World" message.
- `/heartbeat`: Accepts a POST request with a heartbeat message and returns the message with a timestamp.
- `/version`: Returns the current version of the API.
- `/upper`: Accepts a PUT request with text in the body and returns the text in uppercase.
- `/lower`: Accepts a PUT request with text in the body and returns the text in lowercase.

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```

## Usage

1.  Run the application using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

    This will start the server, typically on `http://127.0.0.1:8000`.  The `--reload` flag enables automatic reloading on code changes.

2.  Access the endpoints using a tool like `curl` or Postman:

    -   **Root Endpoint:**

        ```bash
        curl http://127.0.0.1:8000/
        ```

    -   **Heartbeat Endpoint:**

        ```bash
        curl -X POST -H "Content-Type: application/json" -d '{"heartbeat": "Application is alive"}' http://127.0.0.1:8000/heartbeat
        ```

    -   **Version Endpoint:**

        ```bash
        curl http://127.0.0.1:8000/version
        ```

    -   **Upper Endpoint:**

        ```bash
        curl -X PUT -H "Content-Type: application/json" -d '"hello world"' http://127.0.0.1:8000/upper
        ```

    -   **Lower Endpoint:**

        ```bash
        curl -X PUT -H "Content-Type: application/json" -d '"HELLO WORLD"' http://127.0.0.1:8000/lower
        ```

## Project Structure

```
.
├── fast_api.py
└── main.py
```

## Technologies

-   FastAPI
-   Python 3.7+
-   Uvicorn (ASGI server)
-   Pydantic
```