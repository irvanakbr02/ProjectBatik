from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://192.168.204.127:5000/login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")

driver.find_element_by_id("submit").click()