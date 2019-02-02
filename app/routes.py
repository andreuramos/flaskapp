from app import app 
from flask import render_template, flash, redirect, url_for
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Andreu'}
	posts = [
		{
			'author': {'username': 'Andreu'},
			'body': 'Post content, here goes what the author wrote'
		},
		{
			'author': {'username': 'Marina'},
			'body': 'Another post with different content'
		}
	]
	return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if (form.validate_on_submit()):
		flash('Login Required for user {}, remember_me=()'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)
