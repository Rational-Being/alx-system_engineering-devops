#!/usr/bin/python3
"""
Get top ten posts  in reddit api
"""

from json import loads
from requests import get


def recurse(subreddit, hot_list=[]):
    """
    this funtion gets the top te post in reddit api
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "Brave Browser"}
    response = get(url, headers=headers)
    subs = response.json()

    try:
        subs_2 = reddits.get("data").get("children")
        for child in sub_2:
            hot_list.append(title.get("data").get("child"))
        return hot_list
    except Exception as e:
        print(None)
        return 0
