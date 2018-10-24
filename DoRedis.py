# coding:utf-8

import Util
import base64
import sys
import urllib
import time
import datetime

"""
下载渠道对应的配置文件
"""
import redis
import os
import codecs
import re


def main():
	r = redis.Redis(host='127.0.0.1', port=6379, db=3)
	r.flushdb()
	print("============================begin for:" + str(datetime.datetime.now()) + "============================")
	p = r.pipeline()

	# for i in range(0,10000000):#20000000):
	#	p.sadd('n', str(i))   #添加

	print("============================add complete:" + str(datetime.datetime.now()) + "============================")
	p.execute()
	print("============================pipe complete:" + str(datetime.datetime.now()) + "============================")
	print (r.scard('n'))
	print("============================count complete:" + str(datetime.datetime.now()) + "============================")
	# print (r.get('name'))   #获取
	r.flushdb()
	print("============================del complete:" + str(datetime.datetime.now()) + "============================")


# print(r.scard('n'))

if __name__ == '__main__':
	print("============================start:" + str(datetime.datetime.now()) + "============================")
	# import matplotlib.matlab
	from matplotlib.pylab import *

	plot(arange(10))

	savefig('power.png', dpi=75)
	show()
	print("============================start:" + str(datetime.datetime.now()) + "============================")
