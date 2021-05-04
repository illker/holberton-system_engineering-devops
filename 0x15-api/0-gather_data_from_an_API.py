#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv


if __name__ == '__main__':
    em_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/users/' + em_id
    r = requests.get(api_url)
    name = r.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/' + em_id + '/todos'
    r2 = requests.get(url).json()
    burger = [bu for bu in r2 if bu['completed'] is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(burger), len(r2)))

    for beer in burger:
        print('\t ' + beer['title'])
