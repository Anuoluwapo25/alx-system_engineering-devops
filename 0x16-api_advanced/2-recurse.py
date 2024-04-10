#!/usr/bin/python3
"""
recursive function that queries the Reddit API
returns a list containing the titles 
of all hot articles for a given subreddit
"""


import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=""):
    """
    recursively query the reddit API
    """
    if after is None:
        return (hot_list)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    if (len(hot_list) == 0):
        url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    else:
        url = "https://api.reddit.com/r/{}/hot?after={}".format(
                subreddit, after)
    urlRequest = requests.get(url, allow_redirects=False, headers=headers)

    if (urlRequest.status_code == 200):
        response = urlRequest.json()
        for child in response['data']['children']:
            hot_list.append(child['data']['title'])
    else:
        return None

    after = response['data']['after']

    return (recurse(subreddit, hot_list, after))
