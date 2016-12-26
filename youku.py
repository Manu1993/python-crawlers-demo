# -*- coding: utf-8 -*-
import requests
import re
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

url='http://v.youku.com/v_show/id_XMTgxNDI3MTc0OA==.html?from=y1.6-85.3.1.2dddc390257b11e59e2a'
html=requests.get(url).content

videoId=re.search('videoId:(.*?),',html).group()
Id=re.search('(\d+)',videoId).group()
for i in range(1,3):
    urlyou='http://p.comments.youku.com/ycp/comment/pc/commentList?jsoncallback=n_commentList&objectId=453567937&app=100-DDwODVkv&pageSize=30&listType=0&sign=9fb62e3dfb5e9fcb67238dfdc3b51fb3&time=1479260623042&currentPage=%d'%i
    htmlyou=requests.get(urlyou).content
    ct=re.findall('n_commentList((.*?))',htmlyou)

    # print ct
    # print htmlyou
    # print (type(htmlyou))
    # ht=json.loads(urlyou)
    # print ht
    content=re.findall('"content":"(.*?)",',htmlyou)

    # print htmlyou
    # for each in content:
    #    print each


