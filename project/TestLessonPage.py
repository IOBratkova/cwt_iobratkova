import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from classes.lesson import Lessons


class TestLessonPage(unittest.TestCase):
    def start_up(self):
        self.url = 'http://localhost:8080/#/photolessons/3'
        self.driver = webdriver.Chrome('./chromedriver')
        self.lesson = Lessons(self.driver, self.url)
        self.lesson.open_url()

    def test_title_is_ok(self):
        self.start_up()
        title = self.lesson.value_title()
        self.assertEqual(title, 'Сказка')

    def test_author_is_ok(self):
        self.start_up()
        title = self.lesson.value_author()
        self.assertEqual(title, 'admin')

