import os
import connexion
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connex_app = connexion.FlaskApp(__name__, static_folder="static/dist", \
    template_folder="static", specification_dir=basedir+'\\swagger')

# Get the underlying Flask app instance
app = connex_app.app
setattr(app, 'static_folder', basedir + '\\static\\build\\static')
setattr(app, 'template_folder', basedir+ '\\static\\build\\')

# Build the Sqlite ULR for SqlAlchemy
# sqlite_url = 'sqlite:////' + os.path.join(basedir, 'people.db')
file=open('db.txt','r')

# Configure the SqlAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = file.read()  #you should use your own data uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def initdb(app):
    db = SQLAlchemy()
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    return db
    
# Create the SqlAlchemy db instance
db = initdb(app)


