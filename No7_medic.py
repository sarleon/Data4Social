
#coding:utf8
import zhihu_spider
import weibo_spider_new
zhihuspider=zhihu_spider.Spider("看病贵")
question_number_list=zhihuspider.get_question_list()
for question_number in question_number_list:
    zhihuspider.get_concrete_question(question_number)

weibo_spider_new.Spider(6,'1649173367','E2STxlYOH','看病贵2')

