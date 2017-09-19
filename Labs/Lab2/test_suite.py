# Base Python
import unittest

# Created Python
from square import Square
from room import Room
from floor import Floor

class TestBuilding(unittest.TestCase):
    
    def setUp(self):
        self.square_uno = Square(width=100)
        self.room_uno = Room(square=self.square_uno)
        self.floor_uno = Floor(room=self.room_uno)

    def test_create_square(self):
        self.assertIsInstance(self.square_uno, Square)

    def test_square_width(self):
        self.assertEqual(100, self.square_uno.width)

    def test_square_area(self):
        self.assertEqual(10000, self.square_uno.area)

    def test_create_room(self):
        self.assertIsInstance(self.room_uno, Room)

    def test_room_area(self):
        self.assertEqual(10000, self.room_uno.area)

if __name__ == '__main__':
    unittest.main()
