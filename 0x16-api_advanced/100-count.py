#!/usr/bin/python3
"""
recursive function that queries the Reddit API
"""

import requests
from collections import defaultdict

def count_words(subreddit, word_list, after=None, counts=defaultdict(int)):
    """
    connect to the reddit API
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Custom User-Agent to avoid Too Many Requests error
    params = {'limit': 100, 'after': after}  # Limiting the number of posts to retrieve to 100 per request

    response = requests.get(url, headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        # Extract titles and count occurrences of keywords
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if f" {word.lower()} " in f" {title} ":
                    counts[word.lower()] += 1
        
        # Check if there are more posts to fetch
        after = data['data']['after']
        if after is not None:
            # Recursively call the function with the 'after' parameter to fetch the next page of posts
            return count_words(subreddit, word_list, after, counts)
        else:
            # No more posts to fetch, print the sorted counts
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    elif response.status_code == 404:
        print("Invalid subreddit or no posts found.")
    else:
        print("An error occurred while fetching data from Reddit.")
        

