from selenium import webdriver
from classes.signinpage import SignInPage
from classes.page import Page
#
# # driver = webdriver.Chrome('./chromedriver')
# # url_google = 'http://www.google.com'
# # url_yandex = 'https://ya.ru'
# #
# # driver.get(url_yandex)
# # driver.find_element_by_id('text').send_keys('кот')
# # kot = driver.find_element_by_id('text').get_attribute('value')
# #
# # print(kot)
# #
# # ya_page = Page(driver, url_yandex)
# #
# # ya_page.open_url()
# #
# # ya_page.find_element_by_id('text')
# # ya_page.paste_to_element('text', 'кот')
# # text = ya_page.find_element_by_id('text')
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome('./chromedriver')
url = 'http://localhost:8080/#/lessonlist'


from classes.listlessons import LessonsList


ll = LessonsList(driver, url)
ll.open_url()
ll.get_list()
print(ll.miniunits)

ll.click_next()
ll.click_previous()
print(ll.miniunits)
from classes.unit import Unit


def page_3():
    wait_units_3 = [Unit('id', 'Хроники Амбера', 'Прощайте и здравствуйте. Как всегда.'),
                    Unit('id', 'Сказка', 'Сказочное описание урока!')]
    return wait_units_3

ll.click_index(2)
mini_units1 = ll.miniunits
mini_units2 = page_3()


for i in range(8):
    print(mini_units2[i], mini_units1[i], mini_units2[i] == mini_units1[i])


driver.close()