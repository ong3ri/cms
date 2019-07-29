from flask import Blueprint


cms = Blueprint(
    __name__,
    'cms'
)

from . import endpoints
