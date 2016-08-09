#coding:utf-8
import re
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
class Spider:
    def __init__(self):
        driver=webdriver.Chrome()
        driver.get('http://m.weibo.cn/1442246695/DCKfg9reA')
        element=driver.find_element_by_class_name('comment=con')
        print element



spider=Spider()
