from models import Product
from utils import validate_uuid, uuid_notvalidate,uuid_notfound, already_exist
from config import db
from flask import jsonify
import uuid
obj="Product"
def read_all():
    items = Product.query.order_by(Product.name).all()
    # data = item_schema.dump(item).data
    res=[]
    for item in items:
        res.append(item.to_dict(rel=True))
    return jsonify(res)

def read(product_id):
    if not validate_uuid(product_id, 4):
        return uuid_notvalidate(obj, product_id)
    else:
        existing_item = Product.query.filter(Product.id == product_id).one_or_none()
        if existing_item is None:
            return uuid_notfound(obj, product_id)
        else:
            return jsonify(existing_item.to_dict())

def create(product):
    id = product.get('id') if product.get('id') else str(uuid.uuid4())
    if not validate_uuid(id, 4):
        return uuid_notvalidate(obj, "id")
    while True:
        existing_item = Product.query.filter(Product.id == id).one_or_none()
        if existing_item is None:
            product['id'] = id
            break
        else:
            id = str(uuid.uuid4())
            
    item = Product.create(**product)
    return jsonify(item.to_dict()), 201


def update(product_id, product):
    id = product.get('id')
    if not validate_uuid(id, 4):
        return uuid_notvalidate(obj, "id")
    existing_item = Product.query.filter(Product.id == id).one_or_none()
    if existing_item is None:
        return uuid_notfound(obj, 'id')
    else:
        existing_item.update(**product)
        return jsonify(existing_item.to_dict()), 201

def delete(product_id):
    if not validate_uuid(product_id, 4):
        return uuid_notvalidate(obj, "id")
    existing_item = Product.query.filter(Product.id == product_id).one_or_none()
    if existing_item is None:
        return uuid_notfound(obj, 'id')
    else:
        existing_item.delete()
        msg = "{} with id({}) already delete".format(obj, product_id)
        return jsonify(message=msg)
    
        