from user import User
import unittest


class UserUnitTests(unittest.TestCase):
    def setUp(self):
        self.u1 = User("Matthew", "12345")
        self.u2 = User("Jacob", "6789")

    def test_init(self):
        self.assertEqual("Matthew", self.u1.username, "u1's username was not set properly upon initialization")
        self.assertEqual("12345", self.u1.password, "u1's password was not set properly upon initialization")
        self.assertEqual("Jacob", self.u2.username, "u2's username was not set properly upon initialization")
        self.assertEqual("6789", self.u2.password, "u2's password was not set properly upon initialization")

    def test_getUsername(self):
        self.assertEqual("Matthew", self.u1.get_username(), "get_username() did not return u1's correct username")
        self.assertEqual("Jacob", self.u2.get_username(), "get_username() did not return u2's correct username")

    def test_getPassword(self):
        self.assertEqual("12345", self.u1.get_password(), "get_password() did not return u1's correct password")
        self.assertEqual("6789", self.u2.get_password(), "get_password() did not return u2's correct password")

    def test_setUsername(self):
        self.u1.set_username("Matt")
        self.assertEqual("Matt", self.u1.username, "set_username() did not change u1's username correctly")
        self.u1.set_username("Matt F")
        self.assertEqual("Matt F", self.u1.username, "set_username() did not change u1's username correctly")

    def test_setPassword(self):
        self.u1.set_password("54321")
        self.assertEqual("54321", self.u1.password, "set_password() did not change u1's password correctly")
        self.u1.set_password("12345 6789")
        self.assertEqual("12345 6789", self.u1.password, "set_password() did not change u1's password correctly")


if __name__ == "__main__":
    unittest.main()
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(UserUnitTests))
runner = unittest.TextTestRunner()
res = runner.run(suite)

print(res)
print("*" * 20)
for i in res.failures: print(i[1])