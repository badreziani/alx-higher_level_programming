#!/usr/bin/python3
"""8-json_api
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

if __name__ == '__main__':
    import requests
    import sys

    data = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data=data)
    if 'application/json' in res.headers.get('Content-Type'):
        json_data = res.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
