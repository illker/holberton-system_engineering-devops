#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    em_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/users/' + em_id
    r = requests.get(api_url)
    username = r.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/' + em_id + '/todos'
    r2 = requests.get(url).json()

    file = em_id + '.json'

    dic = {em_id: []}

    for bu in r2:
        task = {}
        task['task'] = bu.get('title')
        task['completed'] = bu.get('completed')
        task['username'] = username
        dic[em_id].append(task)

    with open(file, 'w', newline='') as burger:
        json.dump(dic, burger)
