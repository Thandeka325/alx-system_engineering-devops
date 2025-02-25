#!/usr/bin/python3
"""
Module to fetch the number of subscribers,
and top 10 hot posts for a given subreddit.
Also includes a recursive function to get all hot post titles.
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


def recurse(subreddit, hot_list=[], after=None):
    """Recursively retrieves a list of all hot article titles
       for a given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "CustomUserAgent/1.0"}
    params = {"after": after} if after else {}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        hot_list.extend(
                [post.get("data", {}).get("title", "") for post in posts]
        )
        after = data.get("data", {}).get("after", None)
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list

    return None
