from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver.get('http://betastore.carloudy.com/media/documents/v9onh5o8/appIcon.png')
#driver.get('http://sahitest.com/demo/index.htm')
print(driver.current_window_handle)  # 查看当前window handle
"""
driver.find_element_by_link_text('Window Open Test').click()  # 打开新window1
driver.find_element_by_link_text('Window Open Test With Title').click()  # 打开新window2
print(driver.window_handles) # 查看所有window handles
"""
'''
builder = ActionChains(driver)
builder.key_down(Keys.F12).perform()
'''
'''
#body = driver.find_element_by_tag_name('body')
#body.send_keys(Keys.CONTROL, "t")
menu = driver.find_element_by_id("s-nav")
hidden_submenu = driver.find_element_by_class_name("ib logo")

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()
'''
#driver.refresh()
# 关闭标签页
#ActionChains(driver).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()

text_from_web = driver.find_element_by_id("info").get_attribute("textContent")
print(text_from_web)
#driver.close()
print(driver.window_handles) # 查看现在的所有window handles
