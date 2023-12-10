from abc import ABC, abstractmethod
from fastapi import UploadFile
from pandas import DataFrame

class IFileStorageService(ABC):

    # returns the file path
    @abstractmethod
    async def upload_file(self, file: UploadFile) -> str:
        pass

    # returns the dataframe of the file
    @abstractmethod
    def fetch_file(self, path: str) -> DataFrame:
        pass