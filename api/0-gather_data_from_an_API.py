#!/usr/bin/python3
"""Gather data from a REST API for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done_tasks), len(todos)))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
