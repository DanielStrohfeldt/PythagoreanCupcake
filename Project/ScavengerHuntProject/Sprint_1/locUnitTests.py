from loc import Loc
import unittest


class LocUnitTests(unittest.TestCase):
    def setUp(self):
        name1 = "Tree in park"
        question1 = "Is there a bench to the right of the tree?"
        answer1 = "Yes"
        clue1 = "This location is next to the UWM library"
        self.l1 = Loc(name1, question1, answer1, clue1)
        name2 = "ems 180"
        question2 = "Is there a stage up front?"
        answer2 = "Yes"
        clue2 = "This location is within the EMS building and is one of the main lecture halls"
        self.l2 = Loc(name2, question2, answer2, clue2)

    def test_init(self):
        self.assertEqual("tree in park", self.l1.name, "l1's name was not set properly upon instantiation")
        self.assertEqual("Is there a bench to the right of the tree?", self.l1.question, "l1's question was not "
                                                                                         "set properly upon "
                                                                                         "instantiation")
        self.assertEqual("yes", self.l1.answer, "l1's answer was  not set properly upon instantiation")
        self.assertEqual("ems 180", self.l2.name, "l2's name was not set properly upon instantiation")
        self.assertEqual("Is there a stage up front?", self.l2.question, "l2's question was not set properly upon "
                                                                         "instantiation")
        self.assertEqual("yes", self.l2.answer, "l2's answer was  not set properly upon instantiation")

    def test_initNone(self):
        self.assertRaises(TypeError, Loc, None, "Test Q", "Test A")
        self.assertRaises(TypeError, Loc, "Test name", None, "Test A")
        self.assertRaises(TypeError, Loc, "Test name", "Test Q", None)
        self.assertRaises(TypeError, Loc, None, None, None)
        self.assertRaises(TypeError, Loc, None, None, "Test A")
        self.assertRaises(TypeError, Loc, None, "Test Q", None)
        self.assertRaises(TypeError, Loc, "Test name", None, None)

    def test_getName(self):
        self.assertEqual("tree in park", self.l1.get_name(), "get_name() did not return correct name for l1")
        self.assertEqual("ems 180", self.l2.get_name(), "get_name() did not return correct name for l2")

    def test_setName(self):
        name1 = "new tree in park"
        name2 = "ems 190"
        self.assertEqual("tree in park", self.l1.name, "name is upon instantiation of l1")
        self.l1.set_name(name1)
        self.assertEqual("new tree in park", self.l1.name, "name was not properly set for l1")
        self.l2.set_name(name2)
        self.assertEqual("ems 190", self.l2.name, "name was not properly set for l1")

    def test_getQuestion(self):
        self.assertEqual("Is there a bench to the right of the tree?", self.l1.get_question(), "get_question()"
                                                                                               " returned wrong "
                                                                                               "question for l1")
        self.assertEqual("Is there a stage up front?", self.l2.get_question(), "get_question() returned wrong"
                                                                               " question for l2")

    def test_setQuestion(self):
        q1 = "Is there a pine tree within 5 feet of your current location?"
        q2 = "Is there a chair up front?"
        self.l1.set_question(q1)
        self.assertEqual("Is there a pine tree within 5 feet of your current location?", self.l1.question, "l1's"
                                                                                    " question was not set properly")
        self.l2.set_question(q2)
        self.assertEqual("Is there a chair up front?", self.l2.question, "l2's question was not set properly")

    def test_getanswer(self):
        self.assertEqual("yes", self.l1.get_answer(), "get_answer() for l1 should return yes in all lowercase letters")
        self.assertEqual("yes", self.l2.get_answer(), "get_answer() for l2 should return yes in all lowercase letters")

    def test_setanswer(self):
        a = "No"
        a2 = "Possibly, I don't know"
        self.l1.set_answer(a)
        self.assertEqual("no", self.l1.answer, "l1's answer was not set properly")
        self.l2.set_answer(a2)
        self.assertEqual("possibly, i don't know", self.l2.answer, "l2's answer was not set properly")

    def test_getclue(self):
        self.assertEqual("This location is next to the UWM library", self.l1.get_clue(), "get_clue() did not "
                                                                                         "return the correct clue "
                                                                                         "for l1")
        self.assertEqual("This location is within the EMS building and is one of the main lecture halls",
                         self.l2.get_clue(), "get_clue() did not return the correct clue for l2")

    def test_setclue(self):
        clue1 = "This is the changed clue for l1"
        clue2 = "This is the changed clue for l2"
        self.l1.set_clue(clue1)
        self.assertEqual("This is the changed clue for l1", self.l1.clue, "l1's clue was not set properly")
        self.l2.set_clue(clue2)
        self.assertEqual("This is the changed clue for l2", self.l2.clue, "l2's clue was not set properly")


if __name__ == "__main__":
    unittest.main()
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(LocUnitTests))
runner = unittest.TextTestRunner()
res = runner.run(suite)

print(res)
print("*" * 20)
for i in res.failures: print(i[1])