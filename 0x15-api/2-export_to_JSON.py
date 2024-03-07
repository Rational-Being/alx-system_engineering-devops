#!/usr/bin/python3

"""
a pythons scriptthat uses the rest api orm the code
for a given emplyee id, it returns information about his/her TODO list progress
in csv format
"""

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    _id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users/{}".format(_id)
    username = get(base_url).json().get('username')

    task_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            _id)
    task_response = get(task_url).json()

    total_tasks = {_id: []}

    for task in task_response:
        if (task.get("userId") == int(_id)):
            total_tasks[_id].append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
                })

    with open("{}.json".format(_id), "w+") as file:
        dump(total_tasks, file)
