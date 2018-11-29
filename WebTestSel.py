"""
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://betastore.carloudy.com')
browser.maximize_window()

#browser.find_element_by_name()

may not use this next time
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json


#这段代码是用Chrome对网站进行测试
browser = webdriver.Chrome()
#browser = webdriver.Firefox()
browser.get("http://betastore.carloudy.com")
browser.maximize_window()

browser.find_element_by_name("username").send_keys("junqianniub")
browser.find_element_by_name("password").send_keys("1019042603QJ")
browser.find_element_by_xpath("//button[text()='Log in']").click()

print(browser.current_window_handle)

time.sleep(5)
browser.close()



#一下代码是对API 进行测试
"""
https://gist.github.com/lrhache/7686903 from 洪磊
从上述的Chrome 更换到 Firefox 进行API测试，上面的link 是用来
https://my.oschina.net/u/3204996/blog/1796460
"""
browser = webdriver.Firefox()
browser.maximize_window()
browser.get("http://betastore.carloudy.com/approved/?os=android")
print("first one success")
time.sleep(2)

js='window.open("http://betastore.carloudy.com/approved/?os=ios");'
browser.execute_script(js)
time.sleep(2)
print("second one success")

js='window.open("http://betastore.carloudy.com/appinfo/?appid=92e4r05x");'
browser.execute_script(js)
time.sleep(2)
print("third one success")


js='window.open("http://betastore.carloudy.com/jsons/?appid=92e4r05x");'
browser.execute_script(js)
time.sleep(2)
print("forth one success")

#for link in browser.find_elements_by_tag_name("a"): 这一段还没有很明白
   # if link.text!="":
   #     print(link.text + "")
   # else:
   #     print("Not named: ")
   # print(link.get_attribute("http"))
#print(browser.find_element_by_tag_name("a"))
wedata = requests.get("http://betastore.carloudy.com/jsons/?appid=92e4r05x").text
print(wedata)
#request 自带了json的功能
data = json.loads(wedata)
print(data)
print(type(data))
#url_image=data[0]["files"] 的作用与 url_image=data[0].get("files")一样
#json 解析： https://cuiqingcai.com/5564.html
#https://www.cnblogs.com/wzjbg/p/6507497.html   要比较下与方法二之间的区别，方法二是错误的
url_image=data[0].get("files")
print(url_image)

browser.find_element_by_id("json-tab").click()

#browser.get(url_image)
#browser.get("http://www.google.com")
#https://www.zhihu.com/question/43604232
#https://stackoverrun.com/cn/q/13100729
browser.get('https://www.baidu.com/')
element = browser.find_element_by_id('su')
element.send_keys(Keys.CONTROL,"T")


url = "http://www.baidu.com"
js_1 = 'window.open("'+ url + '");'
browser.execute_script(js_1)
print("js_1 is :",js_1)

"""
方法二
json_elements = json.dumps(data)
print(json_elements)

diction = json_elements[1:-1]
print("Dictionary is :",diction)
image_url = diction["files"]
print(image_url)
"""











