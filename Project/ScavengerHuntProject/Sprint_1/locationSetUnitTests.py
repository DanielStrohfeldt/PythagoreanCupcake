import unittest
from locationSet import LocationSet
from loc import Loc


class LocationCollectionUnitTests(unittest.TestCase):
    def setUp(self):
        self.c1 = LocationSet()
        self.l1 = Loc("location1", "question1", "answer1", "clue1")
        self.l2 = Loc("location2", "question2", "answer2", "clue2")
        self.l3 = Loc("location3", "question3", "answer3", "clue3")
        self.falseLoc1 = "This is not a location 1"
        self.falseLoc2 = 0

    def test_add(self):
        self.c1.add(self.l1)
        self.assertEqual([self.l1], self.c1.locations, "l1 should have been added to list of locations")
        self.c1.add(self.l2)
        self.assertEqual([self.l1, self.l2], self.c1.locations, "l2 should have been added to list of locations")
        self.c1.add(self.l3)
        self.assertEqual([self.l1, self.l2, self.l3], self.c1.locations, "l3 should have been added to list of locations")

    def test_addAlreadyExists(self):
        self.c1.locations = [self.l1, self.l2, self.l3]
        self.c1.add(self.l1)
        self.assertEqual([self.l1, self.l2, self.l3], self.c1.locations, "l1 should not have been added twice to the"
                                                                         " list of locations")
        self.c1.add(self.l2)
        self.assertEqual([self.l1, self.l2, self.l3], self.c1.locations, "l2 should not have been added twice to the"
                                                                         " list of locations")
        self.c1.add(self.l3)
        self.assertEqual([self.l1, self.l2, self.l3], self.c1.locations, "l3 should not have been added twice to the"
                                                                         " list of locations")

    def test_addException(self):
        self.assertRaises(TypeError, self.c1.add, self.falseLoc1)
        self.assertRaises(TypeError, self.c1.add, self.falseLoc2)

    def test_remove(self):
        self.c1.locations = [self.l1, self.l2, self.l3]
        self.c1.remove(self.l3)
        self.assertEqual([self.l1, self.l2], self.c1.locations, "l3 was not removed from the list of locations")
        self.c1.remove(self.l1)
        self.assertEqual([self.l2], self.c1.locations, "l1 was not removed from the list of locations")
        self.c1.remove(self.l2)
        self.assertEqual([], self.c1.locations, "l2 was not removed from the list of locations")

    def test_removeDoesntExists(self):
        self.c1.locations = [self.l1, self.l2]
        self.c1.remove(self.l3)
        self.assertEqual([self.l1, self.l2], self.c1.locations, "No location should have been removed when attempting"
                                                                " to remove l3")
        self.c1.locations = [self.l1]
        self.c1.remove(self.l2)
        self.c1.remove(self.l3)
        self.assertEqual([self.l1], self.c1.locations, "No locations should have been removed when attempting "
                                                       "to remove l2 and l3")

    def test_removeException(self):
        self.assertRaises(TypeError, self.c1.remove, self.falseLoc1)
        self.assertRaises(TypeError, self.c1.remove, self.falseLoc2)

    def test_size(self):
        self.c1.locations = [self.l1, self.l2, self.l3]
        self.assertEqual(3, self.c1.size(), "Number of locations should be 3")
        self.c1.locations = [self.l1, self.l2]
        self.assertEqual(2, self.c1.size(), "Number of locations should be 2")
        self.c1.locations = [self.l1]
        self.assertEqual(1, self.c1.size(), "Number of locations should be 1")
        self.c1.locations = []
        self.assertEqual(0, self.c1.size(), "Number of locations should be 0")

if __name__ == "__main__":
    unittest.main()
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(LocationCollectionUnitTests))
runner = unittest.TextTestRunner()
res = runner.run(suite)

print(res)
print("*" * 20)
for i in res.failures: print(i[1])