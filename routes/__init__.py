from flask import Blueprint
routes = Blueprint('routes', __name__)

from .dynamodb import *
from .rds import *
from .monitoring import *