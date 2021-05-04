#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests
from sys import argv

if __name__ == '__main__':

    api_url = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get(api_url).json()
    dic_id = {}
    for bu in r:
        dic_id[bu.get('id')] = bu.get('username')
    r2 = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    dic_f = {}
    for bu in r2:
        user_id = bu.get("userId")
        username = dic_id[user_id]
        title = bu.get("title")
        completed = bu.get("completed")
        dic = {"username": username, "task": title, "completed": completed}
        if dic.get(user_id):
            dic.get(user_id).append(dic)
        else:
            dic_f[user_id] = [dic]
    with open('todo_all_employees.json', 'w', newline='') as burger:
        json.dump(dic_f, burger)
