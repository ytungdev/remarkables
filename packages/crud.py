from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

from . import models, schemas

from datetime import date

def get_remarkables(db: Session):
    return db.query(models.Remarkables).all()


def get_remarkables_by_month(db: Session, month: int):
    res = db.query(models.Remarkables).filter(extract('month', models.Remarkables.date) == month).order_by(models.Remarkables.id.desc()).all()
    sres = sorted(res, key=lambda x: int(x.date.day))
    today = date.today()
    final = []
    for r in sres:
        d = r.__dict__
        parsed = r.date.replace(year=today.year)
        d['active'] = 1 if parsed > today else 0
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
