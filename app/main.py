from fastapi import FastAPI, UploadFile, Depends, Response, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app.models.category import Category
from app.models.excel_file import ExcelFile
from app.exceptions import NameAlreadyExists, InvalidCategoryName
import app.deps as deps

from app.services.category_service import category_service
from app.services.file_service import file_service

Base.metadata.create_all(bind=engine) # create db

app = FastAPI()

###### EXCEPTIONS ######

@app.exception_handler(InvalidCategoryName)
async def invalid_category_name_handler(request: Request, exc: InvalidCategoryName):
    return JSONResponse(status_code=404, content={"message": str(exc)})

@app.exception_handler(NameAlreadyExists)
async def invalid_category_name_handler(request: Request, exc: NameAlreadyExists):
    return JSONResponse(status_code=400, content={"message": str(exc)})



###### ROUTES ######

@app.get("/create-category", status_code=200)
def create_category(name: str, region: str, type: str, db: Session = Depends(deps.get_db)):
    category: Category =  category_service.create(db, name, region, type)
    return category.id

@app.post("/upload-file", status_code=200)
def upload_file(category_name: str, file: UploadFile, db: Session = Depends(deps.get_db)):
    file_service.create_by_category_name(db, category_name, file)
    return Response(status_code=200)

@app.get("/sum-type")
def sum_type(type: str, db: Session = Depends(deps.get_db)):
    sum: float = file_service.sum_files_by_category_type(db, type)
    return sum

@app.get("/find-regions")
def find_regions(search_term: str):
    return {"message": "Find Regions"}