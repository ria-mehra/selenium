from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\Admin\PycharmProjects\FirstSeleniumTest\drivers\chromedriver.exe")

driver.set_page_load_timeout(100)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()
