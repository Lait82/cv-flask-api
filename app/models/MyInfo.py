from sqlalchemy import String, Column, DateTime
from .BaseModel import BaseModel

class MyInfo(BaseModel):
    __tablename__ = 'my_info'  # Nombre de la tabla en la base de datos
    
    firstname = Column(String(16))
    lastname = Column(String(16), nullable=False)
    email = Column(String(32), primary_key=True)
    linkedin_profile = Column(String(64))
    github_profile = Column(String(64))
    dob = Column(DateTime())


    def __repr__(self):
        return f'<MyInfo {self.email}>'