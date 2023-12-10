from fastapi import UploadFile
from pandas import DataFrame
import pandas as pd
import uuid
import os

from app.services.file_storage_service import IFileStorageService

class LocalFileStorageService(IFileStorageService):

    def __init__(self):
        self.directory_name = "./uploads"

    async def upload_file(self, file: UploadFile) -> str:
        filename = uuid.uuid1()
        file_path = f"{self.directory_name}/{filename}.xlsx"

        # create directory if doesn't exist
        if not os.path.exists(self.directory_name):
            os.makedirs(self.directory_name)

        # save the file to the specified path
        with open(file_path, "wb") as file_output:
            file_output.write(file.file.read())
        
        return file_path
    
    def fetch_file(self, path: str) -> DataFrame:
        return pd.read_excel(path)

local_file_storage_service = LocalFileStorageService()