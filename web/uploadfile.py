from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://syncnau.poltektegal.ac.id/login")
driver.find_element_by_name("username").send_keys("19090010")
driver.find_element_by_name("password").send_keys("arif123")
driver.find_element_by_id("submit").click()
driver.find_element_by_class_name("user-image").click()
driver.find_element_by_link_text("Profil").click()
driver.find_element_by_name("user_foto").send_keys("C:/Users/am271/Documents/iya/daun.jpg")
driver.find_element_by_css_selector("button.btn.btn-success").click()