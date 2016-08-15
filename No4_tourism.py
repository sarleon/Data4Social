
#coding:utf8
import zhihu_spider
import weibo_spider_new
zhihuspider=zhihu_spider.Spider("打击恐怖主义")
question_number_list=zhihuspider.get_question_list()
for question_number in question_number_list:
    zhihuspider.get_concrete_question(question_number)




weibospider1=weibo_spider_new.Spider(2,'1709157165','E35Ck7Ffq','恐怖主义2')
weibospider2=weibo_spider_new.Spider(2,'2335625480','E2Zug7KS0','恐怖主义')

