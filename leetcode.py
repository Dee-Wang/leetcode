# -*- coding:utf-8 -*-

import os

for i in os.listdir():
	prefix = i[:i.find('-')]
	print(prefix)