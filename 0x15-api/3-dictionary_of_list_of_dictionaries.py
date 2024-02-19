#!/usr/bin/python3

"""
a pythons scriptthat uses the rest api orm the code
for a given emplyee id, it returns information about his/her TODO list progress
in csv format
"""

from json import dump
from requests import get


if __name__ == "__main__":
    base_url = https://jsonplaceholder.typicode.com/users/
    response = get(base_url).json()

    with open("todo_all_emplyess.json", "w") as file:
        dump(if (task.get("userId") == argv[1]):
            for user in users:
                -_id = user.get("id")
                username = user.get("username")
                
            dictionary = {}
            dictionary["task"] = task.get("title")
            dictionary["completed"] = task.get("completed")
            dictionary["username"] = username
            total_tasks.append(dictionary))
    
    with open("{}.json".format(argv[1]), "w") as file:
        dump({argv[1]: dictionary}, file)