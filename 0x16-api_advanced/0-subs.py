#!/usr/bin/python3
"""
Get subscriber  in reddit api
"""

from json import loads
from requests import get


def number_of_subscribers(subreddit):
    """
    this funtion quaries reddit api
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.1"}
    response = get(url, headers=headers)

    try:
        _subs = response.json()
        return _subs.get("data").get("subscribers")
    except Exception:
        return 0
