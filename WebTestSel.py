"""
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://betastore.carloudy.com')
browser.maximize_window()
#browser.find_element_by_name()
may not use this next time

https://github.com/intypython/seleniumDemo/commits/newBranch
https://www.zhihu.com/question/19660572
https://github.com/ccapton/brook-web
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
from selenium.webdriver.support.select import Select


#这段代码是用Chrome对网站进行测试
browser = webdriver.Chrome()
#browser = webdriver.Firefox()
browser.implicitly_wait(30)  # 隐性等待，最长等30秒
browser.get("http://betastore.carloudy.com")
browser.maximize_window()

browser.find_element_by_name("username").send_keys("junqianniub")
browser.find_element_by_name("password").send_keys("1019042603QJ")
browser.find_element_by_xpath("//button[text()='Log in']").click()

system_type = Select(browser.find_element_by_xpath("/html//select[@id='inputState']"))
system_type.select_by_value("iOS")
#system_type.select_by_value("Android")
file_path_ios = r'C:\Users\qianj\Desktop\1.png'
browser.find_element_by_name("RegisterAppName").send_keys("Test iOS 1")
uploade_icon = browser.find_element_by_xpath("/html//input[@id='exampleFormControlFile2']")
uploade_icon.send_keys(file_path_ios)
browser.find_element_by_name("RegisterPackageName").send_keys("Test iOS Package Name 1")
browser.find_element_by_name("RegisterAppDescription").send_keys("Test iOS App description 1")
browser.find_element_by_xpath("/html/body//main/div[2]/form[@method='post']//button[@type='submit']").click()

system_type = Select(browser.find_element_by_xpath("/html//select[@id='inputState']"))
system_type.select_by_value("Android")
#system_type.select_by_value("Android")
file_path_Android = r'C:\Users\qianj\Desktop\2.png'
browser.find_element_by_name("RegisterAppName").send_keys("Test Android 1")
uploade_icon = browser.find_element_by_xpath("/html//input[@id='exampleFormControlFile2']")
uploade_icon.send_keys(file_path_Android)
browser.find_element_by_name("RegisterPackageName").send_keys("Test Android Package Name 1")
browser.find_element_by_name("RegisterAppDescription").send_keys("Test Android App description 1")
browser.find_element_by_xpath("/html/body//main/div[2]/form[@method='post']//button[@type='submit']").click()


time.sleep(2)
#browser.close()


# 以下代码是对API 进行测试
"""
https://gist.github.com/lrhache/7686903 from 洪磊
从上述的Chrome 更换到 Firefox 进行API测试，上面的link 是用来
https://my.oschina.net/u/3204996/blog/1796460
"""

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("http://betastore.carloudy.com/approved/?os=android")
url_1 = "http://betastore.carloudy.com/approved/?os=android"
webdata = requests.get(url_1).text
# print("The webdata is {}:".format(webdata))
data_1 = json.loads(webdata)
# print("The data_1 is {}:".format(data_1))
length_data_1 = len(data_1)
# dictionary_1 = [length_data_1+1]
dictionary_1 = []

'''
for i in range(length_data_1):
    #print(data_1[i])
    dictionary_1.append(data_1[i])
'''
for i in range(length_data_1):
    dictionary_1.append(data_1[i]["RegisterAppIcon"])  # 这里不能用dictionary_1[i] = length_data_1[i]这个方法,liso[0]不能用
print(dictionary_1)

for i in range(length_data_1):
    js_1 = 'window.open("' + dictionary_1[i] + '");'
    browser.execute_script(js_1)
    #time.sleep(2)
    r = requests.get(dictionary_1[i])
    #https://www.jianshu.com/p/ada99b7880a6    这是request 的解释
    #print(type(r)) #<class 'requests.models.Response'>
    print("Right now the nummber is {}, and the status code is {}!!!!".format(i,r.status_code))
    if r.status_code == 200:
        print("In the first API, the image I am print now is {}, and the link is {}:".format(i, data_1[i]))
        print("The image load success\n")
        time.sleep(2)
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nThe image didn't load success")
        print("In the first API, the image I am print now is {}, and the link is {}:\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n".format(i, data_1[i]))
        time.sleep(2)

    """
    try - catch的基本使用方法 
    try:
    except Exception as e:
        print(e)
    """

print("first one success")
time.sleep(2)

'''
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
webdata_4 = requests.get("http://betastore.carloudy.com/jsons/?appid=92e4r05x").text
print(webdata_4)
print(type(webdata_4))
#request 自带了json的功能
data = json.loads(webdata_4)
print(data)
print(type(data))
#url_image=data[0]["files"] 的作用与 url_image=data[0].get("files")一样
#json 解析： https://cuiqingcai.com/5564.html
#https://www.cnblogs.com/wzjbg/p/6507497.html   要比较下与方法二之间的区别，方法二是错误的
url_image=data[0].get("files")
print(url_image)
# 此处是对现有的url进行open new page
js_4 = 'window.open("'+ url_image + '");'
browser.execute_script(js_4)
print("js_4 is :",js_4)
print(browser.current_url)

#browser.get(url_image)
#browser.get("http://www.google.com")
#https://www.zhihu.com/ques`tion/43604232
#https://stackoverrun.com/cn/q/13100729
'''

"""
方法二
json_elements = json.dumps(data)
print(json_elements)

diction = json_elements[1:-1]
print("Dictionary is :",diction)
image_url = diction["files"]
print(image_url)
"""


