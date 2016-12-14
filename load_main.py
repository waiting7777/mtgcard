# -*- coding: utf-8 -*-

import urllib.request
import codecs
import os
import sys
import time

exec(open(os.getcwd() + "/config/config.py").read())

if len(sys.argv) < 2:
	print('please input card_set')
	exit()

if sys.argv[1] not in card_set:
	print('please input supported card_set')
	print(card_set)
	exit()

set = sys.argv[1]

if os.path.exists("card_data") == False:
    os.mkdir("card_data")

if os.path.exists("card_data/%s"%(set)) == False:
    os.mkdir("card_data/%s"%(set))

for lan in language:
	if os.path.exists('card_data/%s/%s'%(set, lan)) == False: 
		os.mkdir('card_data/%s/%s'%(set, lan))

	f = urllib.request.urlopen('%s/%s/%s.html'%(domain, set, lan))

	w = codecs.open('card_data/%s/%s_all.html'%(set, lan), 'w', 'utf8')

	w.write(f.read().decode('utf8'))
	f.close()
	w.close()

for lan in language:
	for i in range(total_num[set]):
		index = i + 1
		print(index)

		f = urllib.request.urlopen('%s/%s/%s/%d.html'%(domain, set, lan, index))
		w = codecs.open('card_data/%s/%s/%d.html'%(set, lan, index), 'w', 'utf8')
		w.write(f.read().decode('utf8'))
		
		f.close()
		w.close()

		print ('save %s %s %d.html'%(set, lan, index))
		time.sleep(1)

