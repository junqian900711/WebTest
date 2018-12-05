from selenium import webdriver
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest,time
import logging
from selenium import webdriver

#只要 针对参数 使用 赋值语句，会在 函数内部 修改 局部变量的引用，不会影响到 外部变量的引用
def demo(num, num_list):
    print("函数内部")

    # 赋值语句
    num = 200
    num_list = [1, 2, 3]

    print(num)
    print(num_list)

    print("函数代码完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)

#如果传递的参数是 可变类型，在函数内部，使用 方法 修改了数据的内容，同样会影响到外部的数据
def mutable(num_list):
    # num_list = [1, 2, 3]
    num_list.extend([1, 2, 3])

    print(num_list)

gl_list = [6, 7, 8]
mutable(gl_list)
print(gl_list)
print("~"*20)

def demo(num, num_list):

    print("函数内部代码")

    # num = num + num
    num += num
    # num_list.extend(num_list) 由于是调用方法，所以不会修改变量的引用
    # 函数执行结束后，外部数据同样会发生变化
    num_list += num_list

    print(num)
    print(num_list)
    print("函数代码完成")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
print("~"*20)



def demo(num, *args, **kwargs):

    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)

print("~"*20)


def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "小明", "age": 18}

# 会把 num_tuple 和 xiaoming 作为元组传递个 args
# demo(gl_nums, gl_xiaoming)
demo(*gl_nums, **gl_xiaoming)



'''
driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver.get('http://betastore.carloudy.com/media/')
#driver.get('http://sahitest.com/demo/index.htm')
print(driver.current_window_handle)  # 查看当前window handle
"""
driver.find_element_by_link_text('Window Open Test').click()  # 打开新window1
driver.find_element_by_link_text('Window Open Test With Title').click()  # 打开新window2
print(driver.window_handles) # 查看所有window handles
"""

ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()


#body = driver.find_element_by_tag_name('body')
#body.send_keys(Keys.CONTROL, "t")
menu = driver.find_element_by_id("s-nav")
hidden_submenu = driver.find_element_by_class_name("ib logo")

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()

#driver.refresh()
# 关闭标签页
#ActionChains(driver).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()

text_from_web = driver.find_element_by_id("info").get_attribute("textContent")
#text_from_web = driver.find_elements_by_xpath("//div[@id='info']/p/text()")
print(text_from_web)


#driver.close()
print(driver.window_handles) # 查看现在的所有window handles
'''