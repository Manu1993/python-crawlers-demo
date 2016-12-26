
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

import requests
import re
import lxml.html
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
path='/Users/apple/Desktop/chromedriver'
driver =webdriver.Chrome(path)
htm='http://h5test.joojia.com/WeChat/resource/vue/website/index.html'
h=driver.get(htm)
time.sleep(1)
element=driver.find_element_by_class_name("map").click()
ele=driver.find_element_by_tag_name("input")
ele.click()
ele.clear()
ele.send_keys(u'\u91d1\u534e\u5e02')
time.sleep(1)
elem=driver.find_element_by_xpath("//div[@id='amap-sug2']").click()
time.sleep(1)
waimai=driver.find_element_by_xpath("//a[@href='order/Takeout_detail.html']").click()
money=driver.find_element_by_xpath("//li/div[@class='text_main']/div[@class='list_text']/p/span[@class='mony']")
print money
print driver.current_url
r =requests.get(driver.current_url).content
selector=lxml.html.fromstring(r)
info=selector.xpath('//li/div[@class="text_main"]/div[@class="list_text"]/p/span[@class="mony"]/text()')



# print h
# url='http://h5test.joojia.com/WeChat/resource/vue/website/order/Takeout_detail.html'
# html=requests.get(url).content
# selector=lxml.html.fromstring(html)
# info=selector.xpath('//li/div[@class="text_main"]/div[@class="list_text"]/p/text()')
