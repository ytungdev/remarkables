import os
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session


from packages import crud, models, schemas
from packages.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# @app.get("/")
# async def home():
#     data = {
#         "text": "hi"
#     }
#     return {"data": data}


# @app.get("/page/{page_name}")
# async def page(page_name: str):
#     data = {
#         "page": page_name
#     }
#     return {"data": data}


# @app.get("/month/")
# def list_month(mo: int = datetime.now().month):
#     return {"month": mo, "count": 0, "result":[]}

# @app.post("/remarkables/{remarkables_id}")
# def update_remarkables(remarkables_id: int, remarkables: models.Remarkables):
#     return {"item_name": remarkables.name, "remarkables_id": remarkables_id}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/remarkables/", response_model=schemas.Remarkables)
def create_remarkables(db: Session = Depends(get_db)):
    return crud.create_remarkables(db)

@app.get("/remarkables/", response_model=list[schemas.Remarkables])
def get_remarkables(db: Session = Depends(get_db)):
    return crud.get_remarkables(db)

# @app.get("/remarkables/", response_model=list[schemas.Remarkables])
@app.get("/remarkables/month/")
def get_remarkables_by_month(month:int = datetime.now().month, db: Session = Depends(get_db)):
    if month > 12:
        raise HTTPException(status_code=404, detail="Invalid month")
    results = crud.get_remarkables_by_month(db, month=month)
    data = {
        'month': month,
        'result':results
    }
    return data

if __name__ == "__main__":
   os.system('uvicorn main:app --reload --port 8080')

# get_remarkables