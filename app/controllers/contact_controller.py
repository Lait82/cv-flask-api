from flask import jsonify, current_app
from ..extensions import db
from ..models import Contact

def store_contact(data: dict):
    try:
        contact_record = Contact(**data)

        db.session.add(contact_record)
        db.session.commit()
        return ({}, 200)
    except Exception as e:
        current_app.logger.error(
            {
                "msg":"There was an error creating a contact.", 
                "data":e
            }
        )
        return (jsonify(message="There was an error creating the contact info. Please contact me on linkedin."), 500)