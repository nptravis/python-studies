import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	# good practice to configure with environment variables that defaults if not set
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
			'sqlite:///' + os.path.join(basedir, 'app.db') 
	# signals the applicatione verythime a change is trying to be made to the database, not needed here
	SQLALCHEMY_TRACK_MODIFICATIONS = False