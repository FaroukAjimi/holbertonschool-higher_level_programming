#!/usr/bin/python3
"""
post request
to display name and id
"""
if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) == 1:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': ""})
    elif len(sys.argv) == 2:
        r = requests.post('http://0.0.0.0:5000/search_user',
                          data={'q': sys.argv[1]})
    try:
        jsn = r.json()
        if not bool(jsn):
            print("No result")
            exit()
        else:
            print ('[{}] {}'.format(jsn['id'], jsn['name']))
    except ValueError:
        print("Not a valid JSON")
