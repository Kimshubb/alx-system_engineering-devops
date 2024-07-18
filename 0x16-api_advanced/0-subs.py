#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers for a given subreddit.

Functions:
- number_of_subscribers(subreddit): Returns the number of subscribers for a given subreddit. 
  Returns 0 if the subreddit is invalid.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Python/3.8; +http://example.com)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

