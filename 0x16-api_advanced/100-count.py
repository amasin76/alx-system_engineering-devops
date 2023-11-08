#!/usr/bin/python3
"""Count it api"""
import requests
from collections import Counter
import re


def count_words(subreddit, word_list, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    headers = {'User-Agent': 'custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        if hot_list:
            word_count = Counter(hot_list)
            word_list_lower = [word.lower() for word in word_list]
            for word, count in sorted(word_count.items(),
                                      key=lambda x: (-x[1], x[0])):
                if word in word_list_lower:
                    print(f"{word}: {count}")
        return
    data = response.json()['data']
    hot_list.extend([word.lower() for title in data['children']
                     for word in re.split(r'\W', title['data']['title'])])
    if data['after'] is None:
        word_count = Counter(hot_list)
        word_list_lower = [word.lower() for word in word_list]
        for word, count in sorted(word_count.items(),
                                  key=lambda x: (-x[1], x[0])):
            if word in word_list_lower:
                print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, hot_list, data['after'])
