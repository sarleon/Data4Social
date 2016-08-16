
#coding:utf8
import zhihu_spider
import weibo_spider_new
zhihuspider=zhihu_spider.Spider("高房价")
question_number_list=zhihuspider.get_question_list()
for question_number in question_number_list:
    zhihuspider.get_concrete_question(question_number)

weibo_spider_new.Spider(6,'1638782947','E3OUXl0HL','房价2')

