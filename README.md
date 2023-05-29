# REMARKABLES

Mark all the REMARKABLES. Widget for marking important dates (birthdays/anniversaries).


Framework   : FastAPI
Database    : PostgreSQL


## Installation

1. install required package with `pip`

    ```bash
    pip install -r requirements
    ```

2. create `.env` file in root directory and add `DATABASE_URL` with credentials

    ```bash
    DATABASE_URL="<DB>://<usr>:<pwd>@<host>/<db>"
    ```

3. run the script `main.py`

    ```bash
    python main.py
    ```
    or 
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8080
    ```

## Usage

- Visit `<host>:<port>` or `localhost:8080` by default

- Press the title **[REMARKABLES]** to open input form.

## APIs

- Visit `<host>:<port>/docs` or `localhost:8080/docs` by default
