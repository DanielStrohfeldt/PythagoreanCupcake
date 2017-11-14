from abc import ABCMeta


class User(object):
    __metaclass__ = ABCMeta

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def set_username(self, username):
        self.username = username