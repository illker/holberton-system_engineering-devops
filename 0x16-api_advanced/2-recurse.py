#!/usr/bin/python3
"""queries the Reddit API and returns subscribers"""

import json
import requests


def recurse(subreddit, hot_list=[]):
    """Recurse it!"""
    burger = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    h = {'User-Agent': 'linux: burger:v1.0.0 (by /u/da2a)'}
    request = requests.session()
    request.headers = h
    p = {'limit': 100, 'after': after}
    r = request.get(url, params=p)
    # print (r.json())
    if r.status_code == 200:
        after = r.json().get('data').get('after')
        for hot in r.json().get('data').get('children'):
            hot_list.append(hot.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
