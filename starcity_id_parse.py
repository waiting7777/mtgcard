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

set = sys.argv[1]

if os.path.exists("starcity") == False:
    os.mkdir("starcity")

if os.path.exists("starcity/%s"%(set)) == False:
    os.mkdir("starcity/%s"%(set))

w = codecs.open('starcity/%s/cardid.csv'%set, 'w', 'utf8')
w.write('CardName, CardSet, StarCardId\n')

dic = {}

# f = codecs.open('card_data/%s/en_all.html'%(set), 'r', 'utf8')
#
# content = f.read()
#
# soup = BeautifulSoup(content, 'html.parser')

card_data = {}

# for item in soup.select('.even'):
#     card_data[item.select('a')[0].text] = item.select('td[align="right"]')[0].text
#
# for item in soup.select('.odd'):
#     card_data[item.select('a')[0].text] = item.select('td[align="right"]')[0].text

print(card_data)

for rarity in star_city_rarity:

    for i in range(star_city_page[set][rarity]):

        f = codecs.open('starcity/%s/%s_%d.html'%(set, rarity, i+1), 'r', 'utf8')

        content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        for item in soup.select('.card_popup'):
            if '(' in item.text:
                print(item.text, item['href'][-7:], item.text.index('('))
                dic[item.text[1:item.text.index('(')-1]] = item['href'][-7:]
            else:
                print(item.text, item['href'][-7:])
                dic[item.text[1:]] = item['href'][-7:]

        f.close()

for key in sorted(dic):
    print(key, dic[key])
    w.write(key + ', ' + set + ', ' + dic[key] + '\n')
