class Square:

    def __init__(self, width):
        self._width = int(width)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width ** 2 

