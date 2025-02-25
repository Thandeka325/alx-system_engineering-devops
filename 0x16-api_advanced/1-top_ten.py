#!/usr/bin/python3
"""
Module to fetch the number of subscribers,
and top 10 hot posts for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "CustomUserAgent/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)

    return 0


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "CustomUserAgent/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title", "None"))
    else:
        print(None)
