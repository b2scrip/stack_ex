import re
with open("pattern.xml") as f:
    for line in f.readlines():
        date = re.search(r'CreationDate="(.*?)"',line)
        print(date.group())
