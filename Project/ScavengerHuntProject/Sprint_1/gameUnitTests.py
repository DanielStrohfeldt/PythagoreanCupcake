import unittest
from game import Game
from teamSet import TeamSet
from team import Team
from locationSet import LocationSet
from loc import Loc
from gameMaker import GameMaker

class gameUnitTests(unittest.TestCase):

    def setUp(self):
        self.gmusername = "Admin"
        self.gmpassword = "12345"
        self.game = Game(self.gmusername, self.gmpassword)
        self.gamemaker = GameMaker(self.gmusername, self.gmpassword, self.game)
        self.s1 = TeamSet()
        self.u1 = "t1"
        self.u2 = "t2"
        self.u3 = "t3"
        self.p1 = "p1"
        self.p2 = "p2"
        self.p3 = "p3"
        self.t1 = Team(self.u1, self.p1)
        self.t2 = Team(self.u2, self.p2)
        self.t3 = Team(self.u3, self.p3)

        self.game.teams.add(self.t1)
        self.game.teams.add(self.t2)
        self.game.teams.add(self.t3)

        self.i1 = self.t1.get_iterator()
        self.i2 = self.t2.get_iterator()
        self.i3 = self.t3.get_iterator()

        self.t1.current_location = None
        self.t2.current_location = None
        self.t3.current_location = None

        self.sl1 = LocationSet()
        self.l1 = Loc("n1", "c1", "q1", "a1")
        self.l2 = Loc("n2", "c2", "q2", "a2")
        self.sl1.add(self.l1)
        self.sl1.add(self.l2)

        self.gamemaker.add_location("n1", "c1", "q1", "a1")
        self.gamemaker.add_location("n2", "c2", "q2", "a2")

        self.fakeusername1 = "fakeu1"
        self.fakepassword1 = "fakep1"
        self.fakeusername2 = "fakeu2"
        self.fakepassword2 = "fakep2"

    def test_login(self):
        print("Testing the Admin account...\n")
        self.game.login(self.gmusername, self.gmpassword)
        self.assertTrue(isinstance(self.game.get_currentuser(), GameMaker), "Should be able to login to Admin within"
                                                          " correct username and password")

        self.game.logout()
        self.game.login(self.u1, self.p1)
        self.assertEquals(self.game.get_currentuser(), self.t1, "Should be able to login to t1 within"
                          + " correct username and password")

        self.game.logout()
        self.game.login(self.u2, self.p2)
        self.assertEquals(self.game.get_currentuser(), self.t2, "Should be able to login to t2 within"
                          + " correct username and password")

        self.game.logout()
        self.game.login(self.u3, self.p3)
        self.assertEquals(self.game.get_currentuser(), self.t3, "Should be able to login to t3 within"
                          + " correct username and password")

        self.game.logout()
        self.game.login(self.fakeusername1, self.fakepassword1)
        self.assertEquals(self.game.get_currentuser(), None, "Should not be able to login within"
                          + " incorrect username and password")

        self.game.logout()
        self.game.login(self.fakeusername2, self.fakepassword2)
        self.assertEquals(self.game.get_currentuser(), None, "Should not be able to login within"
                          + " incorrect username and password")

        self.game.logout()
        self.game.login(self.u1, self.p2)
        self.assertEquals(self.game.get_currentuser(), None, "Should not be able to login within"
                          + " incorrect username and password")

    def test_start(self):
        self.game.login(self.gmusername, self.gmpassword)
        self.game.start()
        self.assertEquals(self.game.is_running(), True, "Should be able to run the game with admin's permission")

    def test_play(self):
        self.game.login(self.u1, self.p1)
        self.assertEquals(self.game.currentUser.get_currentlocation(), None, "user should be at the 'none' location since the game is not started by admin")
        self.game.play(False)
        self.assertEquals(self.game.currentUser.get_currentlocation(), None, "user should be at the same location since the game is not started by admin")
        self.game.logout()
        self.game.login(self.gmusername, self.gmpassword)
        self.game.start()
        self.game.logout()
        self.game.login(self.u1, self.p1)
        self.assertEquals(self.game.currentUser.get_currentlocation(), None,
                          "user should be at the 'none' location since the user did not start 'playing'")
        self.game.get_currentuser().moveon()
        self.assertEquals(self.game.currentUser.get_currentlocation().get_name(), self.l1.get_name(),
                          "user should be at the 'l1' location since the user started 'playing'")

        a = self.game.currentUser.get_currentlocation()
        self.assertNotEquals(a, None, "user should be at the first location since the user do the first move")
        self.assertEquals(a.get_name(), self.l1.get_name(), "user should be at first location after the first move")
        self.t1.start_time()
        self.game.answer("a1")
        b = self.game.currentUser.get_currentlocation()
        self.assertEquals(b.get_name(), self.l2.get_name(), "user should be at l2 after answered the question correctly")
        self.assertNotEquals(a.get_name(), b.get_name(), "user should not be at the same location as it have before")

        self.game.logout()
        self.t1.current_location = self.l2
        self.t2.current_location = self.l2
        self.t3.current_location = self.l2

        self.game.login(self.u2, self.p2)
        a = self.game.currentUser.get_currentlocation()
        self.assertEquals(a.get_name(), self.l2.get_name(), "user should be at the l2 location")
        self.t2.start_time()
        self.game.answer("q2")
        b = self.game.currentUser.get_currentlocation()

    def test_end(self):
        self.game.end()
        self.assertEquals(self.game.is_running(), False, "Game should stop running since the admin stop the game")
        self.assertEquals(self.t1.get_finalscore(), None, "team t1 should be able to get it"
                                                             " score since it's winning team")
        self.assertEquals(self.t2.get_finalscore(), None, "team t2 should be not be able to get it final score"
                                                          " since it's not the winnning team")
        self.assertEquals(self.t3.get_finalscore(), None, "team t3 should be not be able to get it final score"
                                                          " since it's not the winning team")

        self.game.start()
        self.t1.current_location = None
        self.t2.current_location = None
        self.t3.current_location = None

        self.game.end()

        self.assertEquals(self.game.is_running(), False, "Game should stop running since the admin stop the game")
        self.assertEquals(self.t1.get_finalscore(), None, "team t1 should not be able to get it final score"
                                                             " score since it's winning team")
        self.assertEquals(self.t2.get_finalscore(), None, "team t2 should not be able to get it final score"
                                                          " since it's not the winnning team")
        self.assertEquals(self.t3.get_finalscore(), None, "team t3 should not be able to get it final score"
                                                          " since it's not the winning team")


if __name__ == "__main__":
    unittest.main()
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(gameUnitTests))
runner = unittest.TextTestRunner()
res = runner.run(suite)

print(res)
print("*" * 20)
for i in res.failures: print(i[1])