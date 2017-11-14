from abc import ABCMeta
import abc


class Set(object):
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def add(self, other):
        pass

    @abc.abstractmethod
    def remove(self, other):
        pass

    @abc.abstractmethod
    def size(self):
        pass

    @abc.abstractmethod
    def clear(self):
        pass

    @abc.abstractmethod
    def get(self, other):
        pass

    @abc.abstractmethod
    def iterator(self):
        pass