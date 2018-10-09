# Before you run.

If you do not want to install all python package in your path.
Please use 

```
virtualenv venv
venv\Scripts\activate.bat 
```

# How to run

1. pip install -r requirements.txt
2. set the config.py rewrite database url.

I use the postgresql database. If you use other type of database please adopt it.

3. python manage.py db init
4. python manage.py db migrate
5. python manage.py db upgrade
4. python manage.py runserver

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

PUT /order/{order_id}

### Order_Item

POST /order/{order_id}

DELETE /order_item/{item_id}

PUT /order_item/{item_id}

### Product 

GET /product

POST /product

PUT /product/{product_id}

DELETE /product/{product_id}


# About frontend

The frontend project is in static folder.
It require react and webpack to run.

## before running

1. install last version node js
2. install package:
```
npm install
```
3. build the frontend with webpack:

```
npm run build
```

# THe result expection

1. it will run on localhost:5000
2. the front end have two page:
    2.1. localhost:5000/  is the front-end work
    2.2. http://localhost:5000/backend/ is manager of product and category
