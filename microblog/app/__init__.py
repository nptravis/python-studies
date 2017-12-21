
#  creates the application object as an instance of class Flask imported from the flask package
from flask import Flask 

 
app = Flask(__name__) # set to the 'name' of the module which it is used

from app import routes # different URL's the application implements

## Vocabulary
# circular imports-putting one of the reciprocal imports at the bottom avoids the error that results from the mutual references between these two files.
# view functions- are mapped to one or more route URLs so that Flask knows what logic to execute when a client requests a given URL.
# decorators - A decorator modifies the function that follows it. A common pattern with decorators is to use them to register functions as callbacks for certain events