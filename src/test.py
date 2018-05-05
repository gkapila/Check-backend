from app import app,db,base
import simplejson as json
import unittest


class test(unittest.TestCase):


  #################
  #     Links     #
  #################

  def post(self, input_data, modelType):
    args = self.input_dict_to_args(input_data)
    link = '/check/%s?%s' % (modelType, args)
    return self.app.post(link, follow_redirects=False)

  def get(self, input_data, modelType):
    args = self.input_dict_to_args(input_data)
    link = '/check/%s?%s' % (modelType, args)
    return self.app.get(link, follow_redirects=False)

  def get_all(self, modelType):
    link = '/check/%s/all' % (modelType)
    return self.app.get(link, follow_redirects=False)

  def delete(self, input_data, modelType):
    args = self.input_dict_to_args(input_data)
    link = '/check/%s?%s' % (modelType, args)
    return self.app.delete(link, follow_redirects=False)

  def delete_all(self, modelType):
    link = '/check/%s/all' % (modelType)
    return self.app.delete(link, follow_redirects=False)
  
  def put(self, input_data, modelType):
    args = self.input_dict_to_args(input_data)
    link = '/check/%s?%s' % (modelType, args)
    return self.app.put(link, follow_redirects=False)
  


  ##################
  #     Course     #
  ##################

  def test_add_course(self):
    input_data = dict(name='Course1', category='Category1')
    result = json.loads(self.post(input_data, 'course').data)
    assert(result['success'] == True)
    input_data = dict(name='Course2', category='Category2')
    result = json.loads(self.post(input_data, 'course').data)
    assert(result['success'] == True)
    input_data = dict(name='Course2', category='Category3')
    result = json.loads(self.post(input_data, 'course').data)
    assert(result['success'] == False)
    input_data = dict(name='Course3', category='Category2')
    result = json.loads(self.post(input_data, 'course').data)
    assert(result['success'] == True)


  def test_get_course(self):
    input_data1 = dict(name='Course1', category='Category1')
    input_data2 = dict(name='Course2', category='Category2')
    input_data3 = dict(name='Course3', category='Category2')
    input_data4 = dict(name='Course4', category='Category2')

    self.post(input_data1, 'course').data
    self.post(input_data2, 'course').data
    self.post(input_data3, 'course').data
    self.post(input_data4, 'course').data

    result = json.loads(self.get(dict(name='Course1'), 'course').data)
    assert(result['course']['name'] == 'Course1')
    assert(result['course']['category'] == 'Category1')
    
    result = json.loads(self.get(dict(name='Course3'), 'course').data)
    assert(result['course']['name'] == 'Course3')
    assert(result['course']['category'] == 'Category2')


  def test_get_courses_by_category(self):
    input_data1 = dict(name='Course1', category='Category1')
    input_data2 = dict(name='Course2', category='Category2')
    input_data3 = dict(name='Course3', category='Category2')
    input_data4 = dict(name='Course4', category='Category2')

    self.post(input_data1, 'course').data
    self.post(input_data2, 'course').data
    self.post(input_data3, 'course').data
    self.post(input_data4, 'course').data

    result = json.loads(self.get(dict(category='Category1'), 'course').data)
    assert(len(result['courses']) == 1)
    assert(result['courses'] == [input_data1])
    
    result = json.loads(self.get(dict(category='Category2'), 'course').data)
    assert(len(result['courses']) == 3)
    assert(result['courses'] == [input_data2, input_data3, input_data4])


  def test_get_all_courses(self):
    input_data1 = dict(name='Course1', category='Category1')
    input_data2 = dict(name='Course2', category='Category2')
    input_data3 = dict(name='Course3', category='Category2')
    input_data4 = dict(name='Course4', category='Category2')

    self.post(input_data1, 'course').data
    self.post(input_data2, 'course').data
    self.post(input_data3, 'course').data
    self.post(input_data4, 'course').data

    result = json.loads(self.get_all('course').data)
    assert(len(result['courses']) == 4)
    courses_list = [input_data1, input_data2, input_data3, input_data4]
    assert(result['courses'] == courses_list)


  def test_delete_course_by_name(self):
    input_data1 = dict(name='Course1', category='Category1')
    input_data2 = dict(name='Course2', category='Category2')
    
    self.post(input_data1, 'course').data
    self.post(input_data2, 'course').data

    result = json.loads(self.delete(dict(name='Course1'), 'course').data)
    assert (result['success'] == True)
    result = json.loads(self.get_all('course').data)
    assert(result['courses'] == [input_data2])
    result = json.loads(self.delete(dict(name='Course1'), 'course').data)
    assert (result['success'] == False)
    result = json.loads(self.get_all('course').data)
    assert(result['courses'] == [input_data2])
    result = json.loads(self.delete(dict(name='Course2'), 'course').data)
    assert (result['success'] == True)
    result = json.loads(self.get_all('course').data)
    assert(result['courses'] == [])


  def test_delete_courses_by_category(self):
    input_data1 = dict(name='Course1', category='Category1')
    input_data2 = dict(name='Course2', category='Category2')
    input_data3 = dict(name='Course3', category='Category2')
    input_data4 = dict(name='Course4', category='Category2')

    self.post(input_data1, 'course').data
    self.post(input_data2, 'course').data
    self.post(input_data3, 'course').data
    self.post(input_data4, 'course').data

    result = json.loads(self.delete(dict(category='Category1'), 'course').data)
    assert (result['success'] == True)
    result = json.loads(self.get_all('course').data)
    assert(result['courses'] == [input_data2, input_data3, input_data4])
    result = json.loads(self.delete(dict(category='Category2'), 'course').data)
    assert (result['success'] == True)
    result = json.loads(self.get_all('course').data)
    assert(result['courses'] == [])
    result = json.loads(self.delete(dict(category='Category2'), 'course').data)
    assert (result['success'] == False)
    result = json.loads(self.get_all('course').data)
    assert(result['courses'] == [])

  
  def test_delete_all_courses(self):
    input_data1 = dict(name='Course1', category='Category1')
    input_data2 = dict(name='Course2', category='Category2')
    input_data3 = dict(name='Course3', category='Category2')
    input_data4 = dict(name='Course4', category='Category2')

    self.post(input_data1, 'course').data
    self.post(input_data2, 'course').data
    self.post(input_data3, 'course').data
    self.post(input_data4, 'course').data

    result = json.loads(self.delete_all('course').data)
    assert (result['success'] == True)
    result = json.loads(self.get_all('course').data)
    assert(result['courses'] == [])
    result = json.loads(self.delete_all('course').data)
    assert (result['success'] == False)
  

  def test_modify_course_name(self):
    input_data1 = dict(name='Course1', category='Category1')
    input_data2 = dict(name='Course2', category='Category2')

    self.post(input_data1, 'course').data
    self.post(input_data2, 'course').data

    new_data1 = dict(name='Course1', new_name='Course101')
    new_course = dict(name='Course101', category='Category1')
    
    result = json.loads(self.put(new_data1,'course').data)
    assert (result['success'] == True)
    result = json.loads(self.get_all('course').data)
    assert(result['courses'] == [new_course, input_data2])


  def test_modify_course_category(self):
    input_data1 = dict(name='Course1', category='Category1')
    input_data2 = dict(name='Course2', category='Category2')

    self.post(input_data1, 'course').data
    self.post(input_data2, 'course').data

    new_data1 = dict(name='Course1', new_category='Category101')
    new_course = dict(name='Course1', category='Category101')

    result = json.loads(self.put(new_data1, 'course').data)
    assert (result['success'] == True)
    result = json.loads(self.get_all('course').data)
    assert(result['courses'] == [new_course, input_data2])  



  ##################
  #      Task      #
  ##################


  def test_add_task(self):
    input_course1 = dict(name='Course1', category='Category1')
    self.post(input_course1, 'course').data

    input_task1 = dict(name='Task1', description='', due_date='1/1/1', course_name='Course1')

    result = json.loads(self.post(input_task1, 'task').data)
    assert(result['success'] == True)
    result = json.loads(self.get_all('task').data)
    assert(result['tasks'][0]['name'] == input_task1['name'])

    result = json.loads(self.post(input_task1, 'task').data)
    assert(result['success'] == False)
    result = json.loads(self.get_all('task').data)


  def test_get_task_by_name(self):
    input_course1 = dict(name='Course1', category='Category1')
    self.post(input_course1, 'course').data

    input_task1 = dict(name='Task1', description='', due_date='1/1/1', course_name='Course1')
    input_task2 = dict(name='Task2', description='', due_date='1/2/1', course_name='Course1')

    self.post(input_task1, 'task').data
    self.post(input_task2, 'task').data

    result = json.loads(self.get(dict(name='Task1'), 'task').data)
    assert(result['task']['name'] == 'Task1')
    result = json.loads(self.get(dict(name='Task2'), 'task').data)
    assert(result['task']['name'] == 'Task2')


  def test_get_tasks_by_due_date(self):
    input_course1 = dict(name='Course1', category='Category1')
    self.post(input_course1, 'course').data

    input_task1 = dict(name='Task1', description='', due_date='1/1/1', course_name='Course1')
    input_task2 = dict(name='Task2', description='', due_date='1/2/1', course_name='Course1')
    input_task3 = dict(name='Task3', description='', due_date='1/2/1', course_name='Course1')

    self.post(input_task1, 'task').data
    self.post(input_task2, 'task').data
    self.post(input_task3, 'task').data

    result = json.loads(self.get(dict(due_date='1/1/1'), 'task').data)
    assert(len(result['tasks']) == 1)
    result = json.loads(self.get(dict(due_date='1/2/1'), 'task').data)
    assert(len(result['tasks']) == 2)


  def test_get_tasks_by_course_name(self):
    input_course1 = dict(name='Course1', category='Category1')
    input_course2 = dict(name='Course2', category='Category1')
    input_course3 = dict(name='Course3', category='Category1')
    
    self.post(input_course1, 'course').data
    self.post(input_course2, 'course').data
    self.post(input_course3, 'course').data

    input_task1 = dict(name='Task1', description='', due_date='1/1/1', course_name='Course1')
    input_task2 = dict(name='Task2', description='', due_date='1/2/1', course_name='Course1')
    input_task3 = dict(name='Task3', description='', due_date='1/2/1', course_name='Course2')

    self.post(input_task1, 'task').data
    self.post(input_task2, 'task').data
    self.post(input_task3, 'task').data

    result = json.loads(self.get(dict(course_name='Course1'), 'task').data)
    assert(len(result['tasks']) == 2)
    result = json.loads(self.get(dict(course_name='Course2'), 'task').data)
    assert(len(result['tasks']) == 1)
    result = json.loads(self.get(dict(course_name='Course3'), 'task').data)
    assert(len(result['tasks']) == 0)


  def test_modify_task_name(self):
    input_course1 = dict(name='Course1', category='Category1')
    
    self.post(input_course1, 'course').data

    input_task1 = dict(name='Task1', description='', due_date='1/1/1', course_name='Course1')
    input_task2 = dict(name='Task2', description='', due_date='1/2/1', course_name='Course1')

    self.post(input_task1, 'task').data
    self.post(input_task2, 'task').data

    result = json.loads(self.put(dict(name='Task1', new_name='Task101'), 'task').data)
    assert(result['success'] == True)
    result = json.loads(self.get_all('task').data)
    assert(result['tasks'][0]['name'] == 'Task101')
    assert(result['tasks'][1]['name'] == 'Task2')


  def test_modify_task_description(self):
    input_course1 = dict(name='Course1', category='Category1')
    
    self.post(input_course1, 'course').data

    input_task1 = dict(name='Task1', description='', due_date='1/1/1', course_name='Course1')
    input_task2 = dict(name='Task2', description='', due_date='1/2/1', course_name='Course1')

    self.post(input_task1, 'task').data
    self.post(input_task2, 'task').data

    result = json.loads(self.put(dict(name='Task1', new_description='hi'), 'task').data)
    assert(result['success'] == True)
    result = json.loads(self.get_all('task').data)
    assert(result['tasks'][0]['description'] == 'hi')
    assert(result['tasks'][1]['description'] == '')


  def test_modify_task_due_date(self):
    input_course1 = dict(name='Course1', category='Category1')
    
    self.post(input_course1, 'course').data

    input_task1 = dict(name='Task1', description='', due_date='1/1/1', course_name='Course1')
    input_task2 = dict(name='Task2', description='', due_date='1/2/1', course_name='Course1')

    self.post(input_task1, 'task').data
    self.post(input_task2, 'task').data

    result = json.loads(self.put(dict(name='Task2', new_due_date='10/10/10'), 'task').data)
    assert(result['success'] == True)
    result = json.loads(self.get_all('task').data)
    assert(result['tasks'][0]['due_date'] == '')
    assert(result['tasks'][1]['due_date'] == 'Sun, 10 Oct 2010 00:00:00 GMT')


  def test_modify_task_course_name(self):
    input_course1 = dict(name='Course1', category='Category1')
    input_course2 = dict(name='Course2', category='Category1')

    self.post(input_course1, 'course').data
    self.post(input_course2, 'course').data

    input_task1 = dict(name='Task1', description='', due_date='1/1/1', course_name='Course1')
    input_task2 = dict(name='Task2', description='', due_date='1/2/1', course_name='Course1')

    self.post(input_task1, 'task').data
    self.post(input_task2, 'task').data

    result = json.loads(self.put(dict(name='Task2', new_course_name='Course2'), 'task').data)
    assert(result['success'] == True)
    result = json.loads(self.put(dict(name='Task2', new_course_name='Course3'), 'task').data)
    assert(result['success'] == False)
    result = json.loads(self.get_all('task').data)
    assert(result['tasks'][0]['course_name'] == 'Course1')
    assert(result['tasks'][1]['course_name'] == 'Course2')



  ##################
  # Helper Methods #
  ##################

  def input_dict_to_args(self, input_dict):
    return '&'.join(['%s=%s' % tup for tup in input_dict.items()])

  def setUp(self):
    self.app = app.test_client()
    self.app.testing = True
    self.app_context = app.app_context()
    self.app_context.push()
  
  def commit(self):
    try:
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      print(e)

  def tearDown(self):
    db.session.execute('DELETE FROM task;')
    self.commit()
    db.session.execute('DELETE FROM course;')
    self.commit()
    self.app_context.pop()


if __name__ == '__main__':
  unittest.main()
