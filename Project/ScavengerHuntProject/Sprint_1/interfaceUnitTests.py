import unittest
import sys

from interface import interface
from game import Game
from gameMaker import GameMaker
from team import Team
from location import Location


class interfaceUnitTests(unittest.TestCase):
    def setUp(self):
        self.game = Game(gmusername='king', gmpassword='plebs')
        self.game_maker = GameMaker(username='king', password='plebs', game=self.game)
        self.inter = interface(game=self.game, gamemaker=self.game_maker)
        self.t1 = Team("Matt", "F")
        self.t2 = Team("Chubby", "Chase")

    def test_instantiation(self):
        self.assertIsInstance(self.inter, interface)
        self.assertEqual(self.game, self.inter.game)
        self.assertEqual(self.game_maker, self.inter.gamemaker)

    def test_prompt_login(self):
        sys.stdin = open('gamemaker_login.txt', 'r')
        self.inter.prompt_login()
        self.assertIsInstance(self.inter.game.currentUser, GameMaker)

    def test_prompt_add_remove_edit_team(self):
        sys.stdin = open('teammaker.txt', 'r')
        self.inter.prompt_addteam()
        self.assertIsInstance(self.inter.game.teams.get('chubbyChasers'), Team)
        self.inter.prompt_login()
        self.assertIsInstance(self.inter.game.currentUser, Team)
        self.inter.prompt_editcredentials()
        self.assertEqual('chase', self.inter.game.currentUser.password)
        self.inter.prompt_editcredentials()
        self.assertEqual('chubby', self.inter.game.currentUser.username)
        self.inter.prompt_removeteam()
        self.assertEqual(self.inter.game.teams.get('chubby'), None)

    def test_prompt_add_location(self):
        sys.stdin = open('addlocation.txt', 'r')
        self.inter.prompt_addlocation()
        location = self.inter.game.locations.get('paradise')
        self.assertIsInstance(location, Location)

    def test_prompt_remove_team(self):
        self.game.teams.add(Team("chase", "chubby"))
        t = self.game.teams.get("chase")
        self.assertNotEqual(t, None)
        sys.stdin = open('removeteam.txt', 'r')
        self.inter.prompt_removeteam()
        t = self.inter.game.teams.get('chubby')
        self.assertEqual(t, None)

    def test_prompt_edit_credentials(self):
        self.game.teams.add(Team("chase", "chubby"))
        self.game.teams.add(Team("Matt", "F"))
        sys.stdin = open('editcredentials.txt', 'r')
        self.game.currentUser = self.t1
        self.inter.prompt_editcredentials()
        self.assertEqual(self.game.currentUser.username, "Matthew")
        self.game.currentUser = self.t2
        self.inter.prompt_editcredentials()
        self.assertEqual(self.game.currentUser.password, "newchubbypassword")

if __name__ == "__main__":
    unittest.main()
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(interfaceUnitTests))
runner = unittest.TextTestRunner()
res = runner.run(suite)

print(res)
print("*" * 20)
for i in res.failures: print(i[1])