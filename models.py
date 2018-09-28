from datetime import datetime
from config import db, ma
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import ModelSchema


class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(postgresql.UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    products = relationship("Product", back_populates='category')

class Product(db.Model):
    __tablename__='Product'
    id = db.Column(postgresql.UUID, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.TEXT, nullable=True)
    provider = db.Column(db.String(200), nullable=False)
    barcode = db.Column(db.String(20), nullable=False)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    category_id=db.Column(postgresql.UUID, db.ForeignKey('Category.id'))
    category = relationship("Category", back_populates='products')

class CategorySchema(ModelSchema):
    class Meta:
        model = Category
        sqla_session=db.session


class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        sqla_session=db.session

