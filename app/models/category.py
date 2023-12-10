from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    region = Column(String)
    type = Column(String)
