#coding:utf8
import zhihu_spider
import weibo_spider_new
zhihuspider=zhihu_spider.Spider("美国大选")
question_number_list=zhihuspider.get_question_list()
for question_number in question_number_list:
    zhihuspider.get_concrete_question(question_number)




weibospider1=weibo_spider_new.Spider(2,'2693794880','E2DTe9qxr')
weibospider2=weibo_spider_new.Spider(2,'1442246695','E1B0SkMg2')
weibospider3=weibo_spider_new.Spider(2,'1442246695','E3vymiocU')