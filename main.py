from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

## GET homepage
@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    data = {}
    for i in range(1,13):
        data[i] = crud.get_remarkables_by_month(db, month=i)
    months = [calendar.month_name[i] for i in range(1,13)]
    context = {
        "data" : data,
        "months" : months,
        "current" : {
            "month" : datetime.now().month,
            "day"  : datetime.now().day
        }
    }
    return templates.TemplateResponse("home.html", {"request": request, "context": context})

## GET rmkbls by QUERY
@app.get("/remarkables/", response_model=list[schemas.Remarkables])
async def get_remarkables_by_q(db: Session = Depends(get_db), name: str=None, category:str=None, event:str=None, pic:str=None):
    return crud.get_remarkables_by_q(db, name, category, event, pic)

## ADD rmkbls
@app.post("/remarkables/", response_class=RedirectResponse)
async def create_remarkables(request: Request, db: Session = Depends(get_db)):
    data = await request.form()
    model = schemas.RemarkablesCreate(**data)
    res = crud.create_remarkables(db, model)
    return RedirectResponse('/', status_code=303)

## DEL rmkbls by ID
@app.delete("/remarkables/{remarkables_id}")
def delete_remarkables(remarkables_id: int, db: Session = Depends(get_db)):
    res = crud.delete_remarkables(db, remarkables_id)
    print(res)
    if res:
        return {'status':'ok'}
    else:
        raise HTTPException(status_code=404, detail="Remarkables not found")

## GET all rmkbls
@app.get("/remarkables/", response_model=list[schemas.Remarkables])
def get_remarkables(db: Session = Depends(get_db)):
    return crud.get_remarkables(db)

## GET list of rmkbls by MONTH
@app.get("/remarkables/month/{m}")
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
    os.system('uvicorn main:app --reload --host 0.0.0.0 --port 8080')

