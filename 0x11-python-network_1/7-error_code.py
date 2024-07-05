#!/usr/bin/python3
"""7-error_code
takes in a URL, sends a request to the URL
and displays the body of the response
"""

if __name__ == '__main__':
    import requests
    import sys

    res = requests.get(sys.argv[1])
    if res.ok:
        print(res.text)
    else:
        print(f"Error code: {res.status_code}")
