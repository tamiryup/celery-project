from sqlalchemy.orm import Session
from fastapi import UploadFile
from typing import List
from pandas import DataFrame
import pandas as pd

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
    
    def calc_file_sum(self, file: ExcelFile) -> float:
        df: DataFrame = self.file_storage_service.fetch_file(file.file_addr)
        print(df)
        sum: float = 0
        for column in df.columns:
            for index, value in df[column].items():
                if (type(value) == int or type(value) == float) and not pd.isna(value):
                    print(value)
                    sum += value
        return sum

    
    def sum_files_by_category_type(self, db: Session, category_type: str) -> float:
        categories: List[Category] = self.category_service.get_categories_by_type(db, category_type)
        category_ids: List[int] = list(map(lambda category: category.id, categories)) #TODO: consider querying just the ids
        files: List[ExcelFile] = self.crud_excel_file.get_files_by_category_ids(db, category_ids)

        file_list_to_update: List[ExcelFile] = []
        sums_list: List[float] = []
        sum: float = 0
        for file in files:
            file_sum = file.sum
            if file_sum is None:
                file_sum = self.calc_file_sum(file)
                file_list_to_update.append(file)
                sums_list.append(file_sum)

            sum += file_sum

        if(len(file_list_to_update) > 0):
            crud_excel_file.update_files_sum(db, file_list_to_update, sums_list)

        return sum



file_service = FileService(crud_excel_file=crud_excel_file, file_storage_service=local_file_storage_service,
                            category_service=category_service)