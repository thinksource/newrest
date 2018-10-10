from models import Category, Product
from utils import validate_uuid, uuid_notvalidate
from config import db
from flask import jsonify

import uuid

def read_all():
    items = Category.query.order_by(Category.name).all()
    res=[]
    for item in items:
        res.append(item.to_dict())
    return jsonify(res)

def read_one(category_id):
    print(category_id)
    if not validate_uuid(category_id, 4):
        return uuid_notvalidate("Category","id")
    cate = Category.query.filter(Category.id == category_id).one_or_none()
    if cate is not None:
        return jsonify(cate.to_dict())
    else:
        message = 'Category do not found for Id:{id}'.format(id=category_id)
        return {"message":message},404

def create(category):
    id = category.get('id') if category.get('id') else str(uuid.uuid4())
    print(id)
    if not validate_uuid(id, 4):
        return uuid_notvalidate("Category","id")
    while True:
        existing_cate = Category.query.filter(Category.id == id).one_or_none()
        if existing_cate is None:
            category['id'] = id
            break
        else:
            id = str(uuid.uuid4())

    cate = Category.create(**category)
    return jsonify(cate.to_dict()), 201


def update(category_id, category):
    if not validate_uuid(category_id, 4):
        return uuid_notvalidate("Category","id")
    updata_item = Category.query.filter(Category.id == category_id).one_or_none()
    if updata_item is not None:
        updata_item.update(**category)
        return jsonify(updata_item.to_dict()), 201

    else:
        msg='Category not found for Id: {c_id}'.format(c_id=category_id)
        return {"message":msg},404

def delete(category_id):
    if not validate_uuid(category_id, 4):
        return uuid_notvalidate("Category","id")
    cate = Category.query.filter(Category.id == category_id).one_or_none()
    product = Product.query.filter(Product.category_id == category_id).one_or_none()
    if product is not None:
        msg = 'Can not delete category({}) when it has some production on it'.format(category_id)
        return {"message": msg}, 509
        
    elif cate is not None:
        cate.delete()
        msg='Category {id} deleted'.format(id=category_id)
        return {"message":msg}

    # Otherwise, nope, didn't find that person
    else:
        msg="Id:{id} do not found".format(id=category_id)
        return {"message":msg},404