#!/usr/bin/python3
"""queries the Reddit API and returns subscribers"""

import json
import requests


def top_ten(subreddit):
    """Top Ten"""
    burger = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    h = {'User-Agent': 'linux: burger:v1.0.0 (by /u/da2a)'}
    request = requests.get(burger, headers=h)
    if request.status_code == 200:
        bu = request.json().get("data").get("children")
        for beer in bu[0:10]:
            print(beer.get("data").get("title"))
    else:
        print("None")
