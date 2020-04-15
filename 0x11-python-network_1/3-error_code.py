#!/usr/bin/python3
# error code display
if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('code:', e.code)
