"""
https://github.com/intypython/seleniumDemo/commits/newBranch
https://www.zhihu.com/question/19660572
https://github.com/ccapton/brook-web
https://www.zhihu.com/question/20039623/answer/167106822
https://zhuanlan.zhihu.com/p/28587931
https://www.boxuegu.com/course/free/    13861712384
https://ke.qq.com/course/134017
"""
###
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
from selenium.webdriver.support.select import Select
import os
import os.path
from selenium.webdriver.common.alert import Alert

# 这段代码是用Chrome对网站进行测试
browser = webdriver.Chrome()
#browser = webdriver.Firefox()
browser.implicitly_wait(30)  # 隐性等待，最长等30秒
browser.get("http://betastore.carloudy.com")
browser.maximize_window()

browser.find_element_by_name("username").send_keys("junqianniub")
browser.find_element_by_name("password").send_keys("1019042603QJ")
time.sleep(2)
browser.find_element_by_xpath("//button[text()='Log in']").click()
print("Test1 --- Log in Successfully")
print("*" *50)
time.sleep(2)

system_type = Select(browser.find_element_by_xpath("/html//select[@id='inputState']"))
system_type.select_by_value("iOS")
# system_type.select_by_value("Android")
#file_path_ios = r'C:/Users\qianj\Desktop\1.png'
file_path_ios = os.path.realpath('WebTest/image/1.png') #link for OS 操作: https://blog.csdn.net/xiongchengluo1129/article/details/79181246
#print(file_path_ios)
browser.find_element_by_name("RegisterAppName").send_keys("Test iOS 1")
time.sleep(2)
uploade_icon_ios_path = browser.find_element_by_xpath("/html//input[@id='exampleFormControlFile2']")
time.sleep(2)
uploade_icon_ios_path.send_keys(file_path_ios)
time.sleep(2)
browser.find_element_by_name("RegisterPackageName").send_keys("Test iOS Package Name 1")
time.sleep(2)
browser.find_element_by_name("RegisterAppDescription").send_keys("Test iOS App description 1")
time.sleep(2)
browser.find_element_by_xpath("/html/body//main/div[2]/form[@method='post']//button[@type='submit']").click()
time.sleep(3)
print("Test2 --- Create iOS app successfully")
print("*" *50)
time.sleep(2)

#测试如果同样的app name 注册两次会出现一个alert，测试出现并点击接受
system_type = Select(browser.find_element_by_xpath("/html//select[@id='inputState']"))
system_type.select_by_value("iOS")
file_path_ios = os.path.realpath('WebTest/image/1.png') #link for OS 操作: https://blog.csdn.net/xiongchengluo1129/article/details/79181246
#print(file_path_ios)
browser.find_element_by_name("RegisterAppName").send_keys("Test iOS 1")
uploade_icon_ios_path = browser.find_element_by_xpath("/html//input[@id='exampleFormControlFile2']")
uploade_icon_ios_path.send_keys(file_path_ios)
browser.find_element_by_name("RegisterPackageName").send_keys("Test iOS Package Name 1")
browser.find_element_by_name("RegisterAppDescription").send_keys("Test iOS App description 1")
time.sleep(2)
browser.find_element_by_xpath("/html/body//main/div[2]/form[@method='post']//button[@type='submit']").click()
time.sleep(3)
Alert(browser).accept()
print("Test3 --- Same app name test pass")
print("*" *50)
time.sleep(2)

system_type = Select(browser.find_element_by_xpath("/html//select[@id='inputState']"))
system_type.select_by_value("Android")
#system_type.select_by_value("Android")
#file_path_Android = r'C:/Users\qianj\Desktop\2.png' #https://blog.csdn.net/caibaoH/article/details/78335094  uncommon 之后要把/改成\才能继续使用，为了能够成功uncommon
file_path_Android = os.path.realpath('WebTest/image/2.png')
browser.find_element_by_name("RegisterAppName").send_keys("Test Android 1")
uploade_icon_Android_path = browser.find_element_by_xpath("/html//input[@id='exampleFormControlFile2']")
uploade_icon_Android_path.send_keys(file_path_Android)
browser.find_element_by_name("RegisterPackageName").send_keys("Test Android Package Name 1")
browser.find_element_by_name("RegisterAppDescription").send_keys("Test Android App description 1")
time.sleep(2)
browser.find_element_by_xpath("/html/body//main/div[2]/form[@method='post']//button[@type='submit']").click()
time.sleep(3)
print("Test4 --- Create Android App")
print("*" *50)


#与第一个ios app 做对比，除了系统不一样，其他一样，上传成功，对比测试
system_type = Select(browser.find_element_by_xpath("/html//select[@id='inputState']"))
system_type.select_by_value("Android")
# system_type.select_by_value("Android")
#file_path_ios = r'C:/Users\qianj\Desktop\1.png'
file_path_ios = os.path.realpath('WebTest/image/1.png') #link for OS 操作: https://blog.csdn.net/xiongchengluo1129/article/details/79181246
#print(file_path_ios)
browser.find_element_by_name("RegisterAppName").send_keys("Test iOS 1")
uploade_icon_ios_path = browser.find_element_by_xpath("/html//input[@id='exampleFormControlFile2']")
uploade_icon_ios_path.send_keys(file_path_ios)
browser.find_element_by_name("RegisterPackageName").send_keys("Test iOS Package Name 1")
browser.find_element_by_name("RegisterAppDescription").send_keys("Test iOS App description 1")
time.sleep(2)
browser.find_element_by_xpath("/html/body//main/div[2]/form[@method='post']//button[@type='submit']").click()
print("Test5 --- Compare Test Pass")
print("*" *50)
time.sleep(3)

#image using jpg
file_path_jpg = os.path.realpath('WebTest/image/3.jpg')
uploade_icon_jpg = browser.find_element_by_xpath("/html//input[@id='exampleFormControlFile2']")
time.sleep(2)
uploade_icon_jpg.send_keys(file_path_jpg)
time.sleep(2)
#下面两种Alert的使用方法，分别是：
#https://huilansame.github.io/huilansame.github.io/archivers/switch-to-alert-window-div
#https://blog.csdn.net/chenjuan0530/article/details/79553157
#browser.switch_to.alert.accept()
Alert(browser).accept()
time.sleep(2)
print("Test6 --- Test Using jpg file")
print("*" *50)

#image over 50KB
file_path_over = os.path.realpath('WebTest/image/over50.png')
uploade_icon_over50 = browser.find_element_by_xpath("/html//input[@id='exampleFormControlFile2']")
time.sleep(2)
uploade_icon_over50.send_keys(file_path_over)
time.sleep(2)
browser.switch_to.alert.accept()
time.sleep(2)
print("Test7 --- Test Using image over 50k")
print("*" *50)

# 测试点击edit 然后back 功能,再forward 并且测试cancel的功能
browser.find_element_by_xpath("/html/body//main/div[1]/table[@class='table table-striped']/tbody/tr[4]/td[7]/form[@action='/editappinfo']//button[@name='editappinfo']").click()
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)
browser.find_element_by_xpath("/html/body//div[@role='alert']/form[@action='/updateedit']/div/div[6]/button[1]").click() #cancel
print("Test8 --- Test edit; back; forward; cancel successfully ")
print("*" *50)
time.sleep(2)

#再次点击目的更换图片并且完成更新功能,并且系统从iOS改成了Android
browser.find_element_by_xpath("/html/body//main/div[1]/table[@class='table table-striped']/tbody/tr[4]/td[7]/form[@action='/editappinfo']//button[@name='editappinfo']").click()#click edit
system_type_update_1 = Select(browser.find_element_by_name("OperatingSystem")) #choose operation system
system_type_update_1.select_by_value("Android") #select
uploade_icon_update_path_1 = browser.find_element_by_xpath("//input[@id='exampleFormControlFile4']") #select the image
file_path_update_1 = os.path.realpath('WebTest/image/4.png')
uploade_icon_update_path_1.send_keys(file_path_update_1) #upload image
browser.find_element_by_name("RegisterAppName").clear()  #对之前的文本清理以及输入新的文本
browser.find_element_by_name("RegisterAppName").send_keys("iOS Transfer to Test Android 1")
browser.find_element_by_name("RegisterPackageName").clear()
browser.find_element_by_name("RegisterPackageName").send_keys("iOS to Android Test1")
browser.find_element_by_name("RegisterAppDescription").clear()
browser.find_element_by_name("RegisterAppDescription").send_keys("iOS to Android Test1 description 1")
time.sleep(8)
browser.find_element_by_xpath("/html/body//div[@role='alert']/form[@action='/updateedit']/div/div[6]/button[2]").click()
print("Test9 --- Test image change and transfer from ios to android ")
print("*" *50)
time.sleep(2)
#browser.find_element_by_name("updateedit").click()

#Android update transfer to iOS
browser.find_element_by_xpath("/html/body//main/div[1]/table[@class='table table-striped']/tbody/tr[5]/td[7]/form[@action='/editappinfo']//button[@name='editappinfo']").click()
system_type_update_2 = Select(browser.find_element_by_name("OperatingSystem"))
system_type_update_2.select_by_value("iOS")
uploade_icon_update_path_2 = browser.find_element_by_xpath("/html//input[@id='exampleFormControlFile4']")
file_path_update_2 = os.path.realpath('WebTest/image/5.png')
uploade_icon_update_path_2.send_keys(file_path_update_2)
browser.find_element_by_name("RegisterAppName").clear()  #对之前的文本清理以及输入新的文本
browser.find_element_by_name("RegisterAppName").send_keys("Android Transfer to Test iOS 1")
browser.find_element_by_name("RegisterPackageName").clear()
browser.find_element_by_name("RegisterPackageName").send_keys("Android to iOS Test1")
browser.find_element_by_name("RegisterAppDescription").clear()
browser.find_element_by_name("RegisterAppDescription").send_keys("Android to iOS Test1 description 1")
time.sleep(8)
browser.find_element_by_xpath("/html/body//div[@role='alert']/form[@action='/updateedit']/div/div[6]/button[2]").click()
print("Test10 --- Test image change and transfer from Android  to ios ")
print("*" *50)
time.sleep(2)

#删除之前注册的iOS 和 Android App,需要注意的是location
browser.find_element_by_xpath("/html/body//main/div[1]/table[@class='table table-striped']/tbody/tr[4]/td[8]/form[@action='/deleteapp']//button[@name='deletebutton']").click()
#time.sleep(5)
Alert(browser).dismiss()
time.sleep(2)
browser.find_element_by_xpath("/html/body//main/div[1]/table[@class='table table-striped']/tbody/tr[4]/td[8]/form[@action='/deleteapp']//button[@name='deletebutton']").click()
time.sleep(5)
browser.switch_to.alert.accept()
print("Test11 --- Delete success")
time.sleep(2)
print("*" *50)

#browser.find_element_by_xpath("/html/body//main/div[1]/table[@class='table table-striped']/tbody/tr[5]/td[8]/form[@action='/deleteapp']//button[@name='deletebutton']").click()   注意此处的以及与下一行的区别
browser.find_element_by_xpath("/html/body//main/div[1]/table[@class='table table-striped']/tbody/tr[4]/td[8]/form[@action='/deleteapp']//button[@name='deletebutton']").click()
Alert(browser).accept()
print("Test12 --- Second delete success")
time.sleep(5)
print("*" *50)

browser.find_element_by_xpath("/html/body//main/div[1]/table[@class='table table-striped']/tbody/tr[4]/td[8]/form[@action='/deleteapp']//button[@name='deletebutton']").click()
Alert(browser).accept()
print("Test13 --- third delete success")
time.sleep(5)
print("*" *50)

#upload file
browser.find_element_by_xpath("//body//main/div[3]/a[@href='/details']/button[@type='button']").click()
time.sleep(2)
system_type_update_2 = Select(browser.find_element_by_name("AppName"))
system_type_update_2.select_by_index(1)
print("Test14 -- upload file test done")
time.sleep(5)
print("*" *50)
browser.back()
time.sleep(2)
browser.close()
print("Test15 -- chrome close successfully")
print("*" *50)

# 以下代码是对API 进行测试
"""
https://gist.github.com/lrhache/7686903 from 洪磊
从上述的Chrome 更换到 Firefox 进行API测试，上面的link 是用来
https://my.oschina.net/u/3204996/blog/1796460
"""


browser = webdriver.Firefox()
browser.maximize_window()
browser.get("http://betastore.carloudy.com/approved/?os=android")
time.sleep(2)
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
    r = requests.get(dictionary_1[i])
    #https://www.jianshu.com/p/ada99b7880a6    这是request 的解释
    #print(type(r)) #<class 'requests.models.Response'>
    print("Right now the nummber is {}, and the status code is {}!!!!".format(i, r.status_code))
    if r.status_code == 200:
        print("In the first API, the image I am print now is {}, and the link is {}:".format(i, data_1[i]))
        print("The image load success\n")
        time.sleep(2)
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nThe image didn't load success")
        print("In the first API, the image I am print now is {}, and the link is {}:\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n".format(i, data_1[i]))
        time.sleep(2)

  
    #try - catch的基本使用方法 
    #try:
    #except Exception as e:
     #   print(e)
   

time.sleep(3)
print("Test16 -- first api test success")
print("*" *50)


js='window.open("http://betastore.carloudy.com/approved/?os=ios");'
browser.execute_script(js)
time.sleep(3)
print("Test17 -- second api test success")
print("*" *50)

js='window.open("http://betastore.carloudy.com/appinfo/?appid=92e4r05x");'
browser.execute_script(js)
time.sleep(3)
print("Test17 -- third api test success")
print("*" *50)


js='window.open("http://betastore.carloudy.com/jsons/?appid=92e4r05x");'
browser.execute_script(js)
time.sleep(3)
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

print("Test18 -- forth api test success")
print("*" *50)


#browser.get(url_image)
#browser.get("http://www.google.com")
#https://www.zhihu.com/ques`tion/43604232
#https://stackoverrun.com/cn/q/13100729



"""
方法二
json_elements = json.dumps(data)
print(json_elements)

diction = json_elements[1:-1]
print("Dictionary is :",diction)
image_url = diction["files"]
print(image_url)
"""
