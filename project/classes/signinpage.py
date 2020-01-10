from classes.page import Page
from selenium.webdriver.support.ui import WebDriverWait
import re


class SignInPage(Page):
    def __init__(self, d, u):
        super().__init__(d, u)
        self.title = 'SignIn'

    def login(self):
        return self.find_element_by_id('#login')

    def email(self):
        return self.find_element_by_id('#email')

    def firstName(self):
        return self.find_element_by_id('#firstname')

    def lastName(self):
        return self.find_element_by_id('#lastname')

    def master(self):
        return self.find_element_by_id('#master')

    def see(self):
        return self.find_element_by_id('#see')

    def textArea(self):
        return self.find_element_by_id('#textarea')

    def avatar(self):
        return self.find_element_by_id('#avatar')

    def autocomplete(self):
        return self.find_element_by_id('#autocomplete')

    def select_1(self):
        return self.find_element_by_id('#select_1')

    def select_2(self):
        return self.find_element_by_id('#select_2')

    def password(self):
        return self.find_element_by_id('#password')

    def ppassword(self):
        return self.find_element_by_id('#ppassword')

    def submit(self):
        return self.find_element_by_id('#submit')

    # SET METHODS
    def set_login(self, value):
        return self.paste_to_element('#login', value)

    def set_email(self, value):
        return self.paste_to_element('#email', value)

    def set_firstName(self, value):
        return self.paste_to_element('#firstname', value)

    def set_lastName(self, value):
        return self.paste_to_element('#lastname', value)

    def set_password(self, value):
        return self.paste_to_element('#password', value)

    def set_ppassword(self, value):
        return self.paste_to_element('#ppassword', value)

    def set_autocomplete(self, value):
        return self.paste_to_element('#autocomplete', value)

    def set_avatar(self, value):
        return self.paste_to_element('#avatar', value)

    def set_textarea(self, value):
        return self.paste_to_element('#textarea', value)

    # SELECT METHODS
    def select_value_to_master(self, element):
        element_type = type(element)
        teg = '#select_1'
        if element_type == type('tmp'):
            return self.select_element_by_visible_text(teg, element)
        else:
            return self.select_element_by_index(teg, element)

    def select_value_to_see(self, element):
        element_type = type(element)
        teg = '#select_2'
        if element_type == type('tmp'):
            return self.select_element_by_visible_text(teg, element)
        else:
            return self.select_element_by_index(teg, element)

    # CLICK METHODS
    def click_radio_button_master(self):
        self.click_on_element('#master')

    def click_radio_button_see(self):
        self.click_on_element('#see')

    def click_on_select_1(self):
        self.click_on_element('#select_2')

    def click_on_select_2(self):
        self.click_on_element('#select_2')

    def click_button_submit(self):
        return self.click_on_element('#submit') if self.get_error() else self.get_error()

    def click_on_autocomplete(self, index):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda kek: self.driver.find_element_by_xpath(
                    '//*[@id="list-14"]/div[@aria-labelledby="list-item-20-' + str(index) + '"]')
            )
            self.driver.find_element_by_xpath(
                '//*[@id="list-14"]/div[@aria-labelledby="list-item-20-' + str(index) + '"]').click()
        except Exception:
            WebDriverWait(self.driver, 10).until(
                lambda kek: self.driver.find_element_by_xpath(
                    '//*[@id="list-19"]/div[@aria-labelledby="list-item-25-' + str(index) + '"]')
            )
            self.driver.find_element_by_xpath(
                '//*[@id="list-19"]/div[@aria-labelledby="list-item-25-' + str(index) + '"]').click()

    def check_login(self):
        return True if bool(re.match('[a-zA-Z]', self.get_attribute_value('#login'))) \
                   else 'Введите данные в указанном формате.', '#login'

    def check_email(self):
        return True if bool(re.match('[a-zA-Z]@[a-zA-Z].[a-zA-Z]', self.get_attribute_value('#email'))) \
                   else 'Введите данные в указанном формате.', '#email '

    def check_password(self):
        return True if bool(re.match('[a-zA-Z]', self.get_attribute_value('#password'))) \
                   else 'Введите данные в указанном формате.', '#password'

    def get_error(self):
        if self.get_attribute_value('#login') == '':
            return 'Заполните это поле.', '#login'
        elif self.get_attribute_value('#login') != '':
            return self.check_login()
        elif self.get_attribute_value('#email') == '':
            return 'Заполните это поле.', '#email'
        elif self.get_attribute_value('#email') != '':
            return self.check_email()
        elif self.get_attribute_value('#lastname') == '':
            return 'Заполните это поле.', '#lastname'
        elif self.get_attribute_value('#firstname') == '':
            return 'Заполните это поле.', '#firstname'
        elif self.get_attribute_value('#avatar') == '':
            return 'Заполните это поле.', '#avatar'
        elif self.get_attribute_value('#password') == '':
            return 'Заполните это поле.', '#password'
        elif self.get_attribute_value('#password') != '':
            self.check_password()
        elif self.get_attribute_value('#ppassword') == '':
            return 'Заполните это поле.', '#ppassword'
        elif self.get_attribute_value('#ppassword') != self.get_attribute_value('#password'):
            return 'Пароли не совпадают.', '#ppassword'
        else:
            return True
