import unittest
from classes.page import Page
from selenium import webdriver
from classes.loginmenu import LoginMenu



class TestLoginMenuPage(unittest.TestCase):
    def start_up(self):
        self.url = 'http://127.0.0.1:8080/#/'
        self.driver = webdriver.Chrome('./chromedriver')
        self.lm = LoginMenu(self.driver, self.url)

    def test_should_not_log_in(self):
        self.start_up()
        self.lm.open_url()
        self.lm.click_dropdown_sign_in()
        result = self.lm.click_login_button()
        awaitresult = ([('Заполните «Имя пользователя»', '#username'), ('Проверьте пароль', '#password')], None)
        self.assertEqual(result, awaitresult)
