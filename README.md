# REMARKABLES

Widget for marking and displaying important dates (birthdays/anniversaries). Requested and styled by GF.

## Technologies

- **Framework**   : FastAPI
- **Database**    : PostgreSQL, SQLAlchemy, Alembic


## Functions

- Display _important dates_ in each month
  -  Past months are collapsed.
  -  Clicking the month can toggle it.
  -  Past _important dates_ are darkened.

-  Add new _important dates_
    1.  click the title `REMARKABLES` to open input form.
    2.  fill all details.
    3.  click `Add`.

-  Remove existing _important dates_
    1. find the target _important dates_ card.
    2. click the `x` on the top right corner.
    3. Confirm by clicking `ok` when prompt pop-up.


## Usage

1. install required package with `pip`

    ```bash
    pip install -r requirements.txt
    ```

2. create `.env` file in root directory and add `DATABASE_URL` with credentials

    ```
    DATABASE_URL="<DB>://<usr>:<pwd>@<host>/<db>"
    ```
    e.g
    ```
    DATABASE_URL="postgresql://postgres:password@localhost/postgres"
    ```

4. run the app

    ```bash
    python main.py
    ```
    or 
    ```
    uvicorn main:app --reload --host 0.0.0.0 --port 8080
    ``` 

## APIs

- `GET /remarkables` : retrieve all _important dates_ in json format, filter result if any of the following parameter provided:
    -  name
    -  category
    -  event
- `GET /remarkables/month/{month}` : retrieve all _important dates_ in specific month.
- `POST /remarkables` : create new _important dates_.
- `DELETE /remarkables/{id}` : delete _important dates_ by id.
- visit `/docs` for FastAPI built-in API docs

