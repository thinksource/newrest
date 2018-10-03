# Before you run.

If you do not want to install all python package in your path.
Please use 

```
virtualenv venv
venv\Scripts\activate.bat 
```

# How to run

1. npm install -r requirements.txt
2. set the config.py rewrite database url.

I use the postgresql database. If you use other type of database please adopt it.

3. npm manage.py db upgrade
4. npm manage.py runserver

You can see the swagger style rest-api and the swaggeer ui in:

http://localhost:5000/api/ui/

http://localhost:5000/api/swagger.json

The api requirement is base on /api path, so the correct way to visit api is

for instance:

/category is actually http://localhost:5000/api/category


# Models 

1. dbmodels.py in charge of serialization and deseralization, and some easy save update method.
2. 

# rest api

### Category
GET /category
POST /category
DELETE /category/{category_id}
GET /category/{category_id}
PUT /category/{category_id}


### Order 
GET /order
POST /order
GET /order/{order_id}
POST /order/{order_id}

### Order_Item 
DELETE /order_item/{item_id}
POST /order_item/{item_id}

### Product 
DELETE /product
GET /product
POST /product
PUT /product
