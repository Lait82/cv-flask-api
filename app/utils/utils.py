from flask import current_app
from logging import DEBUG
from ..models import BaseModel

# PRIVATES
def _is_model_instance(obj):
    return BaseModel.BaseModel in obj.__class__.__mro__

# PUBLICS
def to_serializable(lst: list) -> list:
    ret = []
    for obj in lst:
        if (not _is_model_instance(obj)):
            raise TypeError('No se puede convertir a lista serializable.')
        ret.append(obj.to_dict())
    return ret
