from sqlalchemy.orm import Session
from fastapi import UploadFile

from app.models.excel_file import ExcelFile
from app.crud.crud_excel_file import crud_excel_file, ExcelFileCrud
from app.services.file_storage_service import IFileStorageService
from app.services.local_file_storage_service import local_file_storage_service

class FileService:

    def __init__(self, crud_excel_file: ExcelFileCrud, file_storage_service: IFileStorageService):
        self.crud_excel_file = crud_excel_file
        self.file_storage_service = file_storage_service

    async def create(self, category_name: str, file: UploadFile):
        print(f"category name is: {category_name}")
        await self.file_storage_service.upload_file(file)



file_service = FileService(crud_excel_file=crud_excel_file, file_storage_service=local_file_storage_service)