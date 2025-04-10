from flask import Blueprint, request, current_app
from logging import DEBUG
from app.controllers import contact_controller
from app.controllers import info_controller

blueprint = Blueprint('api', __name__, url_prefix='/api')


# Contact
@blueprint.route('/contact', methods=['POST'])
def store_contact():
    data = request.get_json()
    current_app.logger.setLevel(DEBUG)
    current_app.logger.info(data)

    # Generate valid payload
    valid_fields = [
        "firstname",
        "lastname",
        "email",
        "url",
        "contact_message"
    ]
    payload = {}
    for field in valid_fields:
        payload[field] = data.get(field)
    


    current_app.logger.info(payload)

    return contact_controller.store_contact(data)


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



        



