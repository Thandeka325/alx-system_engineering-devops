#!/usr/bin/python3
"""
Script to fetch and export an employee's TODO list progress to a CSV file.
"""
import csv
import requests
import sys


def fetch_and_export_to_csv(employee_id):
    """Fetches the TODO list of an employee and exports it to a CSV file."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_username = user_data.get("username")
    file_name = f"{employee_id}.csv"

    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                employee_username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    fetch_and_export_to_csv(int(sys.argv[1]))
