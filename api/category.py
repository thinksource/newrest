from models import Category
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
    if not validate_uuid(category_id, 4):
        return uuid_notvalidate("Category","id")
    cate = Category.query.filter(Category.id == category_id).one_or_none()
    if cate is not None:
        return jsonify(cate)
    else:
        message = 'Category do not found for Id:{id}'.format(id=category_id)
        return {message:message},404

def create(category):
    id = category.get('id')
    if not validate_uuid(id, 4):
        return uuid_notvalidate("Category","id")
    name=category.get('name')
    existing_cate = Category.query.filter(Category.id == id).one_or_none()
    if id is None:
        id = uuid.uuid4()
        category['id']=id    
    if existing_cate is None:
        cate = Category.create(**category)
        return jsonify(cate.to_dict()), 201
        
    else:
        message= 'Category {id}, {name} exists already'.format(id=id, name=name)
        return {message:message},409

def update(category_id, category):
    if not validate_uuid(category_id, 4):
        return uuid_notvalidate("Category","id")
    updata_item = Category.query.filter(Category.id == category_id).one_or_none()
    if updata_item is not None:
        updata_item.update(category)
        return jsonify(updata_item.to_dict()), 201

    else:
        message='Category not found for Id: {c_id}'.format(c_id=category_id)
        return {message:message},404

def delete(category_id):
    if not validate_uuid(category_id, 4):
        return uuid_notvalidate("Category","id")
    cate = Category.query.filter(Category.id == category_id).one_or_none()

    if cate is not None:
        cate.delete()
        message='Category {id} deleted'.format(id=category_id)
        return {message:message}

    # Otherwise, nope, didn't find that person
    else:
        message="Id:{id} is not correct format".format(id={category_id})
        return {message:message},404