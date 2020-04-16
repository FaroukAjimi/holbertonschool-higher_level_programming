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
        r = r.json()
        if not bool(r):
            print("No result")
        else:
            print ('[{}] {}'.format(r['id'], r['name']))
    except:
        print("Not a valid JSON")
