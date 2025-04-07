from sqlalchemy import String, Column, DateTime, Table, Integer, ForeignKey
from .BaseModel import BaseModel

interest_project = Table(
    'interest_project',
    BaseModel.metadata,
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
    Column('interest_id', Integer, ForeignKey('interests.id'), primary_key=True)
)