# -*- coding: utf-8 -*-

import codecs
import os
import sys
import time
from bs4 import BeautifulSoup

exec(open(os.getcwd() + "/config/config.py").read())

if len(sys.argv) < 2:
	print('please input card_set')
	exit()

if sys.argv[1] not in card_set:
	print('please input supported card_set')
	print(card_set)
	exit()