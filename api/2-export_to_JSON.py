#!/usr/bin/python3
"""Export an employee's TODO list tasks to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    username = user.get("username")

    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": username} for task in todos]

    data = {employee_id: tasks}

    with open("{}.json".format(employee_id), "w") as file:
        json.dump(data, file)
