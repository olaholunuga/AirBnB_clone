#!/usr/bin/env python
"""
BaseModel class for the AirBnB Project
"""
import uuid
import datetime
import storage

class BaseModel:

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = datetime.datetime.strptime(kwargs[k], "%Y-%m-%dT%H:%M:%S.%f")
                if k != ['__class__']:
                    setattr(self, k, v)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save(self)

    def to_dict(self):
        self_dict = {}
        for k, v, in self.__dict__.items():
            if v:
                if k in ["created_at", "updated_at"]:
                    self_dict[k] = v.isofomat()
                else:
                    self_dict[k] = v

        self_dict["__class__"] = self.__class__.__name__
        return self_dict
