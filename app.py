from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import CsrfProtect
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt

app = Flask(__name__)
app.secret_key = '12345'
csrf = CsrfProtect

ENV  = 'dev'

if ENV == 'dev':
   app.debug = True
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:andres601@localhost/LeeyApp'
else:
   app.debug = True
   app.config['SQLALCHEMY_DATABASE_URI'] = ''
   
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
   __tablename__ = 'user'
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   username = db.Column(db.String(25), unique=True)
   email = db.Column(db.String(100))
   passwor = db.Column(db.String(255))
    
   def __init__(self, username, email, password):
      self.username = username
      self.email = email
      self.passwor = password

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
   if request.method == 'POST':
      username = request.form['username'].lower()
      email = request.form['email']
      password = generate_password_hash(request.form['pw'], method="sha256")
      checkpassword = request.form['check-pw']
      
      if db.session.query(User).filter(User.username == username).count() == 0 :
         data = User(username=username, email=email, password=password)
         db.session.add(data)
         db.session.commit()
         
         return render_template('succes.html', name = username)
      else:
          return render_template('index.html', username_exist = True)

      return render_template('index.html')

if __name__=="__main__":
   db.create_all()
   app.run(debug=True, port=5000, host='0.0.0.0')