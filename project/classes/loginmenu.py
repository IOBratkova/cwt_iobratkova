from classes.page import Page
import re


class LoginMenu(Page):
    def __init__(self, d, u):
        super().__init__(d, u)
        self.title = 'LoginMenu'

    def sign_in(self):
        return self.find_element_by_id('#signinbutton')

    def login_button(self):
        return self.find_element_by_id('#login_button')

    def user_name(self):
        return self.find_element_by_id('#username')

    def password(self):
        return self.find_element_by_id('#password')

    def click_dropdown_sign_in(self):
        self.click_on_element('#signinbutton')

    def click_login_button(self):
        return self.click_on_element('#login_button') \
            if self.get_error() == [] \
            else self.get_error(), self.click_on_element('#login_button')

    def set_username(self, value):
        return self.paste_to_element('#username', value)

    def set_password(self, value):
        return self.paste_to_element('#password', value)

    def check_login(self):
        return True if bool(re.match('[a-zA-Z]', self.get_attribute_value('#username'))) \
                   else 'Имя пользователя должно состоять только из латинских букв.', '#username'

    def get_error(self):
        flag = []
        if self.get_attribute_value('#username') == '':
            tp = ('Заполните «Имя пользователя»', '#username')
            flag.append(tp)
        elif self.get_attribute_value('#username') != '':
            tp = self.check_login()
            flag.append(tp)
        if self.get_attribute_value('#password') == '':
            tp = ('Проверьте пароль', '#password')
            flag.append(tp)
        return flag