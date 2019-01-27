from app import app 
from flask import render_template

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
