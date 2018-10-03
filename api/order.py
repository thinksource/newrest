from models import Order, Order_Item
from flask import jsonify
from utils import uuid_notvalidate, validate_uuid, uuid_notfound
import uuid
from config import db
obj="Order"
def create(order):
    id = order.get('id') if order.get('id') else str(uuid.uuid4())
    # delete random repeat id
    while True:
        existing_item = Order.query.filter(Order.id == id).one_or_none()
        if existing_item is None:
            break
        else:
            id = str(uuid.uuid4())
    order['id'] = id
    amount, price = create_order_item(order['order_item'], order.get('id'))
    order.pop('order_item', None)
    order['totalpayment']=price
    item = Order.create(**order)
    item["add_items"]=amount
    return jsonify(item.to_dict()), 201

def list(customer):
    if customer:
        existing_item = Order.query.filter(Order.customer == customer).all()
        if len(existing_item) == 0:
            message = "No order from customer named:{}".format(customer)
            return jsonify(message=message), 202
        else:
            res = []
            for i in existing_item:
                res.append(i.to_dict())
            return jsonify(res)
    else:
        existing_item = Order.query.order_by(Order.id).all()
        res=[]
        for i in existing_item:
            res.append(i.to_dict())
        return jsonify(res)

def update_status(order_id, order):
    id = order.get('id')
    if not validate_uuid(id, 4):
        return uuid_notvalidate(obj, id)
    else:
        existing_item = Order.query.filter(Order.id == id).one_or_none()
        if existing_item is None:
            return uuid_notfound(obj, id)
        else:
            ret = existing_item.update(order)
            return jsonify(ret.to_dict()),201


def create_order_item(itemlist, orderid):
    existing_order = Order.query.filter(Order.id == orderid).one_or_none()
    if existing_order is None:
        return uuid_notfound(obj, id)
    else:
        item_count = 0
        price = 0
        for item in itemlist:
            item['order_id'] = orderid
            if item.get('id') is None:
                item['id'] = str(uuid.uuid4())
            if item.get('amount') is None:
                item['amount']=1 
            order_item = Order_Item(**item)
            order_item.save(False)
            item_count += item['amount']
            price+=item['item_price']*item['amount']
        return item_count, price


def order_details(order_id):
    if not validate_uuid(order_id, 4):
        return uuid_notvalidate(obj, order_id)
    else:
        existing_item = Order.query.filter(Order.id == order_id).one_or_none()
        if existing_item is None:
            return uuid_notfound(obj, id)
        else:
            return jsonify(existing_item)

def orderdetail_add(order_id, order_item):
    if not validate_uuid(order_id,4):
        return uuid_notvalidate(obj, order_id)
    else:
        existing_order = Order.query.filter(Order.id == order_id).one_or_none()
        if existing_order is None:
            return uuid_notfound(obj, order_id)
        else:
            itemid=order_item['id'] if order_item['id'] else uuid.uuid4()
            # delete random repeat id
            while True:
                existing_item = Order_Item.query.filter(Order_Item.id == itemid).one_or_none()
                if existing_item is None:
                    break
                else:
                    itemid = uuid.uuid4()
            if "amount" not in order_item:
                order_item["amount"] = 1
            order_item['order_id'] = order_id
            res=Order_Item.create(commit=False, **order_item)
            oldpayment = existing_order.get("totalpayment")
            newpayment=oldpayment+order_item['itemprice']*order_item["amount"]
            new_order = {"totalpayment": newpayment}
            existing_order.update(**new_order)
            return jsonify(res.to_dict()), 201
            

def orderdetail_update(item_id, order_item):
    id=order_item.get("id")
    order_id = order_item.get('order_id')
    if not validate_uuid(order_id, 4):
        return uuid_notvalidate(obj, order_id)
    elif not validate_uuid(id, 4):
        return uuid_notvalidate("Order_Item", id)
    else:
        existing_item = Order_Item.query.filter(Order_Item.id == id).one_or_none()
        existing_order = Order.query.filter(Order.id == order_id).one_or_none()
        
        if existing_item is None:
            return uuid_notfound("Order_Item", id)
        elif existing_order is None:
            return uuid_notfound(obj, order_id)
        else:
            if order_item['amount'] or order_item['item_price']:
                amount = order_item['amount'] if order_item['amount'] else existing_item['amount']
                price = order_item['item_price'] if order_item['item_price']>=0 else existing_item['item_price']
                existing_order["totalpayment"] += amount * price - existing_item['amount'] * existing_item['item_price']
                # commit = false is make the transation and commit next sql
                existing_order.update(commit=False, **existing_order.to_dict())
            existing_item.update(**order_item)
            return jsonify(existing_item.to_dict()), 201
    
def orderitem_delete(item_id):
    if not validate_uuid(item_id, 4):
        return uuid_notvalidate("Order_Item", item_id)
    else:
        existing_item = Order_Item.query.filter(Order_Item.id == id).one_or_none()
        if existing_item is None:
            return uuid_notfound("Order_Item", id)
        else:
            itemdict=existing_item.to_dict()
            existing_order = Order.query.filter(Order.id == itemdict['order_id']).one_or_none()
            if existing_order:
                existing_order["totalpayment"] -= itemdict["amount"] * itemdict['itemprice']
                existing_order.update(commit=False, **existing_order.to_dict())
            existing_item.delete()
        msg = "Order_Item with id({}) already deleted".format(item_id)
        return jsonify(message=msg)

    
