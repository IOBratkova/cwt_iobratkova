import unittest
from classes.signinpage import SignInPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class TestSignUpPage(unittest.TestCase):
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
        # self.signinpage.close_driver()

    def test_find_visible_elements(self):
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
        complete = self.signinpage.autocomplete()
        self.assertNotEqual(complete, None)
        submit = self.signinpage.submit()
        self.assertNotEqual(submit, None)
        avatar = self.signinpage.avatar()
        self.assertNotEqual(avatar, None)

    def test_find_invisible_elements(self):
        self.start_up()
        self.signinpage.open_url()
        self.signinpage.click_radio_button_master()
        select_master = self.signinpage.master()
        self.assertNotEqual(select_master, None)
        self.signinpage.click_radio_button_see()
        select_see = self.signinpage.see()
        self.assertNotEqual(select_see, None)

    def test_set_information(self):
        self.start_up()
        self.signinpage.open_url()

        self.signinpage.set_login('_boNni1e')
        a = self.signinpage.login().get_attribute('value')
        b = self.driver.find_element_by_id('#login').get_attribute('value')
        self.assertEqual(a, b)

        self.signinpage.set_email('bonnie_parker@ya.ru')
        a = self.signinpage.email().get_attribute('value')
        b = self.driver.find_element_by_id('#email').get_attribute('value')
        self.assertEqual(a, b)

        self.signinpage.set_firstName('Бонни')
        self.signinpage.set_lastName('Паркер')
        a = (self.signinpage.firstName().get_attribute('value'),
             self.signinpage.lastName().get_attribute('value'))
        b = (self.driver.find_element_by_id('#firstname').get_attribute('value'),
             self.driver.find_element_by_id('#lastname').get_attribute('value'))
        self.assertEqual(a, b)

        self.signinpage.set_password('klayd')
        self.signinpage.set_ppassword('klayd')
        a = (self.signinpage.password().get_attribute('value'),
             self.signinpage.ppassword().get_attribute('value'))
        b = (self.driver.find_element_by_id('#password').get_attribute('value'),
             self.driver.find_element_by_id('#ppassword').get_attribute('value'))
        self.assertEqual(a, b)

        self.signinpage.set_autocomplete('Нара')
        a = self.signinpage.autocomplete().get_attribute('value')
        b = self.driver.find_element_by_id('#autocomplete').get_attribute('value')
        self.assertEqual(a, b)

        self.signinpage.set_avatar('/home/irina/repo/cwt_iobratkova')
        a = self.signinpage.avatar().get_attribute('value')
        b = self.driver.find_element_by_id('#avatar').get_attribute('value')
        self.assertEqual(a, b)

        self.signinpage.set_textarea('Нынче Бонни и Клайд - знаменитый дуэт,\n'
                                     'Все газеты о них трубят.\n'
                                     'После их "работы" свидетелей нет,\n'
                                     'Остается лишь смерти смрад.\n')
        a = self.signinpage.textArea().get_attribute('value')
        b = self.driver.find_element_by_id('#textarea').get_attribute('value')
        self.assertEqual(a, b)

        self.signinpage.click_radio_button_master()
        self.signinpage.select_value_to_master('Бог')
        a = self.signinpage.master().get_attribute('value')
        b = self.driver.find_element_by_id('#master').get_attribute('value')
        self.assertEqual(a, b)

        # self.signinpage.click_radio_button_see()
        # self.signinpage.select_value_to_see(0)
        # a = self.signinpage.master().get_attribute('value')
        # b = self.driver.find_element_by_id('#see').get_attribute('value')
        # self.assertEqual(a, b)