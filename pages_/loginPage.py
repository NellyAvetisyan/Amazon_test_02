from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def fill_username_field(self,username):
        # userNameFieldElement = self.driver.find_element(By.ID, "ap_email")
        userNameFieldElement = self._find_element(By.ID, "ap_email")
        self._fill_field(userNameFieldElement, username)
        # userNameFieldElement.clear()
        # userNameFieldElement.send_keys(username)

    def click_to_continue_button(self):
        # continueButton = self.driver.find_element(By.ID, "continue")
        continueButton = self._find_element(By.ID, "continue")
        self._click(continueButton)
        # continueButton.click()

    def fill_password_button(self,password):
        # passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement = self._find_element(By.ID, "ap_password")
        self._fill_field(passwordFieldElement, password)
        # passwordFieldElement.clear()
        # passwordFieldElement.send_keys(password)
        sleep(6)

    def click_signin_button(self):
        # signinButton = self.driver.find_element(By.XPATH, "//input[@id='signInSubmit']")
        signinButton = self._find_element(By.ID, "signInSubmit")
        self._click(signinButton)
        # signinButton.click()
        sleep(6)

