from team import Team
from loc import Loc
import unittest
import StringIO
import sys

class TeamUnitTests(unittest.TestCase):
    def setUp(self):
        self.team1 = Team("Matthew", "12345")
        self.nums = [1,2,3]
        self.loc1 = Loc("loc1", "", "", "")
        self.it1 = iter(self.nums)
        self.it2 = iter([])

    def test_init(self):
        self.assertEqual("Matthew", self.team1.username, "team1's username was not properly set upon initialization")
        self.assertEqual("12345", self.team1.password, "team1's password was not properly set upon initialization")
        self.assertEqual(None, self.team1.startTime, "team1's startTime should be None upon initialization")
        self.assertEqual(None, self.team1.iterator, "team1's iterator should be None upon initialization")
        self.assertEqual(0, self.team1.penalties, "team1's penalties should be 0 upon initialization")

    def test_startTime(self):
        self.assertEqual(None, self.team1.startTime, "team1's start time should be None before start_time() is called")
        self.team1.start_time()
        self.assertNotEqual(None, self.team1.startTime, "team1's start time should not be None after start_time() is "
                                                        "called")

    def test_getStartTime(self):
        self.assertEqual(None, self.team1.get_starttime(), "get_starttime() should return None but returned "
                         + str(self.team1.get_starttime()))
        self.team1.startTime = 20
        self.assertEqual(20, self.team1.get_starttime(), "get_starttime() should return 20 but returned "
                         + str(self.team1.get_starttime()))
        self.team1.startTime = 40
        self.assertEqual(40, self.team1.get_starttime(), "get_starttime() should return 40 but returned "
                         + str(self.team1.get_starttime()))
        self.team1.startTime = 60
        self.assertEqual(60, self.team1.get_starttime(), "get_starttime() should return 60 but returned "
                         + str(self.team1.get_starttime()))

    def test_endTime(self):
        self.team1.startTime = 0
        self.team1.end_time()
        self.assertGreater(self.team1.totalTime, 0, "team1's totalTime should increase when end time is called")
        temp = self.team1.totalTime
        self.team1.end_time()
        self.assertGreater(self.team1.totalTime, temp, "team1's totalTime should increase when end_time is called")
        temp = self.team1.totalTime
        self.team1.end_time()
        self.assertGreater(self.team1.totalTime, temp, "team1's totalTime should increase when end_time is called")

    def test_getPenalties(self):
        self.assertEqual(0, self.team1.get_penalites(), "get_penalties() should return 0 but returned "
                         + str(self.team1.get_penalites()))
        self.team1.penalties = 1
        self.assertEqual(1, self.team1.get_penalites(), "get_penalties() should return 1 but returned "
                         + str(self.team1.get_penalites()))
        self.team1.penalties = 2
        self.assertEqual(2, self.team1.get_penalites(), "get_penalties() should return 2 but returned "
                         + str(self.team1.get_penalites()))
        self.team1.penalties = 3
        self.assertEqual(3, self.team1.get_penalites(), "get_penalties() should return 3 but returned "
                         + str(self.team1.get_penalites()))

    def test_addPenalty(self):
        self.assertEqual(0, self.team1.penalties, "team1's penalties should initially be 0")
        self.team1.add_penalty()
        self.assertEqual(1, self.team1.penalties, "team1's penalties should be 1 after calling add_penalty()")
        self.team1.add_penalty()
        self.assertEqual(2, self.team1.penalties, "team1's penalties should be 2 after calling add_penalty()")
        self.team1.add_penalty()
        self.assertEqual(3, self.team1.penalties, "team1's penalties should be 3 after calling add_penalty()")
        self.team1.add_penalty()
        self.assertEqual(4, self.team1.penalties, "team1's penalties should be 4 after calling add_penalty()")

    def test_setIterator(self):
        self.assertEqual(None, self.team1.iterator, "team1's iterator should be None initially")
        self.team1.set_iterator(self.it1)
        self.assertEqual(self.it1, self.team1.iterator, "team1's iterator should be it1 after calling"
                                                           " set_iterator(it1)")
        self.team1.set_iterator(self.it2)
        self.assertEqual(self.it2, self.team1.iterator, "team1's iterator should be it2 after calling"
                                                        " set_iterator(it2)")

    def test_getIterator(self):
        self.assertEqual(None, self.team1.get_iterator(), "get_iterator() should initially return None")
        self.team1.iterator = self.it1
        self.assertEqual(self.it1, self.team1.get_iterator(), "get_iterator() should return it1 after the iterator"
                                                              " is set to it1")
        self.team1.iterator = self.it2
        self.assertEqual(self.it2, self.team1.get_iterator(), "get_iterator() should return it2 after the iterator"
                                                              " is set to it2")

    def test_finalScore(self):
        self.team1.totalTime = 3
        self.team1.hasFinished = True
        self.team1.penalties = 0
        self.assertEqual(3, self.team1.get_finalscore(), "get_finalscore() should return 3 but returned "
                         + str(self.team1.get_finalscore()))
        self.team1.totalTime = 30
        self.team1.penalties = 5
        self.assertEqual(35, self.team1.get_finalscore(), "get_finalscore() should return 35 but returned "
                         + str(self.team1.get_finalscore()))
        self.team1.totalTime = 297
        self.team1.penalties = 10
        self.assertEqual(307, self.team1.get_finalscore(), "get_finalscore() should return 307 but returned "
                         + str(self.team1.get_finalscore()))

    def test_finalScoreNotFinished(self):
        self.team1.hasFinished = False
        self.team1.totalTime = 5
        self.team1.penalties = 6
        self.assertEqual(None, self.team1.get_finalscore(), "If the team has not finished they shouldn't have a final"
                                                            " score")

    def test_hasfinished(self):
        self.team1.hasFinished = False
        self.assertEqual(False, self.team1.has_finished(), "If the hasFinished field is false, the has_finished() "
                                                           "method should return false")
        self.team1.hasFinished = True
        self.assertEqual(True, self.team1.has_finished(), "If the hasFinished field is true, the has_finished() "
                                                          "method should return true")

    def test_addattempts(self):
        self.assertEqual(0, self.team1.attempted, "team1's attempts should initially be 0")
        self.team1.add_attempt()
        self.assertEqual(1, self.team1.attempted, "team1's attempts should be 1 after calling add_attempt()")
        self.team1.add_attempt()
        self.assertEqual(2, self.team1.attempted, "team1's attempts should be 2 after calling add_attempt()")
        self.team1.add_attempt()
        self.assertEqual(3, self.team1.attempted, "team1's attempts should be 3 after calling add_attempt()")
        self.team1.add_attempt()
        self.assertEqual(4, self.team1.attempted, "team1's attempts should be 4 after calling add_attempt()")

    def test_getattempts(self):
        self.assertEqual(0, self.team1.get_attempts(), "get_attempts() should return 0")
        self.team1.attempted = 1
        self.assertEqual(1, self.team1.get_attempts(), "get_attempts() should return 1")
        self.team1.attempted = 25
        self.assertEqual(25, self.team1.get_attempts(), "get_attempts() should return 25")
        self.team1.attempted = 76
        self.assertEqual(76, self.team1.get_attempts(), "get_attempts() should return 76")

    def test_moveonNoIterator(self):
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.team1.moveon()  # Call unchanged function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("Cannot move on, team does not have iterator over the current locations\n",
                         capturedOutput.getvalue(), "Error should be printed when team1.moveon() is called without an"
                                                        " iterator")

    def test_moveonNoNextLocation(self):
        self.team1.iterator = self.it2
        self.team1.moveon()
        self.assertEqual(True, self.team1.hasFinished, "If there are no more locations to iterator over, "
                                                       "then the hasFinished flag should be set to true")

    def test_moveonHasNextLocation(self):
        self.team1.iterator = self.it1
        self.team1.moveon()
        self.assertEqual(1, self.team1.current_location, "team1's current location should be 1 after moveon() is called")
        self.assertEqual(False, self.team1.hasFinished, "hasFinished should be false since there are more locations to"
                                                        " iterate over")
        self.team1.moveon()
        self.assertEqual(2, self.team1.current_location, "team1's current location should be 2 after moveon() is called")
        self.assertEqual(False, self.team1.hasFinished, "hasFinished should be false since there are more locations to"
                                                        " iterate over")
        self.team1.moveon()
        self.assertEqual(3, self.team1.current_location, "team1's current location should be 3 after moveon() is called")
        self.assertEqual(False, self.team1.hasFinished, "hasFinished should be false since there are more locations to"
                                                        " iterate over")

    def test_printstatusNotFinished(self):
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.team1.totalTime = 5
        self.team1.penalties = 5
        self.team1.current_location = self.loc1
        self.team1.print_status()  # Call unchanged function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("Team: Matthew  Current location: loc1  Total time(so far): 5  Total penalties: 5\n",
                         capturedOutput.getvalue(), "print_status() did not print the correct string")

    def test_printstatusFinished(self):
        capturedOutput = StringIO.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        self.team1.totalTime = 5
        self.team1.penalties = 5
        self.team1.hasFinished = True
        self.team1.current_location = self.loc1
        self.team1.print_status()  # Call unchanged function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual("Team: Matthew  Finished game.  Final score = 10\n",
                         capturedOutput.getvalue(), "print_status() did not print the correct string")


if __name__ == "__main__":
    unittest.main()
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TeamUnitTests))
runner = unittest.TextTestRunner()
res = runner.run(suite)

print(res)
print("*" * 20)
for i in res.failures: print(i[1])