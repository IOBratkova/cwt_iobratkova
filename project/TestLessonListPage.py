import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from classes.unit import Unit
from classes.listlessons import LessonsList


class TestLessonListPage(unittest.TestCase):
    def start_up(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.url = 'http://localhost:8080/#/lessonlist'
        self.ll = LessonsList(self.driver, self.url)
        self.ll.open_url()
        WebDriverWait(self.driver, 100).until(
            lambda tmp: self.driver.current_url != self.url
        )

    def page_1(self):
        wait_units_1 = [Unit('id', 'Тестовый урок еще один', 'Ловец снов номер семь на нашем сайте'),
                        Unit('id', 'Тестовый урок еще один', 'Ловец снов номер семь на нашем сайте'),
                        Unit('id', 'И это тоже урок еще один урок', 'Ловец сно на нашем сайте'),
                        Unit('id', 'И это тоже урок', 'Ловец сно на нашем сайте'),
                        Unit('id', 'И это урок', 'И это урок'), Unit('id', 'Снова урок', 'Снова урок'),
                        Unit('id', 'Тестовый урок еще и еше один', 'Тестовый урок еще и еше один'),
                        Unit('id', 'Тестовый урок еще очередной', 'Тестовый урок еще очередной')]
        return  wait_units_1

    def page_2(self):
        wait_units_2 = [Unit('id', 'Тестовый урок еще один', 'Ловец снов номер семь на нашем сайте'),
                        Unit('id', 'Тестовый урок новый', 'Ловец снов номер семь на нашем сайте'),
                        Unit('id', 'Восьмой', 'Ловец снов номер восемь на нашем сайте'),
                        Unit('id', 'Седьмой', 'Ловец снов номер семь на нашем сайте'), Unit('id', 'Паучок', 'Паучок'),
                        Unit('id', 'Совушка', 'Совушка'), Unit('id', 'Как приручить дракона', 'Как приручить дракона'),
                        Unit('id', 'Дом в котором', 'Дом в котором')]
        return wait_units_2

    def page_3(self):
        wait_units_3 = [Unit('id', 'Хроники Амбера', 'Прощайте и здравствуйте. Как всегда.'),
                        Unit('id', 'Сказка', 'Сказочное описание урока!')]
        return wait_units_3

    def test_first_lst(self):
        self.start_up()
        self.ll.get_list()
        true_units = self.page_1()
        mini_units = self.ll.miniunits
        self.assertEqual(mini_units, true_units)
        self.ll.click_next()
        self.ll.click_previous()
        mini_units = self.ll.miniunits
        self.assertEqual(mini_units, true_units)


    def test_second_lst(self):
        self.start_up()
        self.ll.get_list()
        self.ll.click_index(1)
        true_units = self.page_2()
        mini_units = self.ll.miniunits
        self.assertEqual(mini_units, true_units)
        self.ll.click_previous()
        self.ll.click_next()
        mini_units = self.ll.miniunits
        self.assertEqual(mini_units, true_units)

    def test_third_lst(self):
        self.start_up()
        self.ll.get_list()
        self.ll.click_index(2)
        true_units = self.page_3()
        mini_units = self.ll.miniunits
        self.assertEqual(mini_units, true_units)
        self.ll.click_previous()
        self.ll.click_next()
        mini_units = self.ll.miniunits
        self.assertEqual(mini_units, true_units)


if __name__ == "__main__":
    unittest.main()
