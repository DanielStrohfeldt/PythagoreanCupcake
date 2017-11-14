from location import Location


class Loc(Location):
    def __init__(self, name, question, answer, clue):
        if (name is None) or (question is None) or (answer is None) or (clue is None):
            raise TypeError("Cannot instantiate an instance of Location with parameters set as 'None'")
        self.name = name.lower()
        self.question = question
        self.answer = answer.lower()
        self.clue = clue

    def get_name(self):
        return self.name

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_clue(self):
        return self.clue

    def set_name(self, name):
        self.name = name.lower()

    def set_question(self, question):
        self.question = question

    def set_answer(self, answer):
        self.answer = answer.lower()

    def set_clue(self, clue):
        self.clue = clue

