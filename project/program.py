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
url = 'http://127.0.0.1:8080/#/signup'
driver = webdriver.Chrome('./chromedriver')
signinpage = SignInPage(driver, url)
signinpage.open_url()
signinpage.set_login('myNiceLogin')
signinpage.set_email('thisisemail@em.com')
signinpage.set_firstName('Василий')
signinpage.set_lastName('Котиков')
signinpage.set_textarea('Я люблю котиков. Мур!')
signinpage.click_radio_button_master()
signinpage.select_value_to_master(2)
signinpage.set_autocomplete('Б')
signinpage.click_on_autocomplete(3)
signinpage.set_avatar('/home/irina/repo/cwt_iobratkova/bonnie.jpg')
signinpage.set_password('cat')
signinpage.set_ppassword('cat')
signinpage.click_button_submit()
turl =  driver.current_url
signinpage.click_button_submit()
WebDriverWait(signinpage.driver, 5).until(
    lambda kek: signinpage.driver.current_url != turl
)


result = 'lol'
print(result)

