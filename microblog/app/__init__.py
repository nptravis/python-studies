#  creates the application object as an instance of class Flask imported from the flask package
from flask import Flask 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

 
app = Flask(__name__) # set to the 'name' of the module which it is used
app.config.from_object(Config)
# create a database instance, most extentions are initialized as these two
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models # different URL's the application implements

