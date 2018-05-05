from . import *

class CourseController():


  ### POST ###

  @check.route('/course', methods=['POST'])
  def add_course():
    name = request.args['name']
    category = request.args['category']
    return jsonify(course_dao.add(name, category))


  ### GET ###

  @check.route('/course', methods=['GET'])
  def get_course():
    if 'name' in request.args:
      name = request.args['name']
      return jsonify(course_dao.get_by_name(name))
    elif 'category' in request.args:
      category = request.args['category']
      return jsonify(course_dao.get_by_category(category))

  @check.route('/course/all', methods=['GET'])
  def get_all_courses():
    return jsonify(course_dao.get_all())


  ### DELETE ###

  @check.route('/course', methods=['DELETE'])
  def delete_course():
    if 'name' in request.args:
      name = request.args['name']
      return jsonify(course_dao.delete_by_name(name))
    elif 'category' in request.args:
      category = request.args['category']
      return jsonify(course_dao.delete_by_category(category))
  
  @check.route('/course/all', methods=['DELETE'])
  def delete_all_courses():
    return jsonify(course_dao.delete_all())


  ### PUT ###

  @check.route('/course', methods=['PUT'])
  def modify_course():
    name = request.args['name']
    if 'new_name' in request.args:
      new_name = request.args['new_name']
      return jsonify(course_dao.modify_name(name, new_name))
    elif 'new_category' in request.args:
      new_category = request.args['new_category']
      return jsonify(course_dao.modify_category(name, new_category))


