from . import *

DB_COMMIT_ERROR_MESSAGE = 'Failure to complete DB transaction'


def to_dict(t): 
  return {
    'name': t.name,
    'description': t.description,
    'due_date': t.due_date,
    'course_name': t.course_name
  }


### ADD ###

def add(name, description, due_date, course_name):
  optional = get_by_name(name)['task']
  if optional is not None:
    return {'success': False}
  new = Task(
    name = name,
    description = description,
    due_date = due_date,
    course_name = course_name
  )
  check_dao.commit_model(new)
  return {'success': True}


### GET ###

def get_all():
  return {'tasks': [to_dict(task) for task in Task.query]}

def get_by_name(name):
  task = Task.query.filter_by(name=name).order_by(Task.name).first()
  if task != None:
    task = to_dict(task)
  return {'task': task}

def get_by_due_date(due_date):
  tasks = Task.query.filter_by(due_date=due_date).order_by(Task.name).all()
  tasks = [to_dict(task) for task in tasks]
  return {'tasks': tasks}

def get_by_course_name(course_name):
  tasks = Task.query.filter_by(course_name=course_name).order_by(Task.name).all()
  tasks = [to_dict(task) for task in tasks]
  return {'tasks': tasks}


### DELETE ###

def delete_by_name(name):
  optional = Task.query.filter_by(name=name).first()
  if optional is not None:
    check_dao.delete_model(optional)
    return {'success': True}
  else:
    return {'success': False}

def delete_by_due_date(due_date):
  try:
    tasks = Task.query.filter_by(due_date=due_date).all()
    check_dao.delete_models(tasks)
    return {'success': True}
  except:
    {'success': False}

def delete_by_course_name(course_name):
  try:
    tasks = Task.query.filter_by(course_name=course_name).all()
    check_dao.delete_models(tasks)
    return {'success': True}
  except:
    {'success': False}


### MODIFY ###

def modify_name(name, new_name):
  try:
    task = get_by_name(name)['task']
    delete_by_name(name)
    add(new_name, task['description'], task['due_date'], task['course_name'])
    return {'success': True}
  except:
    return {'success': False}

def modify_description(name, new_description):
  try:
    task = get_by_name(name)['task']
    delete_by_name(name)
    add(name, new_description, task['due_date'], task['course_name'])
    return {'success': True}
  except:
    {'success': False}

def modify_due_date(name, new_due_date):
  try:
    task = get_by_name(name)['task']
    delete_by_name(name)
    add(name, task['description'], new_due_date, task['course_name'])
    return {'success': True}
  except:
    {'success': False}

def modify_course_name(name, new_course_name):
  course = course_dao.get_by_name(name)['course']
  if course is None:
    return {'success': False}
  try:
    task = get_by_name(name)['task']
    delete_by_name(name)
    add(name, task['description'], task['due_date'], new_course_name)
    return {'success': True}
  except:
    {'success': False}
