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

'''
def from_this_dir(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

FILE = from_this_dir("log")
curDay = datetime.datetime.now().strftime("%Y%m%d")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(filename)s <%(process)d> [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y%m%d %H:%M:%S',
                    filename = os.path.join(FILE,curDay + '_log.txt'),
                    filemode='a+')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(filename)s <%(process)d> [line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)
'''

path = r'F:/stat/20181018_PLAY_ERR.txt'

dict_rid_uid = {};


class user_item(object):
	def __init__(self):
		self.u = set();

	def add(self, u):
		self.u.add(u);

	def len(self):
		return len(self.u)


def GetRIDAndCnt(file):
	global g_all_cnt
	global g_all_s

	for i in file:
		# g_all_cnt += 1;
		mt = re.match(".*RID:([^\|]*).*U:([0-9]*)", i, re.IGNORECASE)

		if mt:
			rid = mt.group(1);
			uid = mt.group(2);
			if len(rid) > 0:
				if rid not in dict_rid_uid:
					dict_rid_uid[rid] = user_item();
				dict_rid_uid[rid].add(uid);

	rid_location = sorted(dict_rid_uid.items(), lambda x, y: cmp(x[1].len(), y[1].len()), reverse=True)

	for rid, item in rid_location:
		if item.len() > 0:
			print rid + "\t" + str(item.len());


if __name__ == '__main__':
	fRead = sys.stdin;
	if sys.stdin.isatty() or sys.platform == "win32":
		fRead = codecs.open(path);  # 非重定向则读取指定文件数据
	# GetIPLocation(fRead);
	GetRIDAndCnt(fRead);
