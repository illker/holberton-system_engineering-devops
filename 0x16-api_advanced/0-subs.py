#!/usr/bin/python3
"""queries the Reddit API and returns subscribers"""

import json
import requests


def number_of_subscribers(subreddit):
    """How many subs?"""
    burger = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    headers = {'User-Agent': 'linux: burger:v1.0.0 (by /u/da2a)'}
    request = requests.get(burger, headers)
    if request.status_code == 200:
        return request.json().get('data').get('subscribers')
    else:
        return 0
