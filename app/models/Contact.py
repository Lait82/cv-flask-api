from sqlalchemy import String, Column, Text
from .BaseModel import BaseModel

class Contact(BaseModel):
    __tablename__ = 'contacts'
    
    name = Column(String(16))
    email = Column(String(32), primary_key=True)
    url = Column(String(128))
    company = Column(String(32))
    contact_message = Column(Text(1024))


    def __repr__(self):
        return f'<Contact {self.name}>'