from interface import interface
from game import Game
from gameMaker import GameMaker
from team import Team
from loc import Loc
from user import User
#import StringIO
import sys
import unittest

class AcceptanceTests(unittest.TestCase):
    #this game has no/teams locations
    def setUp(self):
        self.game = Game("admin", "123")
        self.gm = GameMaker("admin", "123", self.game)
        self.one = interface(self.game, self.gm)

    #The following are scenarios that shouldn't work
    def test_start_game_with_no_teamslocations(self):
        self.game.login("admin", "123")
        self.game.start()
        self.assertFalse(self.game.running, "Game was started without any teams or locations")
        #add just teams and start
        self.game.teams.add(Team("t1", "t1"))
        self.game.teams.add(Team("t2", "t2"))
        self.game.start()
        self.assertFalse(self.game.running, "Game has teams but no locations")
        #reset teams
        self.game.teams.clear()

        #add just locations
        self.game.locations.add(Loc("name", "Q", "A", "C"))
        self.game.locations.add(Loc("name2", "Q2", "A2", "C2"))
        self.game.start()
        self.assertFalse(self.game.running, "Game was started without teams")

        #start game witj
        self.game.teams.add(Team("t1", "t1"))
        self.game.start()
        self.assertTrue(self.game.running, "Game has teams and locations but isn't started after calling start() should be")

    def test_add_location_after_game_starts(self):
        self.game.login("admin", "123")
        self.game.teams.add(Team("t1", "t2"))
        self.game.locations.add(Loc("a", "b", "c", "d"))
        self.game.start()

        self.gm.add_location("not", "good", "loc", "added")
        self.assertEqual(self.game.teams.size(), 1, "Error: Added a location after the game started")

    def test_team_change_game_fields(self):
        self.game.login("admin", "123")
        self.game.teams.add(Team("t1", "t2"))
        self.game.locations.add(Loc("a", "b", "c", "d"))
        self.game.logout()
        self.game.login("t1", "t2")
        self.one.command("start")

        self.assertFalse(self.game.running, "Game was started by a logged in team")

        self.game.logout()
        self.game.login("admin", "123")
        self.game.start()
        self.game.logout()
        self.game.login("t1", "t2")
        self.one.command("end")

        self.assertTrue(self.game.running, "Game was ended by someone other than GameMaker")

    def test_add_gamemaker_to_game(self):
        self.game.login("admin", "123")
        with self.assertRaises(TypeError):
            self.game.teams.add(GameMaker("admin2", "321", self.game))

        self.assertEqual(self.game.teams.size(), 0, "GameMaker was added to the game!")

    def test_second_game_maker(self):
        gm2 = GameMaker("admin2", "321", self.game)

        self.game.login("admin2", "321")
        self.assertEqual(self.game.currentUser, None, "Allowed a second gameMaker to enter the game.")

    def test_addTeam(self):
        sys.stdin = open('addteam_acceptancetest.txt', 'r')
        self.one.command("login")
        self.assertIsInstance(self.game.currentUser, GameMaker, "Current user should be GameMaker after GameMaker logs in")
        self.one.command("add team")
        self.assertEqual(1, len(self.game.teams.teams), "Team was not successfully added to the game")
        self.assertEqual("Bill", self.game.teams.teams[0].username, "Team 'Bill' is not present in the game")
        self.one.command("add team")
        self.assertEqual(2, len(self.game.teams.teams), "Team was not successfully added to the game")
        self.assertEqual("Steve", self.game.teams.teams[1].username, "Team 'Steve' is not present in the game")
        self.one.command("add team")
        self.assertEqual(3, len(self.game.teams.teams), "Team was not successfully added to the game")
        self.assertEqual("Apple", self.game.teams.teams[2].username, "Team 'Apple' is not present in the game")


if __name__ == "__main__":
    unittest.main()
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(AcceptanceTests))
runner = unittest.TextTestRunner()
res = runner.run(suite)

print(res)
print("*" * 20)
for i in res.failures: print(i[1])