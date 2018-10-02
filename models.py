from dbmodels import MyModel
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
import sqlalchemy as sa
from sqlalchemy import orm
from uuid import UUID
class Category(MyModel):
    __tablename__ = 'Category'
    id = sa.Column(postgresql.UUID(as_uuid=True), primary_key=True)
    name = sa.Column(sa.String(80), nullable=False)
    products = relationship("Product", back_populates='category')


class Product(MyModel):
    __tablename__='Product'
    id = sa.Column(postgresql.UUID, primary_key=True)
    name = sa.Column(sa.String(80), nullable=False)
    desc = sa.Column(sa.TEXT, nullable=True)
    provider = sa.Column(sa.String(200), nullable=False)
    barcode = sa.Column(sa.String(50), nullable=False)
    price = sa.Column(sa.DECIMAL(10, 2), nullable=False)
    category_id= sa.Column(postgresql.UUID, sa.ForeignKey('Category.id'))
    category = relationship("Category", back_populates='products')

class Order(MyModel):
    __tablename__ = 'Order'
    id = sa.Column(postgresql.UUID, primary_key=True)
    