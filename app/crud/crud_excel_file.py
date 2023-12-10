from sqlalchemy.orm import Session
from typing import Optional, List

from app.models.excel_file import ExcelFile

class ExcelFileCrud:

    def create(self, db: Session, category_id: int, file_addr: str) -> ExcelFile:
        file = ExcelFile(category_id=category_id, file_addr=file_addr)
        db.add(file)
        db.commit()
        db.refresh(file)
        return file

crud_excel_file = ExcelFileCrud()