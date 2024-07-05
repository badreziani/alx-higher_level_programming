#!/usr/bin/python3
"""3-error_code
takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            res_body = res.read().decode('utf-8')
            print(res_body)
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
