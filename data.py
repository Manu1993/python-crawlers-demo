#-*_coding:utf-8-*-
import requests
import re
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
        print u'开始爬取内容'
    def getsource(self,url):
        html = requests.get(url)
        return html.text

    # def changepage(self,url,total_page):
    #     now_page = int(re.search('pi=(\d)', url).group(1))
    #     page_group = []
    #     for i in range(now_page,total_page+1):
    #         link = re.sub('pi=\d','pi=%s'%i,url,re.S)
    #         page_group.append(link)
    #     return page_group

    def geteveryapp(self,source):
        # everyapp = re.findall('(<div class="threadlist_detail clearfix".*?</div>)',source,re.S)
        everyapp = re.findall('(<div class="threadlist_text pull_left">.*?</div>)',source,re.S)
        return everyapp

    def getinfo(self,eachclass):
        info = re.search('u.*?',eachclass,re.S).group(2)
        return info

    def saveinfo(self,classinfo):
        f = open('info.txt','a')

        for each in classinfo:

            f.writelines(each['app_url'] + '\n')
        f.close()

if __name__ == '__main__':

    appinfo = []
    url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%B5%99%E6%B1%9F%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6'
    appurl = spider()


    print u'正在处理页面' + url
    html = appurl.getsource(url)
    every_app = appurl.geteveryapp(html)
    # oka=appurl.getinfo(every_app)
    # my=every_app.read().decode("gbk")
    # print my
    every_app = "中文"
    print unicode(every_app, "gbk")

    # for each in every_app:

    # appurl.saveinfo(appinfo)