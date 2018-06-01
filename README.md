# Check (Backend) 

## Description
This repository contains the backend code to our HackDev challenge project for Cornell's Spring 2018 Principles of Backend Engineering Course (CS 1998, run by CU AppDev). We implemented the backend for an app that allows a user to keep track of tasks for different courses (link to frontend is [`here`](https://github.com/nanditamohan/check)). The backend was fully deployed during the HackDev challenge week. Backend contributors: Garima Kapila (gk347@cornell.edu), Riddhima Narravula (rrn23@cornell.edu)

## Tools/Technologies:
* Language: [`Python 2.7`](https://www.python.org/download/releases/2.7/)
* Database: [`MySQL`](https://www.mysql.com)
* Framework: [`Flask`](https://www.python.org)
* Deployment: [`Docker`](https://www.docker.com) and [`Google Cloud`](https://cloud.google.com/)

## HTTP Methods Supported
#### POST
Add a course/task instance

#### GET
Query for course/task instance(s)

#### DELETE 
Delete course/task instance(s)

#### PUT
Modify a course/task instance

## Organization

### File structure of the directory `./src`:

````bash
.
├── app
│   ├── __init__.py
│   ├── all.py
│   └── check
│       ├── __init__.py
│       ├── controllers
│       │   ├── __init__.py
│       │   ├── course_controller.py
│       │   └── task_controller.py
│       ├── dao
│       │   ├── __init__.py
│       │   ├── check_dao.py
│       │   ├── course_dao.py
│       │   └── task_dao.py
│       └── models
│           ├── __init__.py
│           ├── all.py
│           ├── course.py
│           └── task.py
├── config.py
├── manage.py
├── requirements.txt
├── run.py
└── test.py
````

## Tables

### Course
* name
* category

### Task
* name
* description
* due_date
* course_name

## Network IP Address: http://104.196.110.31

## Course Table Backend Endpoints + Methods/Outputs 

#### General Endpoint
http://104.196.110.31/check/course

#### Endpoint for getting all objects in table (GET)
http://104.196.110.31/check/course/all	

#### Add course with name and category (POST)
* Endpoint (General): http://104.196.110.31/check/course 
* Example Endpoint/Parameters: http://104.196.110.31/check/course?name=course1&category=category1

Output:
````
{
    "success": true
}
````

#### Get course with name (GET)
* Endpoint (General): http://104.196.110.31/check/course 
* Example Endpoint/Parameters: http://104.196.110.31/check/course?name=course1

Output: 
````
{
    "course": {
        "category": "category1",
        "name": "course1"
    }
}
````

#### Get courses with category (GET)
* Endpoint (General): http://104.196.110.31/check/course 
* Example Endpoint/Parameters: http://104.196.110.31/check/course?category=category1

Output: 
````
{
    "courses": [
        {
            "category": "category1",
            "name": "course1"
        }
    ]
}
````

#### Get all courses (GET)
* Endpoint (All): http://104.196.110.31/check/course/all 
* Example Endpoint/Parameters: http://104.196.110.31/check/course/all

Output: 
````
{
    "courses": [
        {
            "category": "category1",
            "name": "course1"
        },
        {
            "category": "category2",
            "name": "course2"
        }
    ]
}
````

#### Delete course with name (DELETE)
* Endpoint (General): http://104.196.110.31/check/course
* Example Endpoint/Parameters: http://104.196.110.31/check/course?name=course2

Output: 
````
{
    "success": true
}
````

#### Delete courses with category (DELETE)
* Endpoint (General): http://104.196.110.31/check/course
* Example Endpoint/Parameters: http://104.196.110.31/check/course?category=category2

Output:
````
{
    "success": true
}
````

#### Delete all courses (DELETE)
* Endpoint (All): http://104.196.110.31/check/course/all
* Example Endpoint/Parameters: http://104.196.110.31/check/course/all

Output:
````
{
    "success": true
}
````

#### Modify course by name (PUT)
* Endpoint (General): http://104.196.110.31/check/course
* Example Endpoint/Parameters: http://104.196.110.31/check/course?name=course3&new_name=course2

Output: 
````
{
    "success": true
}
````

#### Modify course by category (PUT)
* Endpoint (General): http://104.196.110.31/check/course
* Example Endpoint/Parameters: http://104.196.110.31/check/course?category=category2&new_category=category3

Output: 
````
{
    "success": true
}
````

## Task Table Backend Endpoints + Methods/Outputs

#### General Endpoint
http://104.196.110.31/check/task

#### Endpoint for getting all objects in table (GET)
http://104.196.110.31/check/task/all

#### Add task with name, description, due_date, and course_name (POST)
* Endpoint: http://104.196.110.31/check/task
* Example Endpoint/Parameters: http://104.196.110.31/check/task?name=name&description=desc&due_date=a&course_name=course1

Output:
````
{
    "success": true
}
````

#### Get task with name (GET)
* Endpoint: http://104.196.110.31/check/task
* Example Endpoint/Parameters: http://104.196.110.31/check/task?name=task1

Output: 
````
{
    "task": {
        "course_name": "course1",
        "description": "desc1",
        "due_date": "1-2-14",
        "name": "task1"
    }
}
````

#### Get tasks with due_date (GET)
* Endpoint: http://104.196.110.31/check/task
* Example Endpoint/Parameters: http://104.196.110.31/check/task?due_date=1-2-14

Output: 
````
{
    "tasks": [
        {
            "course_name": "course1",
            "description": "desc1",
            "due_date": "1-2-14",
            "name": "task1"
        }
    ]
}
````

#### Get tasks with course_name (GET)
* Endpoint: http://104.196.110.31/check/task
* Example Endpoint/Parameters: http://104.196.110.31/check/task?course_name=course1

Output: 
````
{
    "tasks": [
        {
            "course_name": "course1",
            "description": "desc1",
            "due_date": "1-2-14",
            "name": "task1"
        }
    ]
}
````

#### Get all tasks (GET)
* Endpoint: http://104.196.110.31/check/task/all
* Example Endpoint/Parameters: http://104.196.110.31/check/task/all

Output: 
````
{
    "tasks": [
        {
            "course_name": "a",
            "description": "a",
            "due_date": "a",
            "name": "a"
        },
        {
            "course_name": "course1",
            "description": "desc1",
            "due_date": "1-2-14",
            "name": "task1"
        }
    ]
}
````

#### Delete task by name (DELETE)
* Endpoint: http://104.196.110.31/check/task
* Example Endpoint/Parameters: http://104.196.110.31/check/task?name=task1

Output:
````
{
    "success": true
}
````

#### Modify task by name (PUT) 
* Endpoint: http://104.196.110.31/check/task
* Example Endpoint/Parameters: http://104.196.110.31/check/task?name=a&new_name=b

Output: 
````
{
    "success": true
}
````

#### Modify task by description (PUT)
* Endpoint: http://104.196.110.31/check/task
* Example Endpoint/Parameters: http://104.196.110.31/check/task?name=b&new_description=b

Output: 
````
{
    "success": true
}
````

#### Modify task by due_date (PUT) 
* Endpoint: http://104.196.110.31/check/task
* Example Endpoint/Parameters: http://104.196.110.31/check/task?name=b&new_due_date=cc

Output:
````
{
    "success": true
}
````

