#!coding:utf-8
import re,time
import sys, os, django
sys.path.append(".") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btcfaq.settings")
django.setup()


from googletrans import Translator
from pathlib import Path

from eth.models import Question
import html
n = 0

mylist = []

with open("id.txt") as f:
    for line in f:
        mylist.append(line.rstrip())

#print(mylist)
#        key =  line.split()[0]
#        value = eval(line.split()[1].split("=")[1])
#        mylist[key] = value
#print(mylist)

for item in Question.objects.all():
    try:
        item.postid = mylist[n]
        item.save()
        n += 1
    except Exception :
        print(item.id,)
        continue
