from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flaskapp import User 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///students.sqlite3"
db = SQLAlchemy(app)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/dbtest')
def dbtest():
	

	db.create_all()
	return render_template('db_test.html')

if __name__ == '__main__':
	app.run(debug=True)