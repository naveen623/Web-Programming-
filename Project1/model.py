from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time



db = SQLAlchemy()
class Registration(db.Model):
    __tablename__ = "Registration"
    # Firstname = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, primary_key=True)
    Password = db.Column(db.String, nullable=False)
    datetime = db.Column(db.String, nullable= False)
    def _init_(self,Email,Password,datetime):
        self.Email = Email
        self.Password = Password
        self.datetime = datetime.now()
    
