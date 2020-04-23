import os

from flask import Flask, session,url_for,redirect
from flask import Flask,render_template,request,flash
from flask_session import Session
from  datetime import datetime
# from Database import *

app = Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route('/')
def indexed():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"
  

@app.route("/register")
def index():    
    return render_template("Registration.html")

@app.route("/User",methods = ["GET","POST"])
def User():
    
    # Registration.query.all()
    name = request.form.get("fname")
    email = request.form.get("Email")
    pswd  = request.form.get("password")
    # register = Registration(Firstname =  name ,Email=email,Password = pswd,datetime = str(datetime.now()))
    
    try:
        # db.session.add(register)
        # db.session.commit()
        return render_template("User.html",f=name,email = email)
        
    except Exception :
	    return render_template("error.html", errors = "Details are already given")


                    
        
   
        
    


    

  



   


            
