#!/usr/bin/python3
"""10-my_github
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == '__main__':
    import requests
    import sys

    url = f"https://api.github.com/users/{sys.argv[1]}"
    headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {sys.argv[2]}',
            'X-GitHub-Api-Version': '2022-11-28'
            }
    res = requests.get(url, headers=headers)
    print(res.json().get('id'))
