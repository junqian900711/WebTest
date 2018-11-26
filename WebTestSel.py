""""
from selenium import webdriver
#this is the driver for the firefox
browser = webdriver.Firefox()
browser.get('http://betastore.carloudy.com')
browser.maximize_window()
#browser.find_element_by_name()
may not use this next time
"""

from selenium import webdriver

browser = webdriver.Chrome()
#browser = webdriver.Firefox()
browser.get("http://betastore.carloudy.com")
browser.maximize_window()

browser.find_element_by_name("username").send_keys("junqianniub")
browser.find_element_by_name("password").send_keys("1019042603QJ")
browser.find_element_by_xpath("//button[text()='Log in']").click()

#that is for today