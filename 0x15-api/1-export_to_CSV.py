#!/usr/bin/python3
"""Gather data from an API"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    em_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/users/' + em_id
    r = requests.get(api_url)
    username = r.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/' + em_id + '/todos'
    r2 = requests.get(url).json()

    file = em_id + '.csv'
    with open(file, 'w', newline='') as bu:
        burger = csv.writer(bu, quoting=csv.QUOTE_ALL)
        [burger.writerow([em_id, username, beer.get(
            'completed'), beer.get('title')]) for beer in r2]
