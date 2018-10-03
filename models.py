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
    desc = sa.Column(sa.String(200), nullable=True)
    customer = sa.Column(sa.String(80), nullable=False)
    totalpayment=sa.Column(sa.DECIMAL(14,2), nullable=False)
    status = sa.Column(sa.String(30), nullable=False)
    order_item = relationship("Order_Item", back_populates='order')

class Order_Item(MyModel):
    __taablename__ = 'Order_item'
    id = sa.Column(postgresql.UUID(as_uuid=True), primary_key=True)
    product_id=sa.Column(postgresql.UUID, sa.ForeignKey('Product.id'))
    # product = relationship("Product", back_populates='Product', uselist=False)
    amount = sa.Column(sa.Integer, nullable=False)
    item_price = sa.Column(sa.DECIMAL(10, 2), nullable=False)
    order_id=sa.Column(postgresql.UUID,sa.ForeignKey('order.id'))
    order = relationship("Order", back_populates='order_item', uselist=True)