from flask import render_template

# local modules
import config


# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api('swagger.yml')


# create a URL route in our application for "/"
@connex_app.route('/')
def home():
    return render_template("front.html")

@connex_app.route('/back')
def back():
    return render_template("back.html")