
from flask_script import Manager, Shell, Server, Command
from flask_migrate import MigrateCommand, Migrate
from flask_sqlalchemy import SQLAlchemy
from models import Category
# local modules
from app import connex_app
from config import db

def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': connex_app, 'db': db}

manager=Manager(connex_app.app)

@manager.command
def runserver():
    connex_app.run(debug=True)

@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main(['tests', '-q'])
    return exit_code

manager.add_command('server', Server(host="0.0.0.0", port=5000))
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()