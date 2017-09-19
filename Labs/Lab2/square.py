class Square:

    def __init__(self, width, height):
        self._width = int(width)
        self._height = int(height)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

