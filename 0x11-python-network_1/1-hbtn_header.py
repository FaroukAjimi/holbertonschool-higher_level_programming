#!/usr/bin/python3
# get varibale value
if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        for i, y in html.items():
            if i == "X-Request-Id":
                print(y)
