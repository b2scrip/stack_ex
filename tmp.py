#!coding:utf-8
import re,time
import sys, os, django
sys.path.append(".") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btcfaq.settings")
django.setup()

from post.models import Question as qn

for item in qn.objects.all():
    #res = '''if [ $(grep  'OwnerUserId="%s"' Posts.xml | grep 'Score="%s"' |grep 'ViewCount="%s"' | grep 'AnswerCount="%s"' | grep 'Tags="%s"' |wc -l) != 1 ];then grep  'OwnerUserId="%s"' Posts.xml | grep 'Score="%s"' |grep 'ViewCount="%s"' | grep 'AnswerCount="%s"' ;fi ''' % \
    #      (item.ownuserid,item.score,item.viewcount,item.answercount,item.tags,item.ownuserid,item.score,item.viewcount,item.answercount)
   # res = '''grep  'OwnerUserId="%s"' Posts.xml | grep 'Score="%s"' |grep 'ViewCount="%s"' | grep 'AnswerCount="%s"' | grep 'Tags="%s"' > pattern.xml''' % \
   #       (item.ownuserid,item.score,item.viewcount,item.answercount,item.tags)
   if ownuserid == 29353 and item.score  == 1 and item.viewcount == 47  and item.answercount ==  and item.tags == :
        print(item.content) 
