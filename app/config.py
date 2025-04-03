import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', None)
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@db/{2}'.format(
        os.getenv('MYSQL_USER', None), 
        os.getenv('MYSQL_PASSWORD', None),
        os.getenv('MYSQL_DATABASE', None))
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    