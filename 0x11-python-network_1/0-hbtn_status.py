#!/usr/bin/python3
import urllib.request
rq = urllib.request.Request("https://intranet.hbtn.io/status")
with urllib.request.urlopen(rq) as rs:
    d = rs.read()
print("Body reponse:")
print("    - type: {}".format(type(d)))
print("    - content: {}".format(d))
print("    - utf8 content: {}".format(d.decode("utf-8")))
