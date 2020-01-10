from selenium import webdriver
from classes.signinpage import SignInPage
from classes.page import Page

# driver = webdriver.Chrome('./chromedriver')
# url_google = 'http://www.google.com'
# url_yandex = 'https://ya.ru'
#
# driver.get(url_yandex)
# driver.find_element_by_id('text').send_keys('кот')
# kot = driver.find_element_by_id('text').get_attribute('value')
#
# print(kot)
#
# ya_page = Page(driver, url_yandex)
#
# ya_page.open_url()
#
# ya_page.find_element_by_id('text')
# ya_page.paste_to_element('text', 'кот')
# text = ya_page.find_element_by_id('text')
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome('./chromedriver')
url = 'http://localhost:8080/#/photolessons/3'
from classes.lesson import Lessons
lesson = Lessons(driver, url)
lesson.open_url()

var = driver.find_element_by_id('#imles').text

print(var)

# print(result)