# Check (Backend) 

## LINK FOR FULL BACKEND README: https://github.com/gkapila/Check-Backend/

## BACKEND REPO THAT OUR SERVER USES: https://github.com/gkapila/Check-Backend6
* please look at files in that repo for what is being used by frontend and being run on the server (we did not want to edit that repo in case our server stops working)
* the backend repo you are looking at currently has our updated README file and some other fixed endpoints that are not actually in use by the frontend or being run on the server

## Description
This repository contains the backend code to our final project for Cornell's Spring 2018 Principles of Backend Engineering Course (CS 1998, run by CU AppDev). We implemented the backend for an app that allows a user to keep track of tasks for different courses.

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

### Tables

#### Course
Fields:
* name
* category

#### Task
Fields:
* name
* description
* due_date
* course_name

We used the Flask Boilerplate provided to us as a basis for the backend. The backend is fully deployed using Docker and Google Cloud Services.

## Backend Endpoints + Methods/Outputs

### Network IP Address
http://104.196.110.31

### Course Table Methods 
Two General Endpoints 
* General Endpoint: http://104.196.110.31/check/course
* Endpoints for getting all objects in table: http://104.196.110.31/check/course/all	

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

### Task Table Methods 
Two General Endpoints: 
* General Endpoint: http://104.196.110.31/check/task
* Endpoints for all objects in database: http://104.196.110.31/check/task/all

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

