#/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
if [ $(curl -s -I $1 | grep 'HTTP/' | awk '{print $2}') == '200' ]; then curl -s -L $1; fi
