#-*_coding:utf-8-*-
import requests
import re
import string
import lxml.html
for i in range(0,10):

    datas=25*i
    url='https://movie.douban.com/top250?start=%d&filter='%datas
    html1=requests.get(url).content

    selector=lxml.html.fromstring(html1)

    info=selector.xpath('//div[@class="info"]')

    print info

    for each in info:
        name=each.xpath('//div[@class="hd"]/a/span[@class="title"]/text()')
    for content in name:
        print content
# movies=str(re.findall('<span class="title">(.*?)</span>',html1,re.S))
#
# for movie in info:
#     myfile=open('myfile','w')
#
#     myfile.write(movie)
#     myfile.close()
#     print movie