#coding:utf8
import zhihu_spider
import weibo_spider_new
zhihuspider=zhihu_spider.Spider("英国脱欧")
question_number_list=zhihuspider.get_question_list()
for question_number in question_number_list:
    zhihuspider.get_concrete_question(question_number)




weibospider1=weibo_spider_new.Spider(1,'1638782947','DC8MEyasm','英国脱欧1')
weibospider2=weibo_spider_new.Spider(1,'1698233740','DC8I3aV6e','英国脱欧2')