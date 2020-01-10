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
        self.assertEqual(title, 'Автор: admin')

    def test_category_is_ok(self):
        self.start_up()
        title = self.lesson.value_category()
        self.assertEqual(title, 'Категория: Ловец снов')

    def test_info_is_ok(self):
        self.start_up()
        title = self.lesson.value_info()
        self.assertEqual(title, 'Сказочное описание урока!')

    def test_materials_is_ok(self):
        self.start_up()
        title = self.lesson.value_materials()
        self.assertEqual(title, 'Рассказы А.С. Пушкина, сборник Темный карнавал Рэя Бредбери')

    def test_work_is_ok(self):
        self.start_up()
        title = self.lesson.value_imagelesson()
        result = 'Результат\n' \
                 'Все материалы выкладываем перед собой, как показано в МК.\n' \
                 'Берем деревянное кольцо, круг или обруч, и начинаем его плотно обматывать заготовленными нитками.\n' \
                 'Фиксируем.\n' \
                 'Как только красивый ряд с бусинками из дерева или стекла готов, делаем три обычных ряда.'
        self.assertEqual(title, result)