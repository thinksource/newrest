from flask import make_response, abort,jsonify
from config import db
from models import Category, CategorySchema
import uuid
def read_all():
    cate = Category.query.order_by(Category.name).all()
    cate_schema = CategorySchema(many=True)
    data = cate_schema.dump(cate).data
    return data
def read_one(category_id):
    cate = Category.query.filter(Category.id == category_id).one_or_none()
    if cate is not None:
        cate_schema = CategorySchema()
        data = cate_schema.dump(cate).data
        return data
    else:
        message = 'Category do not found for Id:{id}'.format(id=category_id)
        abort(404, jsonify(message=message))

def create(category):
    id = category.get('id')
    name=category.get('name')
    existing_cate = Category.query.filter(Category.id == id).one_or_none()
    if id is None:
        id = uuid.uuid4()
        category['id']=id
    print(category)    
    if existing_cate is None:
        schema = CategorySchema()
        print(dir(schema))
        new_cate = schema.load(category, session=db.session).data
        db.session.add(new_cate)
        db.session.commit()
        data = schema.dump(new_cate).data
        return data, 201
        
    else:
        message= 'Category {id}, {name} exists already'.format(id=id, name=name)
        abort(409,jsonify(message=message))

def update(category_id, category):
    updata_item = Category.query.filter(Category.id == category_id).one_or_none()
    if updata_item is not None:
        schema = CategorySchema()
        update = schema.load(category, session=db.session).data
        update.id = updata_item.id
        db.session.merge(update)
        db.session.commit()
        data = schema.dump(update).data
        data.session.commit()

    else:
        message='Category not found for Id: {c_id}'.format(c_id=category_id)
        abort(404, jsonify(message=message))

def delete(category_id):
    cate = Category.query.filter(Category.id == category_id).one_or_none()

    if cate is not None:
        db.session.delete(cate)
        db.session.commit()
        message='Category {id} deleted'.format(id=category_id)
        return jsonify(message=message), 200

    # Otherwise, nope, didn't find that person
    else:
        message="Category not found for Id:{id}".format(id={category_id})
        abort(404, jsonify(message=message))