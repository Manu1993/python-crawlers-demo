
# -*- coding: utf-8 -*-
import requests
import lxml.html
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
for i in range(1,8):
    url='http://www.dongyeguiwu.com/books/baiyexing/53.html/%d'%i;

    html=requests.get(url).content
    selector=lxml.html.fromstring(html)
    info=selector.xpath('//div[@class="readtext"]/p/text()')

    listbai=[];
    for each in info:


        listbai.append(each)

    f=open('white.txt','w')
    for bai in listbai:

        f.write(bai)
        f.write('\n')

    f.close()
