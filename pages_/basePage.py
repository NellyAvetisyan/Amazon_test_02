from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))
            return element
        except:
            print("ERROR:Element not found or wrong")
            exit(1)

    def _click(self, webElement):
        webElement.click()

    def _fill_field(self,webElement, text):
        webElement.clear()
        webElement.send_keys(text)

    def _get_element_text(self, webElement,):
        webElement.text()

    def _get_title(self):
        return self.driver.title










