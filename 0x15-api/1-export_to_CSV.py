#!/usr/bin/python3

"""
a pythons scriptthat uses the rest api orm the code
for a given emplyee id, it returns information about his/her TODO list progress
in csv format
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com.users/{}".format(argv[1])
    response = get(base_url)
    employeeName = response.json().get("name")

    task_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    response = get(task_url)
    tasks = response.json()

    with open("{}.csv".format(argv[1]), "w") as csvfile:
        for task in tasks:
            csvfile.write(
                '"{}","{}","{}","{}"\n'.format(
                    argv[1], username, task.get("completed"), task.get("title")
                )
            )
