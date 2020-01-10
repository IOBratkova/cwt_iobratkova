from selenium.webdriver.support.ui import WebDriverWait, Select


class Page:
    def __init__(self, d, u):
        self.driver = d
        self.url = u

    def open_url(self):
        self.driver.get(self.url)

    def close_driver(self):
        self.driver.close()

    def find_element_by_id(self, id):
        return WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element_by_id(id))

    def paste_to_element(self, id, value):
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element_by_id(id))
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys(value)

    def click_on_element(self, id):
        WebDriverWait(self.driver, 5).until(
            lambda driver: self.driver.find_element_by_id(id))
        self.driver.find_element_by_id(id).click()

    def select_element_by_index(self, id, index):
        http_element = self.driver.find_element_by_id(id)
        drp = Select(http_element)
        drp.select_by_index(index)
        return drp

    def select_element_by_visible_text(self, id, text):
        http_element = self.driver.find_element_by_id(id)
        drp = Select(http_element)
        drp.select_by_visible_text(text)
        return drp

    def find_my_element_by_xpath(self, xpath):
        return WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element_by_xpath(xpath))

    def click_element_by_xpath(self, xpath):
        WebDriverWait(self.driver, 5).until(
            lambda driver: self.driver.find_element_by_xpath(xpath))
        self.driver.find_element_by_xpath(xpath).click()

    def get_attribute_value(self, id):
        return self.driver.find_element_by_id(id).get_attribute('value')