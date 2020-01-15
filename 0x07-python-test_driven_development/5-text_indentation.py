#!/usr/bin/python3
"""this module will split
a text by(.) or (:) or (?)
and will skip all spaces
presented at the beggning
and the the end of each line"""


def text_indentation(text):
    """function text_indentation
    args:
    text"""
    i = 0
    y = 0
    if not(isinstance(text, str)):
        raise TypeError('text must be a string')
    text = text.strip()
    while i < (len(text)):
        print('{:s}'.format(text[i]), end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print()
            print()
            y = i + 1
            if (y in range(len(text))):
                while (text[y] == ' '):
                    i = i + 1
                    y += 1
        i = i + 1
