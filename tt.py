#!coding:utf-8
import re,time
import html
import sys, os, django
sys.path.append(".") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btcfaq.settings")
django.setup()


from googletrans import Translator
from pathlib import Path
from eth.models import Answer

translator = Translator()

with open("ans.xml") as f:
    for line in f.readlines():
        id = re.search(r'ParentId="[0-9]+"',line)
        own = re.search(r'OwnerUserId="(\d*)"',line)
        score = re.search(r'Score="(\d*)"',line)
        commentcount = re.search(r'CommentCount="(\d*)"',line)
        date = re.search(r'CreationDate="(.*?)"',line)
        try:
            _body       = line.split("Body=")[1].split("OwnerUserId=")[0]
            _id         = eval(id.group(0).split("=")[1])
            _own        = eval(own.group(0).split("=")[1])
            _score      = eval(score.group(0).split("=")[1])
            _commentcount  = eval(commentcount.group(0).split("=")[1])
            _date       = eval(date.group(0).split("=")[1])
        except Exception as e:
            print("********************获取内容错误************************************")
            continue


        with open("eossource.xml","w") as f2:
            f2.truncate()
            content = '''<?xml version="1.0" encoding="ISO-8859-1"?>''' + '''<document>''' + html.unescape(_body) + '''</document>'''
            f2.write(content)

        import xml.etree.ElementTree as ET
        try:
            tree = ET.parse('eossource.xml')
        #     root =  ET.fromstring(content)
        except Exception as e:
            print(e)
            continue
        root = tree.getroot()
        for child in root.iter():
            if child.tag != "code" and child.text:
                time.sleep(1)
                try:
                    new_text  = translator.translate(child.text,dest="zh-cn").text
                    child.text = new_text
                except Exception as e:
                    print("**********无法翻译以下标签内容********")
                    print(child.text)
                    continue
        #_content = ET.tostring(root, encoding='utf8', method='xml')
        #_content = ET.tostring(root, encoding='UTF-8',)
        try:
            tree.write("tmp.xml",encoding="UTF-8")
        except Exception as e:
            print(e)
            print("write tmp.xml error.........")

        try:
            _content = Path("tmp.xml").read_text().replace('<document>"','').replace('" </document>','')
        except Exception as e:
            continue
        print(_id,_content,_own,_score,_commentcount,_date)
        #_content = Path("tmp.xml").read_text().replace('<document>"','')
        #print(Path("tmp.xml").read_text())

#        print("-------------sofarsogood------------start to write dbo----") 
        Answer.objects.create(parentid=_id,ownuserid=_own,content=_content,score=_score,commentcount=_commentcount,origindate=_date)
        print("succefully...")
