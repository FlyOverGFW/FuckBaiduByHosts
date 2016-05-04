# coding: utf-8

import requests as rq
from bs4 import BeautifulSoup as bs

def parse(html, select='', byid=None):
        element = select.split('.')[0]
        attr = select.split('.')[1]
        sp = bs(html, 'html.parser')
        if byid:
        	preproccess = {byid.split('=')[0]: byid.split('=')[1]}
        	elements = sp.find_all(**preproccess)
        	tmp = map(lambda x: x.find_all(element), elements)
        	imgs = []
        	for i in tmp:
        		for j in i:
        			imgs.append(j)
        else:
        	imgs = sp.find_all(element)
        li = []
        for i in imgs:
            if attr in i.attrs:
                li.append(i.attrs[attr])
        print 'List length: %d (%s)' % (len(li), select)
        return li

r = rq.get('http://www.baidu.com/more/')
li = parse(r.text, 'a.href')
tmp_set = set()
for i in li:
    try:
        tmp = i.split('/')[2]
        if tmp not in tmp_set:
            print tmp
            tmp_set.update([tmp])
    except:
        pass

