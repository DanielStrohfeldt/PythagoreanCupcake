class Floor:

    def __init__(self, room):
        self._rooms = [room]
        self._area = room.area

    @property
    def area(self):
        return self._area

    @property
    def rooms(self):
        return self._rooms
