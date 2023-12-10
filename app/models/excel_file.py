from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

from app.database import Base

class ExcelFile(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer)
    file_addr = Column(String)
    sum = Column(Float, default=None, nullable=True)