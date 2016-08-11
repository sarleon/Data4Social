#coding:utf-8
import re
import selenium
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from file_util import File_helper
class Spider:
    def __init__(self,people,content):
        helper=File_helper(1,'weibo','asdasd')
        driver=webdriver.Chrome()
        driver.get('http://m.weibo.cn/'+people+'/'+content+'/')
        time.sleep(2)
        weibo_text=driver.find_element_by_class_name('weibo-text')
        js="window.scrollBy(0,10000)"
        for i in range(20):
            time.sleep(1)
            driver.execute_script(js)
        print weibo_text.text
        comment_list=driver.find_elements_by_tag_name('li')
        for comment in comment_list:
            print '评论'
            print comment.text


        time.sleep(100)



spider=Spider('1442246695','DCKfg9reA')

