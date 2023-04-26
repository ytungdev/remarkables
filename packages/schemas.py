from pydantic import BaseModel
from datetime import date
from enum import Enum


class Pic(str, Enum):
    B = "B"
    C = "C"
    Y = "Y"

class Event(str, Enum):
    BIRTHDAY = 'birthday'
    ANNIVERSARY = 'anniversary'

class RemarkablesBase(BaseModel):
    name: str
    category: str
    event: Event
    date: date # 'YY-MM-DD'
    pic: Pic = 'B'

class Remarkables(RemarkablesBase):
    id : int
    class Config:
        orm_mode = True

class RemarkablesCreate(RemarkablesBase):
    pass