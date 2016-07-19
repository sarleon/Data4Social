#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
import sqlalchemy
class Spider:
    base_search_url="http://www.zhihu.com/search?type=content&q="

    def __init__(self,question):
        self.question=question
    def get_question_list(self):
        data={'type':'content','q':self.question}
        headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
                 'Referer':'http://www.zhihu.com/search?type=content&q=asd',
                 'Host':'www.zhihu.com'}
        question_list_request=requests.get(url=(self.base_search_url+self.question),params=data,headers=headers)
        question_list_soup=BeautifulSoup(question_list_request.text)
        question_atag_list=question_list_soup.find_all('a')
        pattern=re.compile('/question/(\d+)')
        question_number_list=list()
        for item in question_atag_list:
            question_number=pattern.search(item).group().strip()
            if  question_number is not None:
               question_number_list.append()


    def get_concrete_question(self,question_number):
        pass



if __name__=='__main__':
    spider=Spider("asd")
    spider.get_question_list()
