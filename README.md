# important-dates

Mark down all important dates


## installation

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