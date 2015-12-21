'''
Created on 2015-12-21

@author: shijing
'''
import urllib.request
import re
#网址
page=1
url='http://www.qiushibaike.com/hot/page/'+str(page)
userAgent='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:37.0) Gecko/20100101 Firefox/37.0'#用户代理
headers={'User-Agent':userAgent}#参数头部

try:
    request=urllib.request.Request(url,headers = headers)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?<h2.*?>(.*?)</h2>.*?</a>.*?<div.*?class' +
                                    '="content".*?>\s(.*?)<!--.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
    items=re.findall(pattern, content)
    for item in items:
        print(item[0],item[1],"获得了%s个赞"%item[-1])
        print()
except urllib.error as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)
        
        
    