#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: ', sys.argv[0], '<employee id>')
        sys.exit(1)

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + '/users/{}'.format(user_id)).json()
    todos = requests.get(url + '/users/{}/todos'.format(user_id)).json()

    with open('{}.csv'.format(user_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, user.get('name'),
                            task.get('completed'), task.get('title')])
