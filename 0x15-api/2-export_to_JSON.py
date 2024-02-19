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
    base_url = "https://jsonplaceholder.typicode.com.users/{}".format(argv[1])
    username = get(base_url).json().get('username')
   
    task_url = "https://jsonplaceholder.typicode.com/todos"
    task_response = get(task_url).json()
    
    total_tasks = []
    for task in task_response:
        if (task.get("userId")):
            dictionary = {}
            dictionary["task"] = task.get("title")
            dictionary["completed"] = task.get("completed")
            dictionary["username"] = username
            total_tasks.append(dictionary)
    
    with open("{}.json".format(argv[1]), "w") as file:
        dump({argv[1]: dictionary}, file)