#!/usr/bin/python3

'''
a pythons scriptthat uses the rest api orm the code
for a given emplyee id, it returns information about his/her TODO list progress
'''

from requests import get
from sys import argv

if __name__ == '__main__':
    _id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)
    response = get(base_url)
    employee_name = response.json().get('name')

    task_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(_id)
    response = get(task_url)
    tasks = response.json()

    done_tasks = 0
    total_tasks = []

    for task in tasks:
        if task.get('completed'):
            total_tasks.append(task)
            done_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.format(employee_name, done_tasks, len(tasks)))

    for task in total_tasks:
        print('\t {}'.format(task.get('title')))
