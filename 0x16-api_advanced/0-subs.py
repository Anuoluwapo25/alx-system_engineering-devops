#!/usr/bin/python3
"""
returns the number of subscribers

"""


import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    connect to reddit API
    """
    subreddit = argv[1]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = "https://api.reddit.com/r/{}/about".format(subreddit)

    urlRequest = requests.get(url, headers=headers)
    if urlRequest.status_code == 200:
        response = urlRequest.json()
        subs = response["data"]["subscribers"]
    else:
        subs = 0
    return subs
