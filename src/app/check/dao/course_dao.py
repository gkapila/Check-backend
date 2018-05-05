from . import *

DB_COMMIT_ERROR_MESSAGE = 'Failure to complete DB transaction'


def to_dict(c): 
  return {
    'name': c.name,
    'category': c.category
  }


### ADD ###

def add(name, category):
  optional = get_by_name(name)['course']
  if optional is not None:
    return {'success': False}
  new = Course(name = name, category = category)
  check_dao.commit_model(new)
  return {'success': True}


### GET ###

def get_all():
  return {'courses': [to_dict(course) for course in Course.query]}

def get_by_name(name):
  course = Course.query.filter_by(name=name).first()
  if course != None:
    course = to_dict(course)
  return {'course': course}

def get_by_category(category):
  courses = Course.query.filter_by(category=category).order_by(Course.name).all()
  courses = [to_dict(course) for course in courses]
  return {'courses': courses}


### DELETE ###

def delete_all():
  query = Course.query.all()
  if len(query) > 0:
    check_dao.delete_models(query)
    return {'success': True}
  else:
    return {'success': False}

def delete_by_name(name):
  optional = Course.query.filter_by(name=name).first()
  if optional is not None:
    check_dao.delete_model(optional)
    return {'success': True}
  else:
    return {'success': False}

def delete_by_category(category):
  courses = Course.query.filter_by(category=category).all()
  if len(courses) > 0:
    check_dao.delete_models(courses)
    return {'success': True}
  else:
    return {'success': False}


### MODIFY ###

def modify_name(name, new_name):
  try:
    category = get_by_name(name)['course']['category']
    delete_by_name(name)
    add(new_name, category)
    return {'success': True}
  except:
    return {'success': False}

def modify_category(name, new_category):
  try:
    delete_by_name(name)
    add(name, new_category)
    return {'success': True}
  except:
    return {'success': False}

