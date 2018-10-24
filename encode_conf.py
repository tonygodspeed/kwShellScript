# coding=utf8
__author__ = 'Administrator'

import json
import sys
import os
from collections import Counter
import Util;

reload(sys)
sys.setdefaultencoding("utf-8")


def encode_config(org_path, tar_path):
	with open(org_path, "r") as f:
		data = f.read();
		f.close();
		# data = data.decode('unicode-escape');
		data = data.decode('utf-8')
		data = data.decode('string_escape');
		import base64;
		d_result = base64.b64encode(data)

		import codecs;
		# strdata = json.dumps(pydata,ensure_ascii=False);
		with codecs.open(tar_path, "w") as fw:
			fw.write(d_result);
			fw.close()


def decode_config(org_path, tar_path):
	with open(org_path, "r") as f:
		data = f.read();
		f.close();
		data = data.decode('utf-8')
		data = data.decode('string_escape');
		import base64;
		d_result = base64.b64decode(data);
		import codecs;
		with codecs.open(tar_path, "w") as fw:
			fw.write(d_result);
			fw.close()


def encode_conf():
	org = r"F:\software\xampp\htdocs\plugin\ecom\conf_ver32_uac1_ip0";
	tar = os.path.dirname(org);
	tar = os.path.join(tar, os.path.basename(org) + "_encode");
	# encode_config(org,tar);
	decode_config(tar, org);


def encode_data(org_path, tar_path):
	with open(org_path, "r") as f:
		# print(f)
		data = f.read();
		f.close();
		# data = data.decode('unicode-escape');
		data = data.decode('utf-8')
		data = data.decode('string_escape');
		# print(data);
		g_strBase64Key = "yeelion "
		d_result = Util.KwBase64_encode(data, g_strBase64Key)

		# strdata = json.dumps(pydata,ensure_ascii=False);
		with open(tar_path, "w") as fw:
			fw.write(d_result);
			# json.dump(d_result,fw,ensure_ascii=False)
			fw.close()


def decode_data(org_path, tar_path):
	with open(org_path, "r") as f:
		# print(f)
		data = f.read();
		f.close();
		# data = data.decode('unicode-escape');
		data = data.decode('utf-8')
		data = data.decode('string_escape');
		# print(data);
		g_strBase64Key = "yeelion "
		d_result = Util.KwBase64_decode(data, g_strBase64Key)

		# strdata = json.dumps(pydata,ensure_ascii=False);
		with open(tar_path, "w") as fw:
			fw.write(d_result);
			# json.dump(d_result,fw,ensure_ascii=False)
			fw.close()


def json_del_intent(org_path, tar_path):
	with open(org_path, 'r') as f:
		data = f.read();
		f.close();
		data = data.decode('gbk').encode('utf-8')
		pydata = json.loads(data)
		with open(tar_path, "w") as fw:
			json.dump(pydata, fw, ensure_ascii=False)
			fw.close()


def print_stack():
	try:
		raise ZeroDivisionError
	except ZeroDivisionError:
		print(sys.exc_info()[2].tb_lineno)


def encode_1003():
	# org = r"F:\software\xampp\htdocs\lyrics\img\kwgg\bigdata\t\1003\scan_rules.rules_v4.json";
	org = r"F:\software\xampp\htdocs\lyrics\img\kwgg\bigdata\t\1010\getlivead_v11";
	tar = os.path.dirname(org);
	tar = os.path.join(tar, os.path.basename(org) + "_encode");
	# encode_data(org,tar);
	decode_data(tar, org);


if __name__ == "__main__":
	# print_stack();
	encode_conf();
# encode_1003();
# decode_data(tar,org);

# check_key_words(org,r"E:\trunk\Doc\1010\encode")
