from classes.page import Page
from classes.loginmenu import LoginMenu


class Lessons(Page):
    def __init__(self, d, u):
        super().__init__(d, u)
        self.title = 'Lesson'
        self.login_menu = LoginMenu(self.driver, self.url)

    def title(self):
        return self.find_element_by_id('#title')

    def author(self):
        return self.find_element_by_id('#author')

    def category(self):
        return self.find_element_by_id('#categ')

    def info(self):
        return self.find_element_by_id('#info')

    def materials(self):
        return self.find_element_by_id('#materials')

    def image_lesson(self):
        return self.find_element_by_id('#imles')

    def value_imagelesson(self):
        return self.get_text('#imles')

    def value_title(self):
        return self.get_text('#title')

    def value_author(self):
        return self.get_text('#author')

    def value_info(self):
        return self.get_text('#info')

    def value_category(self):
        return self.get_text('#categ')

    def value_materials(self):
        return self.get_text('#materials')