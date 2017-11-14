import unittest
from teamSet import TeamSet
from team import Team


class LocationCollectionUnitTests(unittest.TestCase):
    def setUp(self):
        self.c1 = TeamSet()
        self.t1 = Team("team1", "password1")
        self.t2 = Team("team2", "password2")
        self.t3 = Team("team3", "question3")
        self.falseTeam1 = "This is not a team 1"
        self.falseTeam2 = 0

    def test_add(self):
        self.c1.add(self.t1)
        self.assertEqual([self.t1], self.c1.teams, "t1 should have been added to list of teams")
        self.c1.add(self.t2)
        self.assertEqual([self.t1, self.t2], self.c1.teams, "t2 should have been added to list of teams")
        self.c1.add(self.t3)
        self.assertEqual([self.t1, self.t2, self.t3], self.c1.teams, "t3 should have been added to list of teams")

    def test_addAlreadyExists(self):
        self.c1.teams = [self.t1, self.t2, self.t3]
        self.c1.add(self.t1)
        self.assertEqual([self.t1, self.t2, self.t3], self.c1.teams, "t1 should not have been added twice to the "
                                                                     "list of teams")
        self.c1.add(self.t2)
        self.assertEqual([self.t1, self.t2, self.t3], self.c1.teams, "t2 should not have been added twice to the "
                                                                     "list of teams")
        self.c1.add(self.t3)
        self.assertEqual([self.t1, self.t2, self.t3], self.c1.teams, "t3 should not have been added twice to the"
                                                                     " list of teams")

    def test_addException(self):
        self.assertRaises(TypeError, self.c1.add, self.falseTeam1)
        self.assertRaises(TypeError, self.c1.add, self.falseTeam2)

    def test_remove(self):
        self.c1.teams = [self.t1, self.t2, self.t3]
        self.c1.remove(self.t3)
        self.assertEqual([self.t1, self.t2], self.c1.teams, "t3 was not removed from the list of teams")
        self.c1.remove(self.t1)
        self.assertEqual([self.t2], self.c1.teams, "t1 was not removed from the list of teams")
        self.c1.remove(self.t2)
        self.assertEqual([], self.c1.teams, "t2 was not removed from the list of teams")

    def test_removeDoesntExists(self):
        self.c1.teams = [self.t1, self.t2]
        self.c1.remove(self.t3)
        self.assertEqual([self.t1, self.t2], self.c1.teams, "No teams should have been removed when attempting "
                                                            "to remove l3")
        self.c1.teams = [self.t1]
        self.c1.remove(self.t2)
        self.c1.remove(self.t3)
        self.assertEqual([self.t1], self.c1.teams, "No teams should have been removed when attempting "
                                                   "to remove t2 and t3")

    def test_removeException(self):
        self.assertRaises(TypeError, self.c1.remove, self.falseTeam1)
        self.assertRaises(TypeError, self.c1.remove, self.falseTeam2)

    def test_size(self):
        self.c1.teams = [self.t1, self.t2, self.t3]
        self.assertEqual(3, self.c1.size(), "Number of teams should be 3")
        self.c1.teams = [self.t1, self.t2]
        self.assertEqual(2, self.c1.size(), "Number of teams should be 2")
        self.c1.teams = [self.t1]
        self.assertEqual(1, self.c1.size(), "Number of teams should be 1")
        self.c1.teams = []
        self.assertEqual(0, self.c1.size(), "Number of teams should be 0")


if __name__ == "__main__":
    unittest.main()
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(LocationCollectionUnitTests))
runner = unittest.TextTestRunner()
res = runner.run(suite)

print(res)
print("*" * 20)
for i in res.failures: print(i[1])