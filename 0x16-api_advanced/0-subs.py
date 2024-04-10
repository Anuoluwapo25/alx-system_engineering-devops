#!/usr/bin/python3
"""
function that queries the Reddit API
"""

import requests
from sys import argv

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = f"https://api.reddit.com/r/{subreddit}/about"

    url_request = requests.get(url, headers=headers)
    if url_request.status_code == 200:
        response = url_request.json()
        subs = response["data"]["subscribers"]
    else:
        subs = 0
    return subs

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py subreddit_name")
    else:
        subreddit_name = argv[1]
        print(number_of_subscribers(subreddit_name))

