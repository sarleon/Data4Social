#coding:utf-8
import os
class File_helper:
    FILE_DIR='./result'
    question_list=['No1_lsc_minority_people',
                       'No2_lsc_USA_election']
    def __init__(self,question_number,info_source,description=None):
        question=self.question_list[question_number-1]





helper=File_helper(1,'zhihu')