from flask import jsonify
from ..utils import to_serializable

# Models
from ..models.MyInfo import MyInfo
from ..models.Interest import Interest


def get_basic_info():
    my_info = MyInfo.query.all()
    data = to_serializable(my_info)
    return jsonify(data)


def get_interests():
    interests = Interest.query.all()
    data = to_serializable(interests)
    return jsonify(data)

def get_proyectos():
    # ...
    return

def get_logros():
    # ...
    return

def get_memes():
    # ...
    return
