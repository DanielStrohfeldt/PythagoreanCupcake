import unittest
from loc import Loc
from team import Team
from game import Game
from gameMaker import GameMaker
import StringIO
import sys

class GameMakerIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.t1 = Team("t1", "t1")
        self.t2 = Team("t2", "t2")
        self.t3 = Team("t3", "t3")
        self.l1 = Loc("l1", "l1", "l1", "l1")
        self.l2 = Loc("l2", "l2", "l2", "l2")
        self.l3 = Loc("l3", "l3", "l3", "l3")
        self.game = Game("Admin", "12345")
        self.gamemaker = GameMaker("Admin", "12345", self.game)


    def test_add_team_exists(self):
        self.game.teams.teams = [self.t1, self.t2, self.t3]
        self.gamemaker.add_team("t1", "t1")
        self.assertEqual([self.t1, self.t2, self.t3], self.game.teams.teams, "No teams should have been added since "
                                                                             "t1 is already an existing team")
        self.gamemaker.add_team("t2", "t2")
        self.assertEqual([self.t1, self.t2, self.t3], self.game.teams.teams, "No teams should have been added since "
                                                                             "t2 is already an existing team")
        self.gamemaker.add_team("t3", "t3")
        self.assertEqual([self.t1, self.t2, self.t3], self.game.teams.teams, "No teams should have been added since "
                                                                             "t3 is already an existing team")

    def test_add_team_not_exists(self):
        self.game.teams.teams = []
        self.gamemaker.add_team("t1", "t1")
        self.assertEqual(1, self.game.teams.size(), "The game should have 1 team after t1 is added")
        self.gamemaker.add_team("t2", "t2")
        self.assertEqual(2, self.game.teams.size(), "The game should have 2 teams after t2 is added")
        self.gamemaker.add_team("t3", "t3")
        self.assertEqual(3, self.game.teams.size(), "The game should have 3 teams after t3 is added")

    def test_add_location_exists(self):
        self.game.locations.locations = [self.l1, self.l2, self.l3]
        self.gamemaker.add_location("l1", "l1", "l1", "l1")
        self.assertEqual([self.l1, self.l2, self.l3], self.game.locations.locations, "No locations should have been "
                                                                                     "been added since l1 already exists")
        self.gamemaker.add_location("l2", "l2", "l2", "l2")
        self.assertEqual([self.l1, self.l2, self.l3], self.game.locations.locations, "No locations should have been "
                                                                                     "been added since l2 already exists")
        self.gamemaker.add_location("l3", "l3", "l3", "l3")
        self.assertEqual([self.l1, self.l2, self.l3], self.game.locations.locations, "No locations should have been "
                                                                                     "been added since l3 already exists")

    def test_add_location_not_exists(self):
        self.game.locations.locations = []
        self.gamemaker.add_location("l1", "l1", "l1", "l1")
        self.assertEqual(1, self.game.locations.size(), "The game should have 1 team after l1 is added")
        self.gamemaker.add_location("l2", "l2", "l2", "l2")
        self.assertEqual(2, self.game.locations.size(), "The game should have 2 teams after l2 is added")
        self.gamemaker.add_location("l3", "l3", "l3", "l3")
        self.assertEqual(3, self.game.locations.size(), "The game should have 3 teams after l3 is added")

    def test_status(self):
        self.game.teams.teams = [self.t1, self.t2, self.t3]
        self.t1.current_location = self.l1
        self.t2.current_location = self.l2
        self.t3.current_location = self.l3
        self.t1.totalTime = 50
        self.t2.totalTime = 60
        self.t3.totalTime = 70
        s = "Team: t1  Current location: l1  Total time(so far): 50  Total penalties: 0\n" \
            "Team: t2  Current location: l2  Total time(so far): 60  Total penalties: 0\n" \
            "Team: t3  Current location: l3  Total time(so far): 70  Total penalties: 0\n"
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.gamemaker.print_status()
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(s, capturedOutput.getvalue(), "Print status did not print correctly")


if __name__ == "__main__":
    unittest.main()
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(GameMakerIntegrationTests))
runner = unittest.TextTestRunner()
res = runner.run(suite)

print(res)
print("*" * 20)
for i in res.failures: print(i[1])