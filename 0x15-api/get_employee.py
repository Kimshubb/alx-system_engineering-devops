#!/usr/bin/python3
# gET employee to do progress
import sys
import requests

def get_employee_todo_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))
    todos_response = requests.get(url + "todos", params{"userId": employee_id})
    if response.status_code == 200 and todos_response.status_code == 200:
        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data.get["name"]
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])
        completed_titles = [todo['title'] for todo in todos_data if todo['completed']]
        print("Employee {} is done with tasks {}/{}".format(employee_name, completed_tasks, total_tasks))
        for title in completed_tasks:
            print("\t{}".format(title))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: <0-gather_data_from_an_API.py><employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
