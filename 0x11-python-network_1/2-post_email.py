#!/usr/bin/python3
"""2-post_email
takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as res:
        res_body = res.read().decode('utf-8')
        print(f"Your email is: {res_body}")
