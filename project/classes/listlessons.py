from classes.page import Page
from classes.unit import Unit


class LessonsList(Page):
    def __init__(self, d, u):
        super().__init__(d, u)
        self.title = 'LessonsList'
        self.miniunits = []
        # self.get_list()

    def my_lessons(self):
        return self.find_element_by_id('my_lessons')

    def lessons_line_1(self):
        return self.find_element_by_id('lessons_line_1')

    def lessons_line_2(self):
        return self.find_element_by_id('lessons_line_2')

    def get_list(self):
        self.miniunits = []
        res = self.find_elements_by_class_name('mini-unit')
        for r in res:
            result = r.text.splitlines()
            unit = Unit('id', result[0], result[1])
            self.miniunits.append(unit)
        return res

    def click_next(self):
        self.click_on_element('next')
        self.get_list()

    def click_previous(self):
        self.click_on_element('previous')
        self.get_list()

    def click_index(self, index):
        self.click_on_element(str(index))
        self.get_list()
