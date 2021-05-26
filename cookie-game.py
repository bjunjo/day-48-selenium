from selenium import webdriver
from selenium.webdriver.common.keys import Keys
i = 0

# TODO: Create a bot using Selenium and Python to click on the cookie as fast as possible.
chrome_driver_path = "/Users/ByoungjunJo/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Click the cookie
cookie = driver.find_element_by_id('bigCookie')

while True:
    cookie.click()
    all_cookies = driver.find_element_by_xpath('//*[@id="cookies"]')
    all_cookies = all_cookies.text
    all_cookies = all_cookies.split()
    num_of_cookies = float(all_cookies[0])
    cookies_per_sec = float(all_cookies[-1])
    print(all_cookies)
    print(f"Num of Cookies: {num_of_cookies}")
    print(f"Cookies per second: {cookies_per_sec}")
    all_upgrades = driver.find_element_by_css_selector("#upgrades")
    print(all_upgrades.text)
    # i += 1

# TODO: Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive one.
#  You'll need to check how much money (cookies) you have against the price of each upgrade.

all_prices = driver.find_elements_by_class_name("price")
all_prices = [float(price.text) for price in all_prices if price.text != '']
print(max(all_prices))
# TODO: After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second". e.g. this is mine: