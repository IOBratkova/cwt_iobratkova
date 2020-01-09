import unittest
from classes.signinpage import SignInPage


class TestSignInPage(unittest.TestCase):
    def test_init(self):
        signinpage = SignInPage(2, 2)
        self.assertNotEqual(signinpage.driver, 10)
        self.assertNotEqual(signinpage.url, 40)
        self.assertEqual(signinpage.title, 'SignIn')