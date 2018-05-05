from . import *
from datetime import datetime


class Task(db.Model):
  _tablename_ = 'task'
  name        = db.Column(db.String(256), primary_key=True, nullable=False, unique=True)
  description = db.Column(db.String(256), nullable=True)
  due_date    = db.Column(db.String(256), nullable=True)
  course_name = db.Column(db.String(256), nullable=False)


  def __init__(self, **kwargs):
    self.name = kwargs.get('name', None)
    self.description = kwargs.get('description', None)
    self.due_date = kwargs.get('due_date', None)
    self.course_name = kwargs.get('course_name', None)