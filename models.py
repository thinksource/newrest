from datetime import datetime
from config import db, ma
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import ModelSchema


class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(postgresql.UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class CategorySchema(ModelSchema):
    class Meta:
        model = Category
        sqla_session=db.session


