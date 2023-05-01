from pydantic import BaseModel
from datetime import date
from enum import Enum


class Event(str, Enum):
    BIRTHDAY = 'birthday'
    ANNIVERSARY = 'anniversary'

class RemarkablesBase(BaseModel):
    name: str
    category: str
    event: Event
    date: date # 'YY-MM-DD'
    class Config:
        orm_mode = True

class Remarkables(RemarkablesBase):
    id : int

class RemarkablesCreate(RemarkablesBase):
    pass