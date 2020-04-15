#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    try:
        r = requests.get(sys.argv[1])
        print(r.headers["X-Request-Id"])
    except:
        pass
