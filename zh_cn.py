#!/usr/bin/python
# coding=utf8
import sys
import codecs;
import re;
import os

# import sys
reload(sys)

sys.setdefaultencoding('utf-8')

keys = ['歌手', '排行']

path = r'F:/NAVSELECT_1'

g_all_cnt = 0;
g_all_s = set()


class key_item(object):
	def __init__(self, key):
		self.u = set();
		self.all = [];
		self.key = key;

	def add(self, u):
		self.u.add(u);
		self.all.append(u);

	def finish(self):
		print(
		"key = " + self.key.encode('gbk', 'ignore') + " unique = " + str(len(self.u)) + " all = " + str(len(self.all)))


def calc_cnt(file):
	global g_all_cnt
	global g_all_s
	# match_cnt = 0;
	# s = set();

	map_res = {};
	for key in keys:
		map_res[key] = key_item(key);
	# print(key.encode('gbk','ignore'))

	for i in file:
		# g_all_cnt += 1;
		mt = re.match(".*U:([0-9]*).*\((\s*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s*)\)", i, re.IGNORECASE)

		if mt:
			uid = mt.group(1);
			g_all_cnt += 1;
			g_all_s.add(uid);
			for key in keys:
				res = i.decode('gbk', 'ignore').find(key);
				if res != -1:
					map_res.get(key).add(uid);
		else:
			print('can\'t find U exception : ', i)

	for key in keys:
		map_res[key].finish();
	print('total count = ' + str(g_all_cnt))


if __name__ == "__main__":
	fRead = sys.stdin;
	if sys.stdin.isatty() or sys.platform == "win32":
		fRead = codecs.open(path);  # 非重定向则读取指定文件数据
	calc_cnt(fRead);
