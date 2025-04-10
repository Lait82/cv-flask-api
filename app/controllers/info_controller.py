from flask import jsonify, current_app
from logging import DEBUG
from ..utils import to_serializable
from ..extensions import db
from ..utils.enums import Interests as InterestsEnum

# Models
from ..models.MyInfo import MyInfo
from ..models.Interest import Interest
from ..models.Project import Project


def get_basic_info():
    my_info = MyInfo.query.all()
    data = to_serializable(my_info)
    return jsonify(data[0])


def get_interests():
    interests = Interest.query.all()
    data = to_serializable(interests)
    return jsonify(data)

def get_projects(interests):
    interest_ids = [
        InterestsEnum[interest].value
        for interest in interests
        if interest in InterestsEnum.__members__
    ]

    # Query
    query = db.session.query(Project)
    if interest_ids:
        query = (query
            .join(Project.interests)
            .filter(Interest.id.in_(interest_ids)))
    projects = query.distinct().all()
    
    projects = to_serializable(projects)

    return jsonify(projects)

def get_logros():
    # ...
    return

def get_memes():
    # ...
    return
