from sqlalchemy import String, Column, Text, Integer
from .BaseModel import BaseModel

class Contact(BaseModel):
    __tablename__ = 'contacts'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    email = Column(String(64))
    url = Column(String(256))
    company = Column(String(64))
    contact_message = Column(Text(2048))

    def __init__(self, name, email, url, company, contact_message):
        self.name = name
        self.email = email
        self.url = url
        self.company = company
        self.contact_message = contact_message

    def __repr__(self):
        return f'<Contact {self.name}>'