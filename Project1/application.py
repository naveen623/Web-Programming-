import os

from flask import Flask, session,url_for,redirect
from flask import Flask,render_template,request,flash
from  datetime import datetime

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
 
  
@app.route("/auth",methods = ["GET","POST"])
def authenticate():
    Registration.query.all()
    name = request.form.get("fname")
    email = request.form.get("Email")
    pswd  = request.form.get("password")
       
    try:
        Member = db.session.query(Registration).filter(Registration.Email == email).all()
        if len(Member) >0 :
            
            print(len(Member))
            print(Member[0].Password)
            if Member[0].Email == email and Member[0].Password == pswd:
                print(Member[0].Firstname)
                session['username'] = request.form.get("Email")
                return redirect(url_for('indexed'))   
            else:
                return render_template("error.html", errors = " Username / Password is incorrect")
        else:
            return "<h1> Please Login / Register </h1>"

    except Exception :
	    return render_template("error.html", errors = "Details are already given")
        
                    
        
   
        
    


    

  



   


            
