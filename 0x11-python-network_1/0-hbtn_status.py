#!/usr/bin/python3
"""0-hbtn_status
This script fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as res:
        res_body = res.read()
        print("Body response:")
        print(f"\t- type: {type(res_body)}")
        print(f"\t- content: {res_body}")
        print(f"\t- utf8 content: {res_body.decode('utf-8')}")
