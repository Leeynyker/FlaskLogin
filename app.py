from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import CsrfProtect
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS
import bcrypt

app = Flask(__name__)
app.secret_key = '12345'
csrf = CsrfProtect
# CORS = app

def conexion():
   return psycopg2.connect(
       host="localhost",
      #  database="loginDB",
       database="practica1",
       user = "postgres",
       password="andres601"
      )
   
@app.route('/')
def index():
   # conn = conexion()
   # cur = conn.cursor(cursor_factory=RealDictCursor)
   # cur.execute("SELECT * FROM usuarios")
   # rows = cur.fetchall() 
   # conn.close()
   # cur.close()
   # return render_template('index.html', rowse = rows)
   return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
   if request.method == 'POST':
      username = request.form['username']
      email = request.form['email']
      password = request.form['pw']
      checkpassword = request.form['check-pw']
      
           
      # print(username, email, password)
      return render_template('succes.html')
   
# @app.route("/insert")
# def insert_default():
#    conn = conexion()
#    cur = conn.cursor(cursor_factory=RealDictCursor)
#    cur.execute('w)
#    rows = cur.fetchall() 
#    conn.close()
#    cur.close()
#    return "The  default post was created"

if __name__=="__main__":
  app.run(debug=True, port=5000, host='0.0.0.0')