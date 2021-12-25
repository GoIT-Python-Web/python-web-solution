"""
Домашнее задание 1.
Задание 1
"""
import pickle
import json
import collections
from abc import ABC, abstractmethod


class SerializationInterface(ABC):
    @abstractmethod
    def to_pickle(self, data):
        pass

    @abstractmethod
    def to_json(self, data):
        pass


class SerializeDict(SerializationInterface):
    def to_pickle(self, data):
        return pickle.dumps(data)

    def to_json(self, data):
        return json.dumps(data)


class SerializeList(SerializationInterface):
    def to_pickle(self, data):
        return pickle.dumps(data)

    def to_json(self, data):
        d = collections.defaultdict(dict)
        for i in range(0, len(data) - 1, 2):
            d[data[i]] = data[i + 1]
        return json.dumps(d)


class SerializeTuple(SerializationInterface):
    def to_pickle(self, data):
        return pickle.dumps(data)

    def to_json(self, data):
        d = collections.defaultdict(dict)
        for i in range(0, len(data) - 1, 2):
            d[data[i]] = data[i + 1]
        return json.dumps(d)


class SerializeSet(SerializationInterface):
    def to_pickle(self, data):
        return pickle.dumps(data)

    def to_json(self, data):
        d = collections.defaultdict(dict)
        for i in range(0, len(data) - 1, 2):
            d[data[i]] = data[i + 1]
        return json.dumps(d)


"""
Домашнее задание 1. Задание 2.
"""


class Meta(type):
    def __new__(*args):
        for name in Meta.__dict__.keys():
            if not name.startswith("__"):
                field_name = name
        number_value = Meta.__dict__[field_name]
        args[len(args) - 1]["class_number"] = number_value
        Meta.__setattr__(Meta, field_name, number_value + 1)
        return type.__new__(*args)


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


print(Cls1.class_number, Cls2.class_number)
assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(""), Cls2("")
assert (a.class_number, b.class_number) == (0, 1)
