from . import *

class Course(db.Model):
  _tablename_ = 'course'
  name           = db.Column(db.String(256), primary_key=True, nullable=False, unique=True)
  category       = db.Column(db.String(256), nullable=False)

  def __init__(self, **kwargs):
    self.name = kwargs.get('name', None)
    self.category = kwargs.get('category', None)