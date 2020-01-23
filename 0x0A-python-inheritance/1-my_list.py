#!/usr/bin/python3
"""Module That contains MyList function"""


class MyList(list):
    """Mylist class"""
    def print_sorted(self):
        """print sorted function"""
        print(sorted(self))
