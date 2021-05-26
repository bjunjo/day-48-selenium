import threading
import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# TODO: Create a bot using Selenium and Python to click on the cookie as fast as possible.
chrome_driver_path = "/Users/ByoungjunJo/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Click the cookie
cookie = driver.find_element_by_id('cookie')
timeout = time.time() + 5

while True:
    cookie.click()
    if time.time() > timeout:
        all_cookies = driver.find_element_by_id('money')
        all_cookies = all_cookies.text
        all_cookies = all_cookies.split()
        print(all_cookies)
        num_of_cookies = float(all_cookies[0].replace(',',''))
        cookies_per_sec = float(all_cookies[-1])
        print(f"Num of Cookies: {num_of_cookies}")
        print(f"Cookies per second: {cookies_per_sec}")
        # all_upgrades = driver.find_element_by_css_selector("#upgrades")
        # print(all_upgrades.text)
        # i += 1

        # TODO: Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive one.
        #  You'll need to check how much money (cookies) you have against the price of each upgrade.
        all_prices = driver.find_elements_by_class_name("price")
        upgrade_ids = [price.get_attribute("id") for price in all_prices]
        # print(f"\nUpgrade IDs: {upgrade_ids}")
        all_prices = [price.text for price in all_prices if price.text != '']
        all_prices = [float(price.replace(',', '')) for price in all_prices]
        max_upgrade_price = max(all_prices)
        print(f"Upgrade Prices: {all_prices}")

        available_upgrades = dict(zip(all_prices, upgrade_ids))
        print(f"Available Upgrades: {available_upgrades}")
        # print(f"Max Price: {max_upgrade_price}")
        affordable_upgrades = {}
        for cost, id in available_upgrades.items():
            if num_of_cookies > cost:
                affordable_upgrades[cost] = id
        print(f"Affordable Upgrades: {affordable_upgrades}")
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(f"Max Affordable: {highest_price_affordable_upgrade}")
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        print(f"Purchase ID: {to_purchase_id}")
        driver.find_element_by_id(to_purchase_id).click()

        # If I can afford any of the first (max) upgrade, then click that
        # for price in reversed(all_prices):
        #     if num_of_cookies > price:
        #         print(f"You can upgrade {available_upgrade[price]} at {price}")
        #         driver.find_element_by_xpath(f'//*[@id="{available_upgrade[price]}"]').click()

        timeout = time.time() + 5


# TODO: After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second". e.g. this is mine: