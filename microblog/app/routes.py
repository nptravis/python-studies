# this is a view function
from flask import render_template
from app import app
from app.forms import LoginForm

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

# the methods argument tell it to accept get and post, overriding the default which is just post
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)
	# passing the form object created in the line above (and shown on the right side) to the template with the name form (shown on the left)
