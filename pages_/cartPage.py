from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def delete_first_item(self):
        # firstItemDeleteButton = self.driver.find_element(By.XPATH, "(//input[@value='Delete'])[1]")
        firstItemDeleteButton = self._find_element(By.XPATH, "(//input[@value='Delete'])[1]")
        self._click(firstItemDeleteButton)
        # firstItemDeleteButton.click()


    # def click_to_addtocart_button(self):
    #     addtocartButton = self.driver.find_element(By.ID,"add-to-cart-button")
    #     addtocartButton.click()
# (//div[@class="a-section"])[1]