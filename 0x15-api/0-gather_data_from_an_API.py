#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress
use urllib or requests module
accepts an integer as a parameter, which is the employee ID
"""


import json
import requests
from sys import argv


def emp_information():
    """
    returns information about employee TODO list progress
    """
    TASK_TITLE = []
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0

    emp_id = int(argv[1])
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    for user in users.json():
        if user.get('id') == emp_id:
            EMPLOYEE_NAME = user.get('name')
            break

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    for task in tasks.json():
        if task.get('userId') == emp_id:
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF_TASKS
                                                          ))

    for title in TASK_TITLE:
        print("\t {}".format(title))


if __name__ == "__main__":
    emp_information()
