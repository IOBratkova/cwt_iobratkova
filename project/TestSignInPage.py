import unittest
from classes.signinpage import SignInPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class TestSignInPage(unittest.TestCase):
    def start_up(self):
        self.url = 'http://127.0.0.1:8080/#/signup'
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.maximize_window()
        self.signinpage = SignInPage(self.driver, self.url)

    def test_init(self):
        signinpage = SignInPage(2, 2)
        self.assertNotEqual(signinpage.driver, 10)
        self.assertNotEqual(signinpage.url, 40)
        self.assertEqual(signinpage.title, 'SignIn')

    def test_open_url(self):
        self.start_up()
        self.signinpage.open_url()
        title = self.signinpage.driver.title
        self.signinpage.driver.close()
        self.assertEqual('MADE HANDMADE', title)

    def test_find_elements(self):
        self.start_up()
        self.signinpage.open_url()
        self.signinpage.open_url()
        login = self.signinpage.login()
        self.assertNotEqual(login, None)
