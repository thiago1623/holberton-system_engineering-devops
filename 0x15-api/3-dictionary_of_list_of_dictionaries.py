#!/usr/bin/python3
""" Calls an API and stores data in a JSON file """
import csv
import json
import requests


if __name__ == '__main__':
    userId = 1
    user_tasks = {}
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url_user).json()

    for userId in range(1, len(users) + 1):
        todo = requests.get(url_todo, params={'userId': userId})
        user = requests.get(url_user, params={'id': userId})

        todo_dict_list = todo.json()
        user_dict_list = user.json()
        task_list = []
        employee = user_dict_list[0].get('username')

        for task in todo_dict_list:
            status = task.get('completed')
            title = task.get('title')
            task_dict = {}
            task_dict['task'] = title
            task_dict['completed'] = status
            task_dict['username'] = employee
            task_list.append(task_dict)
        user_tasks[userId] = task_list

    with open("todo_all_employees.json", "w+") as jsonfile:
        json.dump(user_tasks, jsonfile)
