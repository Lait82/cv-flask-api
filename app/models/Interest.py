from sqlalchemy import Column, Integer, String
from .BaseModel import BaseModel
from ..extensions import db
from .InterestProject import interest_project


class Interest(BaseModel):
    __tablename__ = 'interests'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(32))
    years_of_practice = Column(Integer())
    level_or_degree = Column(String(120))
    notes = Column(String(512))

    projects = db.relationship(
        'Project',
        secondary=interest_project,
        back_populates='interests'
    )
    
    def __repr__(self):
        return f'<Interest {self.name}>'