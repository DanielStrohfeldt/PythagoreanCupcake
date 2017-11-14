from set import Set
from team import Team


class TeamSet(Set):
    def __init__(self):
        self.teams = []

    def add(self, other):
        if isinstance(other, Team):
            for i in range(len(self.teams)):
                if self.teams[i].get_username() == other.get_username():
                    return False
            self.teams.append(other)
            return True
        else:
            raise TypeError("Error attempting to add team. Parameter passed in is not a team object")

    def remove(self, other):
        if isinstance(other, Team):
            for i in range(len(self.teams)):
                if self.teams[i].get_username() == other.get_username():
                    self.teams.remove(self.teams[i])
                    return True
            return False
        else:
            raise TypeError("Error attempting to remove team. Parameter passed in is not a team object!")

    def get(self, other):
        for i in range(len(self.teams)):
            if str(other) == self.teams[i].get_username():
                return self.teams[i]
        return None

    def clear(self):
        self.teams = []

    def size(self):
        return len(self.teams)

    def iterator(self):
        return iter(self.teams)