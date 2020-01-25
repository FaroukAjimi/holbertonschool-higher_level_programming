#!/usr/bin/python3
class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            d = {}
            for i in attrs:
                if i in self.__dict__:
                    d[i] = self.__dict__[i]
            return(d)
        return (self.__dict__)
    def reload_from_json(self, json):
        for i, y in json.items():
            self.__dict__[i] = y
