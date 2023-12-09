from sqlalchemy.orm import Session

from app.models.category import Category

from app.crud.crud_category import crud_category

class CategoryService:

    def create(self, db: Session, name: str, region: str, type: str) -> Category:
        return crud_category.create(db, name, region, type)
    

category_service = CategoryService()


