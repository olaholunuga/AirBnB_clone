#!/usr/bin/env python
"""
class FileStorage to store objects
"""
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    all(self):
        "returns the dictionary representation of created objects"
        return __objects

    new(self, obj):
        "sets in __objects the obj with key <obj class name>.id"
        obj_id = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_id] = obj
