# -*- coding: utf-8 -*-

import urllib.request
import codecs
import os
import sys
import time

user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
headers = { 'User-Agent' : user_agent }

exec(open(os.getcwd() + "/config/config.py").read())

if len(sys.argv) < 2:
	print('please input card_set')
	exit()

if sys.argv[1] not in card_set:
	print('please input supported card_set')
	print(card_set)
	exit()

set = sys.argv[1]

if os.path.exists("starcity") == False:
    os.mkdir("starcity")

if os.path.exists("starcity/%s"%(set)) == False:
    os.mkdir("starcity/%s"%(set))

for rarity in star_city_rarity:

	for i in range(star_city_page[set][rarity]):

		url = 'http://sales.starcitygames.com/category.php?cat=%d&rarity=%s&start=%d'%(star_city_set_number[set], rarity, i*50)
		req = urllib.request.Request(url, None, headers)
		f = urllib.request.urlopen(req)

		w = codecs.open('starcity/%s/%s_%d.html'%(set, rarity, i+1), 'w', 'utf8')
		w.write(f.read().decode('utf8'))
		print('starcity/%s/%s_%d.html'%(set, rarity, i+1))
		time.sleep(1)
