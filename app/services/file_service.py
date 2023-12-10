from sqlalchemy.orm import Session
from fastapi import UploadFile

from app.models.excel_file import ExcelFile
from app.models.category import Category
from app.crud.crud_excel_file import crud_excel_file, ExcelFileCrud
from app.services.category_service import category_service, CategoryService
from app.services.file_storage_service import IFileStorageService
from app.services.local_file_storage_service import local_file_storage_service

class FileService:

    def __init__(self, crud_excel_file: ExcelFileCrud, file_storage_service: IFileStorageService,
                category_service: CategoryService):
        self.crud_excel_file = crud_excel_file
        self.file_storage_service = file_storage_service
        self.category_service = category_service

    def create(self, db: Session, category_id: int, file_addr: str) -> ExcelFile:
        return self.crud_excel_file.create(db, category_id, file_addr)

    def create_by_category_name(self, db: Session, category_name: str, file: UploadFile) -> ExcelFile:
        file_addr: str = self.file_storage_service.upload_file(file)
        category: Category = category_service.get_category_by_name(db, category_name)
        excel_file: ExcelFile = self.create(db, category.id, file_addr)
        return excel_file



file_service = FileService(crud_excel_file=crud_excel_file, file_storage_service=local_file_storage_service,
                            category_service=category_service)