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
        self.signinpage.close_driver()
        self.assertEqual('MADE HANDMADE', title)

    def test_find_elements(self):
        self.start_up()
        self.signinpage.open_url()
        self.signinpage.open_url()
        login = self.signinpage.login()
        self.assertNotEqual(login, None)
        email = self.signinpage.email()
        self.assertNotEqual(email, None)
        name = (self.signinpage.firstName(), self.signinpage.lastName())
        self.assertNotEqual(name[0], None)
        self.assertNotEqual(name[1], None)
        note = (self.signinpage.master(), self.signinpage.see())
        self.assertNotEqual(note[0], None)
        self.assertNotEqual(note[1], None)
        text = self.signinpage.textArea()
        self.assertNotEqual(text, None)
        passwords = (self.signinpage.password(), self.signinpage.ppassword())
        self.assertNotEqual(passwords[0], None)
        self.assertNotEqual(passwords[1], None)
        self.signinpage.close_driver()
