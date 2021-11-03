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
        signup_tab = driver.find_elements_by_class_name("opt")[1]

        signup_tab.click()

        signup_name = driver.find_element_by_id("signup_name")
        signup_username = driver.find_element_by_id("signup_username")
        signup_dob = driver.find_element_by_id("dob")
        signup_email = driver.find_element_by_id("signup_email")
        signup_password = driver.find_element_by_id("signup_password")
        signup_password2 = driver.find_element_by_id("signup_password2")

        signup_name.clear()
        signup_name.send_keys("Divyansh Tiwari")

        signup_username.clear()
        signup_username.send_keys("DragoDoom")

        signup_dob.clear()
        signup_dob.send_keys("03042000")

        signup_email.clear()
        signup_email.send_keys("inasumaeleven.gautam8@gmail.com")

        signup_password.clear()
        signup_password.send_keys("Divyansh@03")

        signup_password2.clear()
        signup_password2.send_keys("Divyansh@3")
        #search_bar.send_keys(Keys.RETURN)

        signup_submit = driver.find_element_by_id("signup_submit")
        signup_submit.click()

        # create alert object
        alert = Alert(driver)        
        self.assertEqual("Passwords do not match!", alert.text, "Wrong password error is not raised")
        alert.accept()
        
    def test_wrong_email(self):
        open_chat_app()
        signup_tab = driver.find_elements_by_class_name("opt")[1]

        signup_tab.click()

        signup_name = driver.find_element_by_id("signup_name")
        signup_username = driver.find_element_by_id("signup_username")
        signup_dob = driver.find_element_by_id("dob")
        signup_email = driver.find_element_by_id("signup_email")
        signup_password = driver.find_element_by_id("signup_password")
        signup_password2 = driver.find_element_by_id("signup_password2")

        signup_name.clear()
        signup_name.send_keys("Divyansh Tiwari")

        signup_username.clear()
        signup_username.send_keys("DragoDoom")

        signup_dob.clear()
        signup_dob.send_keys("03042000")

        signup_email.clear()
        signup_email.send_keys("YE EMAIL GALAT HAI")

        signup_password.clear()
        signup_password.send_keys("Divyansh@03")

        signup_password2.clear()
        signup_password2.send_keys("Divyansh@03")
        #search_bar.send_keys(Keys.RETURN)

        signup_submit = driver.find_element_by_id("signup_submit")
        signup_submit.click()

        # create alert object
        alert = Alert(driver)        
        self.assertEqual("Please enter a valid email address", alert.text, "Invalid Email error is not raised")
        alert.accept()

    def test_empty_name(self):
        open_chat_app()
        signup_tab = driver.find_elements_by_class_name("opt")[1]

        signup_tab.click()

        signup_name = driver.find_element_by_id("signup_name")
        signup_username = driver.find_element_by_id("signup_username")
        signup_dob = driver.find_element_by_id("dob")
        signup_email = driver.find_element_by_id("signup_email")
        signup_password = driver.find_element_by_id("signup_password")
        signup_password2 = driver.find_element_by_id("signup_password2")

        signup_name.clear()
        signup_name.send_keys("")

        signup_username.clear()
        signup_username.send_keys("DragoDoom")

        signup_dob.clear()
        signup_dob.send_keys("03042000")

        signup_email.clear()
        signup_email.send_keys("inasumaeleven.gautam8@gmail.com")

        signup_password.clear()
        signup_password.send_keys("Divyansh@03")

        signup_password2.clear()
        signup_password2.send_keys("Divyansh@03")
        #search_bar.send_keys(Keys.RETURN)

        signup_submit = driver.find_element_by_id("signup_submit")
        signup_submit.click()

        # create alert object
        alert = Alert(driver)        
        self.assertEqual("One or more required fields are empty", alert.text, "Empty Name Field error is not raised")
        alert.accept()

    def test_empty_username(self):
        open_chat_app()
        signup_tab = driver.find_elements_by_class_name("opt")[1]

        signup_tab.click()

        signup_name = driver.find_element_by_id("signup_name")
        signup_username = driver.find_element_by_id("signup_username")
        signup_dob = driver.find_element_by_id("dob")
        signup_email = driver.find_element_by_id("signup_email")
        signup_password = driver.find_element_by_id("signup_password")
        signup_password2 = driver.find_element_by_id("signup_password2")

        signup_name.clear()
        signup_name.send_keys("Divyansh Tiwari")

        signup_username.clear()
        signup_username.send_keys("")

        signup_dob.clear()
        signup_dob.send_keys("03042000")

        signup_email.clear()
        signup_email.send_keys("inasumaeleven.gautam8@gmail.com")

        signup_password.clear()
        signup_password.send_keys("Divyansh@03")

        signup_password2.clear()
        signup_password2.send_keys("Divyansh@03")
        #search_bar.send_keys(Keys.RETURN)

        signup_submit = driver.find_element_by_id("signup_submit")
        signup_submit.click()

        # create alert object
        alert = Alert(driver)        
        self.assertEqual("One or more required fields are empty", alert.text, "Empty username Field error is not raised")
        alert.accept()
        
    def test_empty_email(self):
        open_chat_app()
        signup_tab = driver.find_elements_by_class_name("opt")[1]

        signup_tab.click()

        signup_name = driver.find_element_by_id("signup_name")
        signup_username = driver.find_element_by_id("signup_username")
        signup_dob = driver.find_element_by_id("dob")
        signup_email = driver.find_element_by_id("signup_email")
        signup_password = driver.find_element_by_id("signup_password")
        signup_password2 = driver.find_element_by_id("signup_password2")

        signup_name.clear()
        signup_name.send_keys("Divyansh Tiwari")

        signup_username.clear()
        signup_username.send_keys("DragoDoom")

        signup_dob.clear()
        signup_dob.send_keys("03042000")

        signup_email.clear()
        signup_email.send_keys("")

        signup_password.clear()
        signup_password.send_keys("Divyansh@03")

        signup_password2.clear()
        signup_password2.send_keys("Divyansh@03")
        #search_bar.send_keys(Keys.RETURN)

        signup_submit = driver.find_element_by_id("signup_submit")
        signup_submit.click()

        # create alert object
        alert = Alert(driver)        
        self.assertEqual("One or more required fields are empty", alert.text, "Empty email Field error is not raised")
        alert.accept()
        
    def test_empty_pass(self):
        open_chat_app()
        signup_tab = driver.find_elements_by_class_name("opt")[1]

        signup_tab.click()

        signup_name = driver.find_element_by_id("signup_name")
        signup_username = driver.find_element_by_id("signup_username")
        signup_dob = driver.find_element_by_id("dob")
        signup_email = driver.find_element_by_id("signup_email")
        signup_password = driver.find_element_by_id("signup_password")
        signup_password2 = driver.find_element_by_id("signup_password2")

        signup_name.clear()
        signup_name.send_keys("Divyansh Tiwari")

        signup_username.clear()
        signup_username.send_keys("DragoDoom")

        signup_dob.clear()
        signup_dob.send_keys("03042000")

        signup_email.clear()
        signup_email.send_keys("inasumaeleven.gautam8@gmail.com")

        signup_password.clear()
        signup_password.send_keys("")

        signup_password2.clear()
        signup_password2.send_keys("Divyansh@03")
        #search_bar.send_keys(Keys.RETURN)

        signup_submit = driver.find_element_by_id("signup_submit")
        signup_submit.click()

        # create alert object
        alert = Alert(driver)        
        self.assertEqual("One or more required fields are empty", alert.text, "Empty PAssword Field error is not raised")
        alert.accept()
        
    def test_empty_pass_2(self):
        open_chat_app()
        signup_tab = driver.find_elements_by_class_name("opt")[1]

        signup_tab.click()

        signup_name = driver.find_element_by_id("signup_name")
        signup_username = driver.find_element_by_id("signup_username")
        signup_dob = driver.find_element_by_id("dob")
        signup_email = driver.find_element_by_id("signup_email")
        signup_password = driver.find_element_by_id("signup_password")
        signup_password2 = driver.find_element_by_id("signup_password2")

        signup_name.clear()
        signup_name.send_keys("Divyansh Tiwari")

        signup_username.clear()
        signup_username.send_keys("DragoDoom")

        signup_dob.clear()
        signup_dob.send_keys("03042000")

        signup_email.clear()
        signup_email.send_keys("inasumaeleven.gautam8@gmail.com")

        signup_password.clear()
        signup_password.send_keys("Divyansh@03")

        signup_password2.clear()
        signup_password2.send_keys("")
        #search_bar.send_keys(Keys.RETURN)

        signup_submit = driver.find_element_by_id("signup_submit")
        signup_submit.click()

        # create alert object
        alert = Alert(driver)        
        self.assertEqual("One or more required fields are empty", alert.text, "Empty Confirm Password Field error is not raised")
        alert.accept()

    def test_signup(self):
        open_chat_app()
        signup_tab = driver.find_elements_by_class_name("opt")[1]

        signup_tab.click()

        signup_name = driver.find_element_by_id("signup_name")
        signup_username = driver.find_element_by_id("signup_username")
        signup_dob = driver.find_element_by_id("dob")
        signup_email = driver.find_element_by_id("signup_email")
        signup_password = driver.find_element_by_id("signup_password")
        signup_password2 = driver.find_element_by_id("signup_password2")

        signup_name.clear()
        signup_name.send_keys("Divyansh Tiwari")

        signup_username.clear()
        signup_username.send_keys("Drago-Doom")

        signup_dob.clear()
        signup_dob.send_keys("03042000")

        signup_email.clear()
        signup_email.send_keys("inasumaeleven.gautam9@gmail.com")

        signup_password.clear()
        signup_password.send_keys("Divyansh@03")

        signup_password2.clear()
        signup_password2.send_keys("Divyansh@03")
        #search_bar.send_keys(Keys.RETURN)

        signup_submit = driver.find_element_by_id("signup_submit")
        signup_submit.click()

        WebDriverWait(driver,10).until(expected_conditions.alert_is_present())
        
        # create alert object
        alert = Alert(driver)
        self.assertEqual("Account Successfully Created", alert.text, "Account is not being created")
        ale = driver.switch_to_alert();
        alert.accept()
        ale.accept()

if __name__ == '__main__':
    unittest.main()

