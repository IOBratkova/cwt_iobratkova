from classes.page import Page
from classes.loginmenu import LoginMenu

class LessonsList(Page):
    def __init__(self, d, u):
        super().__init__(d, u)
        self.title = 'LessonsList'
        self.login_menu = LoginMenu(self.driver, self.url)




