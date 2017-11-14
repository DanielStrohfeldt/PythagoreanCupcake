import unittest
import StringIO
import sys
from game import Game
from gameMaker import GameMaker


class TestGameMaker(unittest.TestCase):
    def setUp(self):
        self.Game = Game("admin", "admin")
        self.GameMaker = GameMaker("admin", "admin", self.Game)

    def test_add_team(self):
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.GameMaker.add_team("test", "test2")
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("Team '" + "test" + "' has been successfully added to the game\n",
                         capturedOutput.getvalue(), "Team should have been added")

    def test_add_team_exists(self):
        self.GameMaker.add_team("test", "test2")
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.GameMaker.add_team("test", "test2")
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("Team '" + "test" + "' could not be added to the game, this team already exists\n",
                         capturedOutput.getvalue(), "Team shouldn't have been added")

    def test_remove_team(self):
        self.GameMaker.add_team("test", "test2")
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.GameMaker.remove_team("test")
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("Team '" + "test" + "' was successfully removed\n",
                         capturedOutput.getvalue(), "Team should have been removed")

    def test_remove_team_non_exist(self):
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.GameMaker.remove_team("test")
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("Team '" + "test" + "'could not be removed, the team does not exist\n",
                         capturedOutput.getvalue(), "Team shouldn't have been removed")

    def test_add_location(self):
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.GameMaker.add_location("test", "test2", "test3", "test4")
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("Location '" + "test" + "' has been successfully added to the game\n",
                         capturedOutput.getvalue(), "Location should have been added")

    def test_add_location_exists(self):
        self.GameMaker.add_location("test", "test2", "test3", "test4")
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.GameMaker.add_location("test", "test2", "test3", "test4")
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("Location '" + "test" + "' could not be added to the game, this location already exists\n",
                         capturedOutput.getvalue(), "Location should'nt have been added")

    def test_print(self):
        self.GameMaker.add_location("test", "test2", "test3", "test4")
        self.GameMaker.add_team("test", "test2")
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.GameMaker.print_status()
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("Team: " + "test" + "  Current location: None  Total time(so far): 0  Total penalties: 0\n",
                         capturedOutput.getvalue(), "Print statment doesn't match")


if __name__ == "__main__":
    unittest.main()
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestGameMaker))
runner = unittest.TextTestRunner()
res = runner.run(suite)

print(res)
print("*" * 20)
for i in res.failures: print(i[1])
