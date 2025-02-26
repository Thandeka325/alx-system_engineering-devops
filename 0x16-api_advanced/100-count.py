#!/usr/bin/python3
"""
Module to fetch the number of subscribers,
and top 10 hot posts for a given subreddit.
Also includes recursive functions to get all hot post titles,
and count keyword occurrences.
"""
from collections import Counter
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
    params = {"limit": 100, "after": after} if after else {"limit": 100}
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


def count_words(subreddit, word_list, word_count=None, after=None):
    """Recursively queries the Reddit API,
       and counts keyword occurrences in hot article titles.
    """
    if not subreddit or not isinstance(subreddit, str):
        return

    if word_count is None:
        word_count = Counter()

    word_list = Counter(word.lower() for word in word_list)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "CustomUserAgent/1.0"}
    params = {"limit": 100, "after": after} if after else {"limit": 100}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    # Count words in post titles
    title_counts = Counter(
        word for post in posts for word in post.get("data", {}).get(
            "title", "").lower().split()
    )

    for word in word_list:
        word_count[word] += title_counts[word]

    after = data.get("data", {}).get("after", None)
    if after:
        return count_words(subreddit, word_list, word_count, after)

    # Sort and print the final word count
    sorted_word_count = sorted(
        [(word, count) for word, count in word_count.items() if count > 0],
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_word_count:
        print(f"{word}: {count}")
