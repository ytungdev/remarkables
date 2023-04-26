from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

from . import models, schemas


def get_remarkables(db: Session):
    return db.query(models.Remarkables).all()


def get_remarkables_by_month(db: Session, month: int):
    return db.query(models.Remarkables).filter(extract('month', models.Remarkables.date) == month).all()


def create_remarkables(db: Session, remarkables: schemas.RemarkablesCreate):
    db_entry = models.Remarkables(**remarkables.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
