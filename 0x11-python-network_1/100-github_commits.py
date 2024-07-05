#!/usr/bin/python3
"""10-my_github
The Holberton School staff evaluates candidates applying
for a back-end position with multiple technical challenges, like this one:
    Please list 10 commits (from the most recent to oldest)
    of the repository “rails” by the user “rails”
    You must use the GitHub API, here is the documentation
    https://developer.github.com/v3/repos/commits/
    Print all commits by: `<sha>: <author name>` (one by line)

This script takes 2 arguments in order to solve this challenge.
"""

if __name__ == '__main__':
    import requests
    import sys

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    headers = {
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
            }
    res = requests.get(url, headers=headers)
    for commit in res.json()[:10]:
        print(f"{commit.get('sha')}: ", end="")
        print(f"{commit.get('commit').get('author').get('name')}")
