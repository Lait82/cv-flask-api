from flask import Blueprint, request, current_app, jsonify
from logging import DEBUG
from app.controllers import contact_controller
from app.controllers import info_controller

blueprint = Blueprint('api', __name__)


# Contact
@blueprint.route('/contact', methods=['POST'])
def store_contact():
    data = request.get_json()
    current_app.logger.setLevel(DEBUG)
    current_app.logger.info(data)

    # Generate valid payload
    valid_fields = [
        "name",
        "email",
        "url",
        "company",
        "contact_message"
    ]
    payload = {}
    for field in valid_fields:
        payload[field] = data.get(field)
    
    current_app.logger.info(payload)

    return contact_controller.store_contact(payload)


# Info
@blueprint.route('/basic_info', methods=['GET'])
def get_basic_info():
    return info_controller.get_basic_info()

# Info
@blueprint.route('/interests', methods=['GET'])
def get_interests():
    return info_controller.get_interests()

# Info 
@blueprint.route('/projects', methods=['GET'])
def get_projects():
    interests = request.args.getlist('interests')

    return info_controller.get_projects(interests)



        



