#!/usr/bin/python3
"""
Calls an API in order to get completed tasks
"""
import requests
import sys


if __name__ == '__main__':
    userId = sys.argv[1]
    url_TODO = 'https://jsonplaceholder.typicode.com/todos/'
    url_usr = 'https://jsonplaceholder.typicode.com/users/'

    todo = requests.get(url_TODO, params={'userID': userId})
    user = requests.get(url_usr, params={'id': userId})

    """convert in json"""
    dict_todo = todo.json()
    dict_usr = user.json()

    completed_task = []
    total_task = len(dict_todo)
    employee = dict_usr[0].get('name')

    """ add tasks """
    for task in dict_todo:
        if task['completed']:
            completed_task.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(completed_task), total_task))

    for task in completed_task:
        print("\t {}".format(task.get('title')))
