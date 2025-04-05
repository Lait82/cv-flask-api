from flask import Blueprint, request
from app.controllers import contact_controller
from app.controllers import info_controller

blueprint = Blueprint('api', __name__, url_prefix='/api')


# Contact
@blueprint.route('/contact', methods=['POST'])
def get_users():
    data = request.get_json()
    return contact_controller.contact()


# Info
@blueprint.route('/basic_info', methods=['GET'])
def get_basic_info():
    return info_controller.get_basic_info()

