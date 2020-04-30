import os

from flask import Flask, session,url_for,redirect
from flask import Flask,render_template,request,flash
from flask_session import Session
from  datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from model import *

app = Flask(__name__)
app.secret_key = 'any random string'
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
engine = create_engine(os.getenv("DATABASE_URL"))
Session(app)
db.init_app(app)

with app.app_context():
	db.create_all()

@app.route("/")
def index0():
	if 'email' in session and 'key' in session:
		return render_template("home.html")
	return redirect(url_for("register"))

  

@app.route("/register")
def index():    
    return render_template("Registration.html")

@app.route("/User",methods = ["GET","POST"])
def User():
    
    if request.method == "POST":
        name = request.form.get("fname")
        email = request.form.get("Email")
        pswd  = request.form.get("password")
        register = Registration(Email = email, Password = pswd)
    
        
        db.session.add(register)
        db.session.commit()
        return render_template("User.html")
    return render_template("error.html", errors = "Details are already given")
    
@app.route("/admin")

def Member():
      """List all users."""
     
      Member = Registration.query.all()
      return render_template("show.html", Member = Member)

@app.route("/auth",methods = ["GET","POST"])
def auth():
    if request.method == "POST":
        email = request.form.get('Email')
        pswd = request.form.get('password')

        userData = Registration.query.filter_by(Email=email).first()

        if userData is not None:
            if userData.Email == email and userData.Password == pswd:
                session['email'] = request.form['email']
            else:
                return render_template("Registration.html", message="username/password is incorrect!!")
        else:
            return render_template("Registration.html", message="Account doesn't exists, Please register!")
    else:
        return "<h1>Please login/register instead.</h1>"
 

@app.route('/logout')
def logout():
   session.pop('Email', None)
   return redirect(url_for('index0'))  
