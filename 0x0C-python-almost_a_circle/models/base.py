#!/usr/bin/python3
"""Module tha contains the Base class"""


import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init function
        args:
        self
        id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list_dictionaries
        args
        list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file
        args
        cls
        list_objs"""
        for i, y in enumerate(list_objs):
            list_objs[i] = cls.to_dictionary(y)
        with open(cls.__name__ + '.json', 'w', encoding='utf8') as file:
            if list_objs is None:
                file.write('[]')
            else:
                file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string
        args
        json_string"""
        if json_string is None or json_string == []:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """create function"""
        pass

    @classmethod
    def load_from_file(cls):
        with open(cls.__name__+'.json', 'r') as file:
            if file.readlines() is None:
                return ([])
