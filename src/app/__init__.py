from flask import Flask, render_template, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import os

# Configure Flask app
app = Flask(__name__, static_url_path='/static')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Database
db = SQLAlchemy(app)

# Import + Register Blueprints
# Workflow is as follows:
from app.check import check as check
app.register_blueprint(check)
