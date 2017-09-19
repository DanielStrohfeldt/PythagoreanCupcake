class Room:

    def __init__(self, square):
        self._squares = [square]
        self._area = square.area 

    @property
    def area(self):
        return self._area

    @property
    def squares(self):
        return self._squares

    def add_square(self, square):
        self._squares.append(square)
        self._area += square.area

    def remove_square(self, square):
        self._squares.remove(square)
            

