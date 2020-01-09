from selenium.webdriver.support.ui import WebDriverWait


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
        return self.driver.find_element_by_id(id).click()