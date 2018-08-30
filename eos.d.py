#!coding:utf-8
import re,time
import sys, os, django
sys.path.append(".") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btcfaq.settings")
django.setup()


from googletrans import Translator
from pathlib import Path

from eos.models import Question
import html
n = 0

#with open("eostitle.xml") as f:
#    for line in f.readlines():
#        date = re.search(r'CreationDate="(.*?)"',line)
#        print(date.group())
#    mystr = '''grep 'OwnerUserId="%s"' Posts.xml  |grep 'Score="%s"' |grep 'ViewCount="%s"' |grep 'AnswerCount="%s"' ''' % \
#              (item.ownuserid,item.score,item.viewcount,item.answercount)
#    print(mystr)
mylist = {}
with open("date.txt") as f:
    for line in f:
        key =  line.split()[0]
        value = eval(line.split()[1].split("=")[1])
        mylist[key] = value
#print(mylist)

for item in Question.objects.all():
    try:
        item.postid = mylist[item.origindate]
        item.save()
    except Exception :
        print(item.id,mylist[item.origindate])
        continue
