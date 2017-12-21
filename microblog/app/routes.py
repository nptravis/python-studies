# this is a view function
from flask import render_template
from app import app

@app.route('/') # decorators
@app.route('/index') # basically assign this url path to this function
def index():
	user = {'username': 'Nic'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The avengers movie was so cool!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)