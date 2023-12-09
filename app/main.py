from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get("/create-category")
def create_category(category_name: str, region: str, type: str):
    return {"message": category_name}

@app.post("/upload-file")
def upload_file(category_name: str, file: UploadFile):
    return {"message": file.content_type}

@app.get("/sum-type")
def sum_type(type: str):
    return {"message": "Sum Type"}

@app.get("/find-regions")
def find_regions(search_term: str):
    return {"message": "Find Regions"}