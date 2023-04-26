from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from packages import crud, models, schemas
from packages.database import SessionLocal, engine

import os
from datetime import datetime
import calendar

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

templates = Jinja2Templates(directory="templates")


# @app.get("/page/{page_name}")
# async def page(page_name: str):
#     data = {
#         "page": page_name
#     }
#     return {"data": data}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):

    data = {}
    for i in range(1,13):
        data[i] = crud.get_remarkables_by_month(db, month=i)
    months = [calendar.month_name[i] for i in range(1,13)]
    context = {
        "data" : data,
        "months" : months
    }
    return templates.TemplateResponse("home.html", {"request": request, "context": context})


@app.post("/remarkables/", response_model=schemas.Remarkables)
def create_remarkables(db: Session = Depends(get_db)):
    return crud.create_remarkables(db)


@app.get("/remarkables/", response_model=list[schemas.Remarkables])
def get_remarkables(db: Session = Depends(get_db)):
    return crud.get_remarkables(db)

# @app.get("/remarkables/", response_model=list[schemas.Remarkables])


@app.get("/remarkables/month/")
def get_remarkables_by_month(m: int = datetime.now().month, db: Session = Depends(get_db)):
    if m > 12:
        raise HTTPException(status_code=404, detail="Invalid month")
    results = crud.get_remarkables_by_month(db, month=m)
    data = {
        'month': m,
        'result': results
    }
    return data


if __name__ == "__main__":
    os.system('uvicorn main:app --reload --port 8080')

# get_remarkables
