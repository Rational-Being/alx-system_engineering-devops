#!/usr/bin/python3
"""
Get top ten posts  in reddit api
"""

from json import loads
from requests import get


def top_ten(subreddit):
    """
    this funtion gets the top te post in reddit api
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "Brave Browser"}
    response = get(url, headers=headers)
    subs = response.json()

    if response.status_code == 404:
        print("None")
    elif "data" not in subs:
        print("None")
    else:
        for post in subs["data"]["children"]:
            print(post["data"]["title"])
