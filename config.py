import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir+'\\swagger')

# Get the underlying Flask app instance
app = connex_app.app

# Build the Sqlite ULR for SqlAlchemy
# sqlite_url = 'sqlite:////' + os.path.join(basedir, 'people.db')
post_url='postgres://postgres:postgres@52.40.252.126:5432/ormproj'
# Configure the SqlAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = post_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def initdb(app):
    db = SQLAlchemy()
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    return db
    
# Create the SqlAlchemy db instance
db = initdb(app)

# Initialize Marshmallow
ma = Marshmallow(app)
