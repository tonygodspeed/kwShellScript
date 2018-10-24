# coding=utf8
__author__ = 'Administrator'

import json
import sys
import os
import getopt
from collections import Counter

reload(sys)
sys.setdefaultencoding("utf-8")


def check_key_words(org_path, tar_path):
	with open(org_path, "r") as f:
		# print(f)
		data = f.read();
		f.close();
		# data = data.decode('unicode-escape');
		data = data.decode('gbk')
		# print(data);
		pydata = json.loads(data)
		print len(pydata["keywords"]);
		c = Counter(pydata["keywords"])
		del c[""];
		pydata["keywords"] = c.keys();
		with open(tar_path, "r") as t_f:
			t_data = t_f.read();
			t_f.close();
		t_data = t_data.decode('utf-8')
		t_pydata = json.loads(t_data)
		pydata["search_rules"] = t_pydata["search_rules"];
		pydata["keywords_blacklist"] = t_pydata["keywords_blacklist"];
		# strdata = json.dumps(pydata,ensure_ascii=False);
		with open(tar_path, "w") as fw:
			json.dump(pydata, fw, ensure_ascii=False)
			fw.close()
		d = str(c.most_common(50))
		print len(c.keys())
		print(d.decode('unicode-escape'))


def json_del_intent(org_path, tar_path):
	with open(org_path, 'r') as f:
		data = f.read();
		f.close();
		data = data.decode('gbk').encode('utf-8')
		pydata = json.loads(data)
		with open(tar_path, "w") as fw:
			json.dump(pydata, fw, ensure_ascii=False)
			fw.close()


if __name__ == "__main__":
	# print "hi"
	check_key_words(r"F:/181023.txt", r"F:/keywords_search_rules_v1")
	'''
	if(len(sys.argv) != 3):
		print("args err,please input path_org and path_target");
	else:
		if(os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2])):
			check_key_words(sys.argv[1],sys.argv[2])
		else:
			print("path not exist {0} or {1}".format(sys.argv[1],sys.argv[2]))
	'''
