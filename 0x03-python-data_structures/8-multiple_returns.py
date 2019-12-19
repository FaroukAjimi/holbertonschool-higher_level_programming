#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if sentence == "":
        return(l, None)
    f = sentence[0:1]
    s = (l, f)
    return(s)
