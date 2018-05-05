from course import *
from task import *

class CourseSchema(ModelSchema):
  class Meta(ModelSchema.Meta):
    model = Course
    
class TaskSchema(ModelSchema):
  class Meta(ModelSchema.Meta):
    model = Task