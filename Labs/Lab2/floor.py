class Floor:

    def __init__(self, floor_number, room):
        self._floor_number = floor_number
        self._rooms = [room]
        self._area = room.area

    @property
    def area(self):
        return self._area

    @property
    def rooms(self):
        return self._rooms

    @property
    def floor_number(self):
        return self._floor_number

    def change_floor_number(self, number):
        self._floor_number = number

    def add_room(self, room):
        self._rooms.append(room)
        self._area += room.area

    def remove_room(self, room):
        self._rooms.remove(room)
        self._area -= room.area
