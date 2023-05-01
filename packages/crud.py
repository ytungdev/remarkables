from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

from . import models, schemas

from datetime import date

def get_remarkables(db: Session):
    return db.query(models.Remarkables).all()

def get_remarkables_by_q(db: Session, name: str=None, category:str=None, event:str=None, pic:str=None):
    q = db.query(models.Remarkables)
    print(name, category, event, pic)
    if name:
        q = q.filter(models.Remarkables.name==name)
    if category:
        q = q.filter(models.Remarkables.category==category)
    if event != None:
        q = q.filter(models.Remarkables.event==event)
    if pic != None:
        q = q.filter(models.Remarkables.pic==pic)
    res = q.order_by(models.Remarkables.id.desc()).all()
    sres = sorted(res, key=lambda x: int(x.date.month)*100+int(x.date.day))
    print(q.statement.compile(compile_kwargs={"literal_binds": True}))
    return sres

def get_remarkables_by_month(db: Session, month: int):
    res = db.query(models.Remarkables).filter(extract('month', models.Remarkables.date) == month).order_by(models.Remarkables.id.desc()).all()
    sres = sorted(res, key=lambda x: int(x.date.day))
    today = date.today()
    final = []
    for r in sres:
        d = r.__dict__
        parsed = r.date.replace(year=today.year)
        d['active'] = 2 if parsed == today else 1 if parsed > today else 0 
        final.append(d)
    return final


def create_remarkables(db: Session, remarkables: schemas.RemarkablesCreate):
    db_entry = models.Remarkables(**remarkables.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def delete_remarkables(db: Session, remarkables_id: int):
    entry = db.query(models.Remarkables).get(remarkables_id)
    if entry:
        db.delete(entry)
        db.commit()
        return True
    else:
        return False
