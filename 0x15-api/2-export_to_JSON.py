#!/usr/bin/python3
"""
Script fetches an employee's TODO list from an API, eports it to a JSON file.
"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    user_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    username = user_data.get("username")
    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        for task in todos_data
    ]

    json_data = {employee_id: tasks}

    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(json_data, json_file)
