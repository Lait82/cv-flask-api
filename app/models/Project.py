from sqlalchemy import String, Column, Integer
from .BaseModel import BaseModel
from .InterestProject import interest_project
from ..extensions import db

class Project(BaseModel):
    __tablename__ = 'projects'  # Nombre de la tabla en la base de datos
    id = Column(Integer(), primary_key=True)
    name = Column(String(64))
    description = Column(String(512), primary_key=True)
    github_url = Column(String(128))
    banner_img = Column(String(32))

    interests = db.relationship(
        'Interest',
        secondary=interest_project,
        back_populates='projects'
    )

    def __repr__(self):
        return f'<Project {self.name}>'