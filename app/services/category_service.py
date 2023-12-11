from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from app.models.category import Category
from app.crud.crud_category import crud_category, CategoryCrud
from app.exceptions import NameAlreadyExists, InvalidCategoryName

class CategoryService:

    def __init__(self, crud_category: CategoryCrud):
        self.crud_category = crud_category

    def create(self, db: Session, name: str, region: str, type: str) -> Category:
        category: Category = None

        try:
            category = self.crud_category.create(db, name, region, type) 
        except IntegrityError as e:
            if "UNIQUE constraint failed: categories.name" in str(e):
                raise NameAlreadyExists()
        
        return category
    
    def get_category_by_name(self, db: Session, name: str) -> Category:
        category: Optional[Category] = self.crud_category.get_category_by_name(db, name)
        if category is None:
            raise InvalidCategoryName()

        return category
    
    def get_category_ids_by_type(self, db: Session, type: str) -> List[int]:
        categories: List[int] = self.crud_category.get_category_ids_by_type(db, type)
        return categories
    
    def get_distinct_regions(self, db: Session) -> List[str]:
        regions: List[str] = self.crud_category.get_distinct_regions(db)
        return regions
    
    def get_category_ids_by_region(self, db: Session, region: str) -> List[int]:
        category_ids: List[int] = self.crud_category.get_category_ids_by_region(db, region)
        return category_ids


    

category_service = CategoryService(crud_category)


