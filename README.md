# Check (Backend)


## Description
This repository contains the backend code to our final project for Cornell's Spring 2018 Principles of Backend Engineering Course (CS 1998, run by CU AppDev).


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

The following shows the file structure of the directory `./src`:

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

## Tools/Technologies:
* Language: [`Python 2.7`](https://www.python.org/download/releases/2.7/)
* Database: [`MySQL`](https://www.mysql.com)
* Framework: [`Flask`](https://www.python.org)
* Deployment: [`Google Cloud`](https://cloud.google.com/)
