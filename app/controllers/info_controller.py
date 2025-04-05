from flask import jsonify
from ..models.MyInfo import MyInfo
# from app.models.user import User  # Asumiendo que tienes modelos separados

def get_basic_info():
    my_info = MyInfo.query.all()
    return jsonify(my_info)


def get_hobbies():
    #...
    return

def get_proyectos():
    # ...
    return

def get_logros():
    # ...
    return

def get_memes():
    # ...
    return
