# coding:utf-8

import json
import urllib
import time
import urllib2
import sys
import codecs;
import re
import logging
import datetime
import os
import getopt
import requests
import IPy

reload(sys)
sys.setdefaultencoding("utf-8")


def request_fun():
	session = requests.session()
	'''
	str_url =[
			"http://comment.kuwo.cn/com.s?type=get_rec_comment&uid=0&digest=15&sid=316799&page=1&rows=10&f=web&prod=MUSIC_8.7.5.0_BDS4&devid=15710039",
			"http://comment.kuwo.cn/com.s?type=get_rec_comment&uid=0&digest=15&sid=15249345&page=1&rows=10&f=web&prod=MUSIC_8.7.5.0_BDS4&devid=15710039",
	        "http://comment.kuwo.cn/com.s?type=get_rec_comment&uid=0&digest=15&sid=451779&page=1&rows=10&f=web&prod=MUSIC_8.7.5.0_BDS4&devid=15710039"
	    ]
	for i in range(0,10):
		#session = requests.session()
		print (session.get(str_url[i%3]) ," index = ",str(i%3))
	'''
	print(session.get("https://www.zhibo8.cc/index.html"))


def urllib2_fun():
	req = urllib2.Request("https://www.zhibo8.cc/index.html")
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	print(res.encode('gbk'))


def urllib_fun():
	fUrl = urllib.urlopen("https://www.zhibo8.cc/index.html")
	strHtml = fUrl.read(20480)
	# strHtml = strHtml.decode("utf-8","ignore")
	print(strHtml.encode('gbk'))


if __name__ == '__main__':
	# request_fun();
	# urllib_fun();
	request_fun();
