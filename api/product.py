from models import Product, ProductSchema
from utils import validate_uuid, uuid_error
from config import db
import uuid
obj="Product"
def read_all():
    item = Product.query.order_by(Product.name).all()
    item_schema = ProductSchema(many=True)
    data = item_schema.dump(item).data
    return data

def create(req):
    id = req.get('id')
    if not validate_uuid(id, 4):
        return uuid_error(obj,"id")
    name=req.get('name')
    existing_item = Product.query.filter(Product.id == id).one_or_none()
    if id is None:
        id = uuid.uuid4()
        req['id']=id
    if existing_item is None:
        schema = ProductSchema()
        print(dir(schema))
        new_item = schema.load(req, session=db.session).data
        db.session.add(new_item)
        db.session.commit()
        data = schema.dump(new_item).data
        return data, 201