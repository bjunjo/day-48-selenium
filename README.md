# day-48-selenium
## Lessons: Learning how `Selenium` library works


1. Setup path
```
from selenium import webdriver
chrome_driver_path = "/Users/ByoungjunJo/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
```
2. Extract the upcoming event data from the python.org website.
```
# Use Selenium to scrape all upcoming event dates and names and store them in a nested Python dict.
driver.get("https://www.python.org")

dates = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
dates = [date.text for date in dates]
print(f"Dates: {dates}")
events = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')
events = [event.text for event in events]
print(f"Events: {events}")

dates_and_events = {}
for n in range(len(events)):
    dates_and_events[n] = {
        "time": dates[n],
        "name": events[n]
    }
# Print the dict to the console
# The event data from python.org should be stored under the keys "time" and "name"
print(dates_and_events)
```

3. Close up the window
```
# Close method close a tab
driver.close()
# Quit method close the entire web browser
driver.quit()
```
