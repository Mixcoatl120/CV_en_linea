from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class names(db.Model):
    __tablename__ = 'nombres'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __init__(self,id,name):
        self.id = id
        self.name = name
        
