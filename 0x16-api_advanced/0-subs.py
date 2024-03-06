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

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "Brave Browser"}
    response = get(url, headers=headers)
    subs = response.json()

    try:
        return int(subs.get("data").get("subscribers"))
    except Exception:
        return 0
