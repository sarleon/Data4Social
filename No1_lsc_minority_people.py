#coding:utf8
import zhihu_spider
spider=zhihu_spider.Spider("民族政策")
question_number_list=spider.get_question_list()
for question_number in question_number_list:
    spider.get_concrete_question(question_number)


spider.get_concrete_question('24120354')
spider.get_concrete_question('34513121')