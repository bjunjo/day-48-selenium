from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/ByoungjunJo/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("ByoungJun")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Jo")

email = driver.find_element_by_name("email")
email.send_keys("contact@byoungjun.com")

submit = driver.find_element_by_xpath("/html/body/form/button")
submit.send_keys(Keys.ENTER)
