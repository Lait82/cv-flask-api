from app.extensions import db
from sqlalchemy import Column, Integer, String

class Interest(db.Model):
    __tablename__ = 'interests'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(32))
    years_of_practice = Column(Integer())
    level_or_degree = Column(String(120))
    notes = Column(String(64))
    
    def __repr__(self):
        return f'<Interest {self.name}>'