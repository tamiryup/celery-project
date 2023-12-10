from sqlalchemy.orm import Session
from sqlalchemy import update
from typing import Optional, List

from app.models.excel_file import ExcelFile

class ExcelFileCrud:

    def create(self, db: Session, category_id: int, file_addr: str) -> ExcelFile:
        file = ExcelFile(category_id=category_id, file_addr=file_addr)
        db.add(file)
        db.commit()
        db.refresh(file)
        return file
    
    def get_files_by_category_ids(self, db: Session, category_ids: List[int]):
        return db.query(ExcelFile).filter(ExcelFile.category_id.in_(category_ids)).all()
    
    # Bulk update files sum
    def update_files_sum(self, db: Session, file_list_to_update: List[ExcelFile], sums_list: List[float]):
        for i in range(len(file_list_to_update)):
            stmt = update(ExcelFile).where(ExcelFile.id == file_list_to_update[i].id).values(sum=sums_list[i])
            db.execute(stmt)
        
        db.commit()


crud_excel_file = ExcelFileCrud()