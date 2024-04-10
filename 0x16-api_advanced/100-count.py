#!/usr/bin/python3
"""
queries the Reddit API
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    recursive function that queries the Reddit API, parses the title
    """

    if counts is None:
        counts = {}
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if f" {word.lower()} " in f" {title} ":
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1
        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    elif response.status_code == 404:
        print("nonexisting subreddit")
    else:
        print("existing Subreddit")
