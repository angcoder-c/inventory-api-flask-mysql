import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@db:3306/inventory_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super_secret'