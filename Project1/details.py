import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




db = SQLAlchemy()
class Registration(db.Model):
    __tablename__ = "Details"
    # Firstname = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, unique = True, primary_key = True)
    Password = db.Column(db.String, nullable = False)
    dt = db.Column(db.DateTime, nullable= False)
    def _init_(self,Email,Password,dt):
        self.Email = Email
        self.Password = Password
        self.dt = datetime.now()
    
