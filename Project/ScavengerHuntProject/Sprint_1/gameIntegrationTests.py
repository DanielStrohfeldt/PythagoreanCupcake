import unittest
from game import Game
from team import Team
from gameMaker import GameMaker
from loc import Loc
import sys
import StringIO

class GameIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.game = Game("Admin", "12345")
        self.gamemaker = GameMaker("Admin", "12345", self.game)
        self.t1 = Team("t1", "t1")
        self.t2 = Team("t2", "t2")
        self.t3 = Team("t3", "t3")
        self.l1 = Loc("l1", "l1", "l1", "l1")
        self.l2 = Loc("l2", "l2", "l2", "l2")
        self.l3 = Loc("l3", "l3", "l3", "l3")

    def test_call_login_no_user(self):
        self.game.teams.teams = [self.t2, self.t3]
        self.game.login("t1", "t1")
        self.assertEqual(self.game.currentUser, None, "There should be no current user since t1 is not a valid team")
        self.game.login("t4", "t4")
        self.assertEqual(self.game.currentUser, None, "There should be no current user since t4 is not a valid team")

    def test_call_login_user_exists(self):
        self.game.teams.teams = [self.t1, self.t3, self.t2]
        self.game.login("t1", "t1")
        self.assertEqual(self.game.currentUser, self.t1, "t1 should be the current user since they exist")
        self.game.currentUser = None
        self.game.login("t2", "t2")
        self.assertEqual(self.game.currentUser, self.t2, "t2 should be the current user since they exist")
        self.game.currentUser = None
        self.game.login("t3", "t3")
        self.assertEqual(self.game.currentUser, self.t3, "t3 should be the current user since they exist")

    def test_call_login_gamemaker(self):
        self.game.login("Admin", "12345")
        self.assertIsInstance(self.game.currentUser, GameMaker, "The games current user should be a GameMaker")
        self.game.currentUser = None
        self.game.login("Admin", "1456788i")
        self.assertIsNone(self.game.currentUser, "The games current user should be none since password is incorrect"
                                                 " for GameMaker")

    def test_end_has_users(self):
        self.game.teams.teams = [self.t1, self.t2, self.t3]
        self.t1.hasFinished = True
        self.t2.hasFinished = True
        self.t3.hasFinished = True
        self.t1.totalTime = 50
        self.t2.totalTime = 60
        self.t3.totalTime = 70
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.game.end()
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("The game has ended!\nWinner of the scavenger hunt game is team t1 with a score of 50\n",
                         capturedOutput.getvalue(), "Incorrect output, was: " + capturedOutput.getvalue())

    def test_end_no_users(self):
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.game.end()
        sys.stdout = sys.__stdout__
        self.assertEqual("The game has ended!\nNo winner since there are no teams!\n", capturedOutput.getvalue(),
                         "Incorrect output, was: " + capturedOutput.getvalue())

if __name__ == "__main__":
    unittest.main()
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(GameIntegrationTests))
runner = unittest.TextTestRunner()
res = runner.run(suite)

print(res)
print("*" * 20)
for i in res.failures: print(i[1])
