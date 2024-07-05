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

