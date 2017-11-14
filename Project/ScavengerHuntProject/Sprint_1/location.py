import abc


class Location:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def get_question(self):
        pass

    @abc.abstractmethod
    def get_clue(self):
        pass

    @abc.abstractmethod
    def get_answer(self):
        pass

    @abc.abstractmethod
    def set_name(self, name):
        pass

    @abc.abstractmethod
    def set_question(self, question):
        pass

    @abc.abstractmethod
    def set_answer(self, answer):
        pass

    @abc.abstractmethod
    def set_clue(self, clue):
        pass