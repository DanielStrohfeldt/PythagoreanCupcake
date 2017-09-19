class Square:

    def __init__(self, width, length):
        self._width = int(width)
        self._length = int(length)

    @property
    def width(self):
        return self._width
    
    @property
    def length(self):
        return self.length

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._length 

