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

url = 'http://127.0.0.1:8080/#/signup'
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
signinpage = SignInPage(driver, url)
signinpage.open_url()

print(signinpage.master())
signinpage.click_radio_button_master()
print(signinpage.master())
signinpage.select_value_to_master(2)
print('+++++++++++++++++++++++++++++')