#coding:utf-8
import os
class File_helper:
    FILE_DIR='./result/'
    question_list=['No1_lsc_minority_people',
                       'No2_lsc_USA_election']

    def __init__(self,question_number,info_source,description=" "):
        self.question=self.question_list[question_number-1]
        self.f=open(name=self.FILE_DIR+str(question_number)+'_'+info_source+'_'+description+'.txt',mode='w')
    def append_line(self,content):

        self.f.write(content+"\n")







helper=File_helper(1,'zhihu')
helper.append_line("asdasdsa")
helper.append_line("121414")
