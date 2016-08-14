#coding:utf-8
import re
import selenium
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from file_util import File_helper
class Spider:
    def __init__(self,people,content,desciption=None):
        helper=File_helper(1,'weibo'+content,description=desciption)
        driver=webdriver.Chrome()
        driver.get('http://m.weibo.cn/'+people+'/'+content+'/')
        time.sleep(2)
        #weibo_content=driver.find_element_by_class_name('weibo-text')
        weibo_content=driver.find_element_by_class_name('weibo-text')
        weibo_text=unicode.encode(weibo_content.text,encoding='utf-8')
        helper.append_line('微博正文')
        helper.append_line(weibo_text)
        js="window.scrollBy(0,10000)"
        for i in range(20):
            time.sleep(1)
            driver.execute_script(js)
        #comment_list=driver.find_elements_by_tag_name('li')
        comment_list=driver.find_elements_by_class_name('comment-con')

        helper.append_line('评论内容')
        i=0
        for comment in comment_list:
            i=i+1
            comment_text=unicode.encode(comment.text,encoding='utf-8')
            helper.append_line('评论'+str(i))
            helper.append_line(comment_text)





spider=Spider('1442246695','DCKfg9reA','民众对民族政策的看法')

