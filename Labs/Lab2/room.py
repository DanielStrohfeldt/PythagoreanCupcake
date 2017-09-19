class Room:

    def __init__(self, name, square):
        self._name = name
        self._squares = [square]
        self._area = square.area 

    @property
    def area(self):
        return self._area

    @property
    def squares(self):
        return self._squares

    @property
    def name(self):
        return self._name

    def change_name(self, name):
        self._name = name

    def add_square(self, square):
        self._squares.append(square)
        self._area += square.area

    def remove_square(self, square):
        self._squares.remove(square)
        self._area -= square.area
            

