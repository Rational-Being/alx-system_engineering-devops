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
    employee_name = response.json().get('username')

    task_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(_id)
    response = get(task_url)
    tasks = response.json()

    with open("{}.csv".format(_id), "w") as csvfile:
        for task in tasks:
            csvfile.write(
                '"{}","{}","{}","{}"\n'.format(
                    _id, employee_name, task.get("completed"), task.get("title")
                )
            )
