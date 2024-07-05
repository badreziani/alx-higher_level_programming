#!/usr/bin/python3
"""0-hbtn_status
This script fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as res:
        res_body = res.read()
        print(f"""Body response:
            - type: {type(res_body)}
            - content: {res_body}
            - utf8 content: {res_body.decode('utf-8')}""")
