from set import Set
from loc import Location


class LocationSet(Set):
    def __init__(self):
        self.locations = []

    def add(self, other):
        if isinstance(other, Location):
            for i in range(len(self.locations)):
                if self.locations[i].get_name() == other.get_name():
                    return False
            self.locations.append(other)
            return True
        else:
            raise TypeError("Error attempting to add location. Parameter passed in is not a location object")

    def remove(self, other):
        if isinstance(other, Location):
            for i in range(len(self.locations)):
                if self.locations[i].get_name() == other.get_name():
                    self.locations.remove(self.locations[i])
                    return True
            return False
        else:
            raise TypeError("Error attempting to remove location. Parameter passed in is not a location object!")

    def get(self, other):
        for i in range(len(self.locations)):
            if str(other).lower() == self.locations[i].get_name():
                return self.locations[i]
        return None

    def clear(self):
        self.locations = {}

    def size(self):
        return len(self.locations)

    def iterator(self):
        return iter(self.locations)