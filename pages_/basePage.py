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
            print("ERROR:Element not found")
            exit(1)

    def _click(self, webElement):
        webElement.click()

    def _fill_field(self,webElement, text):
        webElement.clear()
        webElement.send_keys(text)

    def _get_element_text(self, webElement,):
        webElement.get_attribute()

    def _get_title(self):
        return self.driver.title()

    # def _find_element(self, locator):
    #     if self._is_element_visible(locator):
    #         element = self.driver.find_element(*locator)
    #         return element
    #     else:
    #         print("Element is Not found")

    # def _is_element_visible(self, locator):
    #     try:
    #         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #         return True
    #     except:
    #         return False
    #
    # def _element_should_be_visible(self, locator):
    #     try:
    #         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #     except:
    #         print("ERROR: Element is not visible")









