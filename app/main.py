from fastapi import FastAPI, UploadFile, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app.models.category import Category
from app.models.excel_file import ExcelFile
import app.deps as deps

from app.services.category_service import category_service
from app.services.file_service import file_service

Base.metadata.create_all(bind=engine) # create db

app = FastAPI()

@app.get("/create-category", status_code=200)
def create_category(name: str, region: str, type: str, db: Session = Depends(deps.get_db)):
    return category_service.create(db, name, region, type).id

@app.post("/upload-file", status_code=200)
def upload_file(category_name: str, file: UploadFile):
    file_service.create(category_name, file)

@app.get("/sum-type")
def sum_type(type: str):
    return {"message": "Sum Type"}

@app.get("/find-regions")
def find_regions(search_term: str):
    return {"message": "Find Regions"}