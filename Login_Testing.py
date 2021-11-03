import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome('./chromedriver')

def open_chat_app():
    driver.get("http://localhost/chat/")
    driver.implicitly_wait(20)

class Test(unittest.TestCase):
    def test_title(self):
        open_chat_app()
        self.assertEqual("Chat", driver.title, "Correct web page is not opened")
        
    def test_different_password(self):
        open_chat_app()

        signin_username = driver.find_element_by_id("signin_username")
        signin_password = driver.find_element_by_id("signin_password")

        signin_username.clear()
        signin_username.send_keys("Drago-Doom")

        signin_password.clear()
        signin_password.send_keys("Divyansh@0345")
        #search_bar.send_keys(Keys.RETURN)

        signup_submit = driver.find_element_by_id("login_submit")
        signup_submit.click()

        WebDriverWait(driver,10).until(expected_conditions.alert_is_present())

        # create alert object
        alert = Alert(driver)        
        self.assertEqual("Invalid Login Credentials", alert.text, "Wrong creds error is not raised")
        alert.accept()
        
    def test_wrong_username(self):
        open_chat_app()

        signin_username = driver.find_element_by_id("signin_username")
        signin_password = driver.find_element_by_id("signin_password")

        signin_username.clear()
        signin_username.send_keys("DragDoom")

        signin_password.clear()
        signin_password.send_keys("Divyansh@0345")
        #search_bar.send_keys(Keys.RETURN)

        signup_submit = driver.find_element_by_id("login_submit")
        signup_submit.click()

        WebDriverWait(driver,10).until(expected_conditions.alert_is_present())

        # create alert object
        alert = Alert(driver)        
        self.assertEqual("Invalid Login Credentials", alert.text, "Wrong creds error is not raised")
        alert.accept()

if __name__ == '__main__':
    unittest.main()

