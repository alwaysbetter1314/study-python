# 爬取百度热点新闻标题
import requests as rq
from lxml import etree
import json

def gethot():
	headersParameters = {    #发送HTTP请求时的HEAD信息，用于伪装为浏览器
	    'Connection': 'Keep-Alive',
	    'Accept': 'text/html, application/xhtml+xml, */*',
	    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
	    'Accept-Encoding': 'gzip, deflate',
	    'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
	}

	r = rq.get("http://top.baidu.com/",headers = headersParameters).content
	rr = etree.HTML(r)
	ls = rr.xpath("//ul[@id='hot-list']/li/a[@class='list-title']/text()")
	s={}
	s['hotlist']=ls
	return json.dumps(s,ensure_ascii=False)
print(gethot())
