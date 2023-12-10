from sqlalchemy.orm import Session
from typing import Optional, List

from app.models.category import Category

class CategoryCrud:

    def create(self, db: Session, name: str, region: str, type: str) -> Category:
        category = Category(name=name, region=region, type=type)
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    def get_category_by_id(self, db: Session, id: int) -> Optional[Category]:
        return db.query(Category).filter(Category.id == id).first()
    
    def get_category_by_name(self, db: Session, name: str) -> Optional[Category]:
        return db.query(Category).filter(Category.name == name).first()

    def get_categories_by_region(self, db: Session, region: str) -> List[Category]:
        return db.query(Category).filter(Category.region == region).all()

    def get_categories_by_type(self, db: Session, type: str) -> List[Category]:
        return db.query(Category).filter(Category.type == type).all()
    

crud_category = CategoryCrud() # instantiate CategoryCrud module