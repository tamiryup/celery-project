from sqlalchemy.orm import Session

from app.models.category import Category

from app.crud.crud_category import crud_category, CategoryCrud

class CategoryService:

    def __init__(self, crud_category: CategoryCrud):
        self.crud_category = crud_category

    def create(self, db: Session, name: str, region: str, type: str) -> Category:
        return self.crud_category.create(db, name, region, type)
    

category_service = CategoryService(crud_category)


