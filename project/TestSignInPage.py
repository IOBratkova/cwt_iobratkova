import unittest
from classes.signinpage import SignInPage
from selenium import webdriver


class TestSignInPage(unittest.TestCase):
    def start_up(self):
        self.url = 'http://127.0.0.1:8080/#/signin'
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.maximize_window()

    def test_init(self):
        signinpage = SignInPage(2, 2)
        self.assertNotEqual(signinpage.driver, 10)
        self.assertNotEqual(signinpage.url, 40)
        self.assertEqual(signinpage.title, 'SignIn')

    def test_open_url(self):
        self.start_up()
        signinpage = SignInPage(self.driver, self.url)
        signinpage.open_url()
        title = signinpage.driver.title
        self.assertEqual('MADE HANDMADE', title)
