from flask import Blueprint
from app import *

# Check Blueprint
check = Blueprint('check', __name__, url_prefix='/check')

# Import all endpoints
from controllers.course_controller import *
from controllers.task_controller import *
