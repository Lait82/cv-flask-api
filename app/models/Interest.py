from app import db

class Interest(db.Model):
    __tablename__ = 'interests'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32))
    years_of_practice = db.Column(db.Integer())
    level_or_degree = db.Column(db.String(120))
    notes = db.Column(db.String(64))
    
    def __repr__(self):
        return f'<Interest {self.name}>'