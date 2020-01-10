import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from classes.loginmenu import LoginMenu


class TestLoginMenuPage(unittest.TestCase):
    def start_up(self):
        self.url = 'http://127.0.0.1:8080/#/'
        self.driver = webdriver.Chrome('./chromedriver')
        self.lm = LoginMenu(self.driver, self.url)

    def wait_update(self, oru_user):
        WebDriverWait(self.lm.driver, 5).until(
            lambda tmp: self.driver.find_element_by_id('user-name').text == oru_user
        )

    def test_should_not_log_in(self):
        self.start_up()
        self.lm.open_url()
        self.lm.click_dropdown_sign_in()
        result = self.lm.click_login_button()
        wait_result = ([('Заполните «Имя пользователя»', '#username'), ('Проверьте пароль', '#password')], None)
        self.assertEqual(result, wait_result)

    def test_should_be_returned_invalid_username(self):
        self.start_up()
        self.lm.open_url()
        self.lm.click_dropdown_sign_in()
        self.lm.set_username('сильвана')
        result = self.lm.click_login_button()
        wait_result = ([('Имя пользователя должно состоять только из латинских букв.', '#username'), ('Проверьте пароль', '#password')], None)
        self.assertEqual(result, wait_result)

    def test_should_be_returned_invalid_password(self):
        self.start_up()
        self.lm.open_url()
        self.lm.click_dropdown_sign_in()
        self.lm.set_username('marry')
        result = self.lm.click_login_button()
        wait_result = ([(True, '#username'), ('Проверьте пароль', '#password')], None)
        self.assertEqual(result, wait_result)

    def test_should_be_log_in(self):
        self.start_up()
        self.lm.open_url()
        self.lm.click_dropdown_sign_in()
        self.lm.set_username('pwd')
        self.lm.set_password('pwd')
        our_user = 'Привет, pwd!' # запоминаем юзеа
        result = self.lm.click_login_button() # кнопкожмяк
        self.wait_update(our_user)
        user = self.driver.find_element_by_id('user-name').text
        self.assertEqual(user, our_user)
