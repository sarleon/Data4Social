#coding:utf-8
import re
import requests
from bs4 import BeautifulSoup
class Spider:
    base_url='http://weibo.com/'
    def __init__(self,user_id,question_id):
        self.user_id=user_id
        self.question_id=question_id
        data={'type':'comment'}
        headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
                 'Accept-Encoding':'gzip, deflate, sdch',
                 'Host':'Host:weibo.com',
                 'Connection':'keep-alive',
                 'Upgrade-Insecure-Requests':'1',
                 }

        r=requests.get(url=self.base_url+user_id+'/'+question_id,data=data,headers=headers)
        self.soup=BeautifulSoup(r.text,'lxml')
        print r.text

    def get_comment_list(self):
        comment_list=self.soup.find_all('div','WB_text')
        print comment_list



spider=Spider('1442246695','DCKfg9reA')