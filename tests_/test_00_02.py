from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from time import sleep
# from selenium.webdriver.common.by import By
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage
from pages_.searchFieldElement import SearchFieldElement
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

loginPageObj = LoginPage(driver)
loginPageObj.fill_username_field("Nellikoko91@gmail.com")
loginPageObj.click_to_continue_button()
loginPageObj.fill_password_button("Korea2022")
loginPageObj.click_signin_button()

navigationBarObj = NavigationBar(driver)
navigationBarObj.click_to_navigation_bar()

cartPageObj = CartPage(driver)
cartPageObj.delete_first_item()

# navigationBarObj.click_to_logo_bar()
# navigationBarObj.click_to_customersmostloved_field()
#
#
# searchFieldElementObj = SearchFieldElement(driver)
# searchFieldElementObj.fill_search_field("candle")
# searchFieldElementObj.click_to_search_submit_button()
# searchFieldElementObj.click_to_first_item()
#
# cartPageObj.click_to_addtocart_button()
#
sleep(10)
driver.close()