from abc import ABCMeta
import abc


class Playable(object):
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def login(self, username, password):
        pass

    @abc.abstractmethod
    def logout(self):
        pass

    @abc.abstractmethod
    def play(self, hasArrived):
        pass

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def end(self):
        pass

    @abc.abstractmethod
    def is_running(self):
        pass

    @abc.abstractmethod
    def get_teamset(self):
        pass

    @abc.abstractmethod
    def get_locationset(self):
        pass

    @abc.abstractmethod
    def get_currentuser(self):
        pass
