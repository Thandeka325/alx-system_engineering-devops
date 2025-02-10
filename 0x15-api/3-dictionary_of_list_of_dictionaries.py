#!/usr/bin/python3
"""
Script exports all employees' tasks in JSON format to a file.
"""
import json
import requests


def fetch_data():
    """Fetches user and task data from the API."""
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    user_dict = {user["id"]: user["username"] for user in users}
    tasks_dict = {}

    for task in todos:
        user_id = task["userId"]
        if user_id not in tasks_dict:
            tasks_dict[user_id] = []
        tasks_dict[user_id].append({
            "username": user_dict[user_id],
            "task": task["title"],
            "completed": task["completed"]
        })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_dict, json_file)


if __name__ == "__main__":
    fetch_data()
