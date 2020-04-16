#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    dic = {}
    dic['username'] = sys.argv[1]
    dic['Authorization'] = 'token ' + sys.argv[2]
    rs = requests.get('https://api.github.com/user', headers=dic)
    jsn = rs.json()
    if rs.status_code == 200:
        print(jsn['id'])
    else:
        print('None')
