#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
import sqlalchemy
class Spider:
    base_search_url="http://www.zhihu.com/search?type=content&q="

    def __init__(self, topic):
        self.topic=topic
    def get_question_list(self):
        data={'type':'content','q':self.topic}
        headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
                 'Referer':'http://www.zhihu.com/search?type=content&q=asd',
                 'Host':'www.zhihu.com'}
        question_list_request=requests.get(url=(self.base_search_url + self.topic), params=data, headers=headers)
        question_list_soup=BeautifulSoup(question_list_request.text,'lxml')
        question_atag_list=question_list_soup.find_all('a')
        question_atag_string_list=[]
        for atag in question_atag_list:
            question_atag_string_list.append(str(atag))
        pattern=re.compile('/question/(\d+)')
        question_number_list=[]
        for item in question_atag_string_list:
            question_number_regex=pattern.search(item)
            if question_number_regex is not None:
                question_number=question_number_regex.group(1)
                question_number_list.append(question_number)
                print question_number
        return question_number_list

    def get_concrete_question(self,question_number):
        question_base_url="https://www.zhihu.com/question/"
        question_url=question_base_url+question_number
        headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
                 'Referer':'http://www.zhihu.com/search?type=content&q=asd',
                 'Host':'www.zhihu.com'}
        question_request=requests.get(question_base_url+question_number,headers=headers)
        question_soup=BeautifulSoup(question_request.text,'lxml')
        question_name=question_soup.find('div',id='zh-question-title').contents[1].contents[1].string
        print question_name

        question_div_list=question_soup.find_all('div',class_='zm-item-answer')
        for item in question_div_list:
            pass


if __name__=='__main__':
    spider=Spider("asd")
    spider.get_question_list()
    spider.get_concrete_question('26417244')

