from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/Admin/PycharmProjects/POMProjectDemo/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
