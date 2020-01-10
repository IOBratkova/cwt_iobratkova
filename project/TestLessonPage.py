import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from classes.lesson import Lessons


class TestLessonPage(unittest.TestCase):
    def start_up(self):
        self.url = 'http://localhost:8080/#/photolessons/10'
        self.driver = webdriver.Chrome('./chromedriver')
        self.lesson = Lessons(self.driver, self.url)

    def test_lesson(self):
        self.start_up()
        self.lesson.open_url()
