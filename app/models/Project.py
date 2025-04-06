from sqlalchemy import String, Column, Integer
from .BaseModel import BaseModel

class Project(BaseModel):
    __tablename__ = 'projects'  # Nombre de la tabla en la base de datos
    id = Column(Integer(), primary_key=True)
    name = Column(String(16))
    description = Column(String(32), primary_key=True)
    interest_id = Column(String(64))

    def __repr__(self):
        return f'<Project {self.name}>'