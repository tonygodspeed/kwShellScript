#!/usr/bin/python
# coding=utf8
import sys
import codecs;
import re;
import os

reload(sys)

sys.setdefaultencoding('utf-8')
split_tag = ".*"
keys = [
	# 'DSTATUS:WIFISDOK',
	# 'DSTATUS:WIFISDFAIL',
	# 'DSTATUS:CONNSDOK',
	# 'DSTATUS:CONNSDFAIL'
	'CLICK:1' + split_tag + 'bang',
	'GROUP:列表组1'
]

# path = r'/tmp/NAVSELEC.txt'
path = r'F:\stat\8771_bcs7_0812'

# '.*VER:([^\\|]*).*?MAC:([^\\|]*).*?quit_err:([^\\|]*)\\|.*?$'

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
		# print("key = " + self.key.encode('gbk','ignore') + " unique = " + str(len(self.u)) + " all = "+str(len(self.all)))
		print(self.key.encode('gbk', 'ignore') + str("\t") + str(len(self.all)) + str("\t") + str(len(self.u)))

	def output_u(self):
		for u in self.u:
			print(u);


def calc_cnt(file):
	global g_all_cnt
	global g_all_s
	# match_cnt = 0;
	# s = set();

	map_res = {};
	# for key in keys:


	# print(key.encode('gbk','ignore'))

	for i in file:
		# g_all_cnt += 1;
		# re.match(".*DISPLAY:([0-9]*)",i,re.IGNORECASE)
		str_org = i.decode('gbk', 'ignore');

		mt = re.match(".*DISPLAY:([^\\|]*)", str_org, re.IGNORECASE)
		if mt:
			key = mt.group(1);
			key = key.encode('utf8', 'ignore');
		else:
			continue;
		if key not in map_res:
			map_res[key] = key_item(key);
		mt = re.match(".*U:([0-9]*)", str_org, re.IGNORECASE)

		if mt:
			uid = mt.group(1);
			g_all_cnt += 1;
			g_all_s.add(uid);
			# for key in keys:
			# res = i.decode('gbk','ignore').find(key);
			# if res != -1:
			#	map_res.get(key).add(uid);
			v_k = key.split(split_tag);
			bFind = True;
			find_index = 0;
			for k in v_k:
				res = str_org.find(k, find_index);
				if res == -1:
					bFind = False
					break;
				else:
					find_index = res;
			if bFind:
				map_res.get(key).add(uid);
		else:
			print('can\'t find U exception : ', i)
	print("key\tcount\tunique")
	for key in map_res:
		map_res[key].finish();


if __name__ == "__main__":
	fRead = sys.stdin;
	if sys.stdin.isatty() or sys.platform == "win32":
		fRead = codecs.open(path);  # 非重定向则读取指定文件数据
	calc_cnt(fRead);
