# -*- coding:utf-8 -*-

import os
import re

item_re = re.compile(r'''([0-9]+)\t(.*?)\t([0-9]+\.[0-9]+%)\t+([a-zA-Z]+)
''')

f = open('c.txt', 'r')
lines = f.readlines()
f.close()


chs = []


def item_sub(match):
    number = match.group(1)
    title = match.group(2)
    difficulty = match.group(4)
    filename = number+'-'+title.replace(' ', '-')+'.MD'
    chs.append((number, title, difficulty, filename))
    return '---'

for i in range(0, len(lines)):
    line = lines[len(lines) - i - 1]
    item_re.sub(item_sub, line)

for ch in chs:
    if os.path.exists(ch[3]):
        print('| %s | [%s](%s) | %s | | |' % ( ch[0], ch[1], ch[3], ch[2] ))
    else:
        print('| %s | %s | %s | | |' % ( ch[0], ch[1], ch[2] ))
