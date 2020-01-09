from selenium import webdriver
from classes.page import Page

driver = webdriver.Chrome('./chromedriver')
url_google = 'http://www.google.com'
url_yandex = 'https://ya.ru'

ya_page = Page(driver, url_yandex)

ya_page.open_url()

ya_page.find_element_by_id('text')
ya_page.paste_to_element('text', 'кот')