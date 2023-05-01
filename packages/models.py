from sqlalchemy import Column, Date, Integer, String

from .database import Base

class Remarkables(Base):
    __tablename__ = 'remarkables'
    id  = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    event = Column(String)
    date = Column(Date)
