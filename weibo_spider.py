#coding:utf-8
import re
import requests
from bs4 import BeautifulSoup
from selenium import selenium,webdriver
class Spider:
    base_url='http://m.weibo.cn/'
    def __init__(self,user_id,question_id):

        self.user_id=user_id
        self.question_id=question_id
        data={'type':'comment'}
        cookies={
            '_T_WM':'29db43da761f4adc0a53322436bb6f50',
            'SUB':'_2A256raXRDeTxGeNJ7FMZ8ibPyD-IHXVWUcuZrDV6PUJbkdBeLXTckW2JVHzzU62ankF9lJkLdKbjyNnyTA..',
            'SUHB':'0z1ARwRlvHoKYQ',
            'SSOLoginState':'1470748033',
            'M_WEIBOCN_PARAMS':'uicode%3D20000061%26featurecode%3D20000180%26fid%3D3992342342249644%26oid%3D3992342342249644',

            'YF-Page-G0':'f017d20b1081f0a1606831bba19e407b',
            'SUBP':'0033WrSXqPxfM72wWs9jqgMF55529P9D9W5HbZvK6P273.UChYJYS3Vs5JpVF02f1K5feK.4eh2E',
            'login_sid_t':'7266fe6dddc26de25f6e41bc4d9c3b1a	',
            'un':'15905199012'

        }
        headers={
            'Host':'m.weibo.cn',
            'Connection':'keep-alive',
            'Cache-Control':'max-age=0',

            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Content-Type': 'application/x-www-form-urlencoded'
                 }
        url=self.base_url+user_id+'/'+question_id
        print url

        r=requests.get(url=url,headers=headers,cookies=cookies)
        self.soup=BeautifulSoup(r.text,'lxml')
        print r.text
        print '********************************************************'

    def get_comment_list(self):
        comment_list=self.soup.find_all('li')
        print comment_list



spider=Spider('1442246695','DCKfg9reA')
spider.get_comment_list()