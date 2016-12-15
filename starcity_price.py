# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import codecs
import os
import sys
import time
import csv

exec(open(os.getcwd() + "/config/config.py").read())

if len(sys.argv) < 2:
	print('please input card_set')
	exit()

if sys.argv[1] not in card_set:
	print('please input supported card_set')
	print(card_set)
	exit()

set = sys.argv[1]

with open('starcity/%s/cardid.csv'%set, newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		print(row[0] + ' ' + row[1])


# user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
# headers = { 'User-Agent' : user_agent }

# url = 'http://sales.starcitygames.com/cart_bulk_ajax.php'
# data = {
# 	'cart_productids[]' : 1264013,
# 	'cart_qtys[]' : 1,
# 	'mode' : 'login'
# }

# query = urllib.parse.urlencode(data)

# req = urllib.request.Request(url, query.encode('utf8'), headers)

# f = urllib.request.urlopen(req)

# print(f.read())