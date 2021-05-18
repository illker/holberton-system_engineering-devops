#!/usr/bin/python3
"""queries the Reddit API and returns subscribers"""

import json
import requests
from requests.api import request


def recurse(subreddit, hot_list=[]):
    """Recurse it!"""
    burger = 'https://www.reddit.com/r/' + subreddit
    burger += '/hot.json?limit=100&after=' + page
    h = {'User-Agent': 'linux: burger:v1.0.0 (by /u/da2a)'}
    if len(hot_list) != 0:
        page = hot_list[0]
    else:
        page = ''
        hot_list.append('')
    request = requests.get(burger, headers=h)
    if request.status_code != 200:
        return None
    else:
        d = request.json().get("data")
        a = d.get("after")
        hot_list[0] = a
        c = d.get("children")
        for child in c:
            hot_list.append(child.get("data").get("title"))
        if a is None:
            return hot_list[1:]
        return recurse(subreddit, hot_list)
