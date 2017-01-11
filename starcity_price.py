# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import codecs
import os
import sys
import time
import csv
import json

exec(open(os.getcwd() + "/config/config.py").read())

if len(sys.argv) < 2:
	print('please input card_set')
	exit()

if sys.argv[1] not in card_set:
	print('please input supported card_set')
	print(card_set)
	exit()

user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
headers = { 'User-Agent' : user_agent }
url = 'http://sales.starcitygames.com/cart_bulk_ajax.php'

set = sys.argv[1]

if os.path.exists("dailyprice") == False:
    os.mkdir("dailyprice")

if os.path.exists("dailyprice/%s"%(set)) == False:
    os.mkdir("dailyprice/%s"%(set))

w = codecs.open('dailyprice/%s/%s.csv'%(set, date_string), 'w', 'utf8')
w.write('CardName, CardSet, CardPrice\n')

first_flag = True

no_price = []

with open('starcity/%s/cardid.csv'%set, newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		if first_flag == True:
			first_flag = False
			continue
		if len(row) == 4:
			row_temp[0] = row[0] + row[1]
			row_temp[1] = row[2]
			row_temp[2] = row[3]
		else:
			row_temp = row
		data = {
			'cart_productids[]' : int(row_temp[2]),
			'cart_qtys[]' : 1,
			'mode' : 'login'
		}
		query = urllib.parse.urlencode(data)

		req = urllib.request.Request(url, query.encode('utf8'), headers)

		f = urllib.request.urlopen(req)

		temp = json.loads(f.read().decode('utf8'))
		print(row_temp, temp['cart_total'])
		if(temp['cart_total'] == None):
			temp['cart_total'] = '0'
			no_price.append(row_temp[0])
		w.write(row_temp[0] + ', ' + row_temp[1] + ', ' + row_temp[2] + ', ' + temp['cart_total'] + '\n')
		print(no_price)
		time.sleep(2)

w.write('The card with no price :\n')
for item in no_price:
    w.write(item + ',')
