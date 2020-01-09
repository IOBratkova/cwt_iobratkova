import unittest
from classes.page import Page
from selenium import webdriver


class TestPage(unittest.TestCase):
    def test_init(self):
        page = Page(3, 4)
        self.assertNotEqual(page.driver, 10)
        self.assertNotEqual(page.url, 10)
