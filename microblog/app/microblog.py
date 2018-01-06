from app import app, db # The Flask application instance is called app and is a member of the app package
from app.models import User, Post

# this decorator registers the function as a shell context function
@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}