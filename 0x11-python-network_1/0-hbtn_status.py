#!/usr/bin/python3
'''
get type, content, and utf8 content
'''
if __name__ == "__main__":
    import urllib.request
    rq = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(rq) as rs:
        d = rs.read()
        print("Body response:")
        print("\t- type: {}".format(type(d)))
        print("\t- content: {}".format(d))
        print("\t- utf8 content: {}".format(d.decode("utf-8")))
