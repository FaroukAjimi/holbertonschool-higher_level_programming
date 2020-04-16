#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) == 1:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': ""})
    else:
        r = requests.post('http://0.0.0.0:5000/search_user',
                          data={'q': sys.argv[1]})
    try:
        r = r.json()
    except:
        print("Not a valid JSON")
    if not r:
        print("No result")
        exit()
    print ('[{}] {}'.format(r['id'], r['name']))
