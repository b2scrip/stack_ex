#!coding:utf-8
import re,time
import sys, os, django
sys.path.append(".") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btcfaq.settings")
django.setup()


from googletrans import Translator
from pathlib import Path

from post.models import Question
import html

translator = Translator()
mylist = []
with open("id.txt") as f:
    for line in f.readlines():
        mylist.append(line.rstrip())
n = 0 
for i in Question.objects.all():
    i.postid =  mylist[n]
    i.save()
    n += 1
