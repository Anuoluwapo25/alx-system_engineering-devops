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
        return subs
    elif url_request.status_code == 404:
        return "nonexisting subreddit"
    else:
        return "existing Subreddit"

# Call the function with the subreddit provided as a command-line argument
if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py subreddit_name")
    else:
        subreddit_name = argv[1]
        result = number_of_subscribers(subreddit_name)
        print(result)

