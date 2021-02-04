#!/usr/bin/python3
""" Contains the number_of_subscribers function """
import requests


def number_of_subscribers(subreddit):
    """
        Returns the number of subscribers to a specified subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'thiago'}
    req = requests.get(url, headers=user_agent, allow_redirects=False)
    if req.status_code == 200:
        req = req.json()
        data = req.get('data')
        subscribers = data.get('subscribers')
        if data is not None and subscribers is not None:
            return subscribers
    return 0
