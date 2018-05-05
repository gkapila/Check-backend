from . import *


class TaskController():


  ################
  #     POST     #
  ################

  @check.route('/task', methods=['POST'])
  def add_task():
    name = request.args['name']
    description = request.args['description']
    due_date = request.args['due_date']
    course_name = request.args['course_name']
    return jsonify(task_dao.add(name, description, due_date, course_name))


  #################
  #      GET      #
  #################

  @check.route('/task', methods=['GET'])
  def get_task():
    if 'name' in request.args:
      name = request.args['name']
      return jsonify(task_dao.get_by_name(name))
    elif 'due_date' in request.args:
      due_date = request.args['due_date']
      return jsonify(task_dao.get_by_due_date(due_date))
    elif 'course_name' in request.args:
      course_name = request.args['course_name']
      return jsonify(task_dao.get_by_course_name(course_name))

  @check.route('/task/all', methods=['GET'])
  def get_all_tasks():
    return jsonify(task_dao.get_all())


  ################
  #    DELETE    #
  ################

  @check.route('/task', methods=['DELETE'])
  def delete_task():
    if 'name' in request.args:
      name = request.args['name']
      return jsonify(task_dao.delete_by_name(name))
    elif 'due_date' in request.args:
      due_date = request.args['due_date']
      return jsonify(task_dao.delete_by_due_date(due_date))
    elif 'course_name' in request.args:
      course_name = request.args['course_name']
      return jsonify(task_dao.delete_by_course_name(course_name))
  
  @check.route('/task/all', methods=['DELETE'])
  def delete_all_tasks():
    return jsonify(task_dao.delete_all())


  #################
  #      PUT      #
  #################

  @check.route('/task', methods=['PUT'])
  def modify_task():
    name = request.args['name']
    if 'new_name' in request.args:
      new_name = request.args['new_name']
      return jsonify(task_dao.modify_name(name, new_name))
    elif 'new_description' in request.args:
      new_description = request.args['new_description']
      return jsonify(task_dao.modify_description(name, new_description))
    elif 'new_due_date' in request.args:
      new_due_date = request.args['new_due_date']
      return jsonify(task_dao.modify_due_date(name, new_due_date))
    elif 'new_course_name' in request.args:
      new_course_name = request.args['new_course_name']
      return jsonify(task_dao.modify_course_name(name, new_course_name))
