#!/usr/bin/python3
"""2-post_email
takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib
    import sys
