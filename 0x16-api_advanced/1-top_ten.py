#!/usr/bin/python3
"""
function that queries the Reddit API 
and prints the titles of the first 10 hot posts
"""


import requests
from sys import argv


def top_ten(subreddit):
    """
    connect to reddit API
    """
    subreddit = argv[1]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)

    urlRequest = requests.get(url, headers=headers, allow_redirects=False)
    if urlRequest.status_code == 200:
        response = urlRequest.json()
        for child in response['data']['children']:
            print(child['data']['title'])
    else:
        print(None)
