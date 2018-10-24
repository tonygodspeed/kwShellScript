# coding=utf8

__author__ = 'Administrator'

import json
import sys
import os

import re
import codecs
from collections import Counter

reload(sys)
sys.setdefaultencoding("utf-8")

# 更新的任务列表
vec_files = [
	# "1007.dll",
	"1010.dll",
	# "1011.dll",
	# "1012.dll",
	# "RecomTips.exe",
]

# 打包的地址
base_path = r'\\172.17.60.30\OutPackage\KwShellExt_trunk\201807\303_2018072516283529_Package_33957_1.0.6.9077\Product_Release'
# base_path = r'\\172.17.60.30\OutPackage\KwShellExt_trunk\201801\282_2018012318503923_Package_32222_1.0.6.9077\Release'
# r'F:\packet\20171211_vip_no_tips_pr\Product_Release'
# task_list地址
task_list_path = r'F:\software\xampp\htdocs\lyrics\img\kwgg\bigdata\t\task_list\task_list_58'
# recomtips配置地址
recomtips_info_path = r'F:\software\xampp\htdocs\lyrics\img\kwgg\bigdata\t\1007\getrecomcfgdata_v12'

# 以下地址基本固定
task_zip_path = r'F:\software\xampp\htdocs\lyrics\img\kwgg\bigdata\t'
base_url = r'http://wa.kuwo.cn/lyrics/img/kwgg/bigdata/t/'
import win32api
import zipfile
import datetime
import shutil;
import hashlib;


# 变化的内容
class task_info(object):
	def __init__(self, ver, url, md5):
		self.ver = ver;
		self.url = url;
		self.md5 = md5;


# 返回目标地址算md5 返回url填写json
def zip_file(file_path, file_ver):
	curDay = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S");
	(shotname, extension) = os.path.splitext(os.path.basename(file_path))

	zip_file = os.path.join(os.path.dirname(file_path), shotname + "_" + curDay + "_" + file_ver + ".zip");
	azip = zipfile.ZipFile(zip_file, 'w')
	azip.write(file_path, os.path.basename(file_path),
	           compress_type=zipfile.ZIP_DEFLATED)  # compress_type=zipfile.ZIP_LZMA
	azip.close()
	base_dir = shotname;
	if shotname == "RecomTips":
		base_dir = "tips"

	url_path = base_url + base_dir + "/" + os.path.basename(zip_file);
	tar_zip_path = os.path.join(os.path.join(task_zip_path, base_dir), os.path.basename(zip_file));

	if os.path.isfile(tar_zip_path):
		os.remove(tar_zip_path)

	shutil.copyfile(zip_file, tar_zip_path);

	return tar_zip_path, url_path;


def get_file_ver(file_path):
	info = win32api.GetFileVersionInfo(file_path, os.sep)
	ms = info['FileVersionMS']
	ls = info['FileVersionLS']
	version = '%d.%d.%d.%d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
	return version


def calc_md5(file_path):
	with open(file_path, "rb") as f:
		md5 = hashlib.md5(f.read()).hexdigest();
		f.close();
	return md5;


def get_task_ver():
	index = task_list_path.rfind("_");
	ver = 0;
	if index != -1:
		ver = task_list_path[index + 1:]
	return ver


def update_task_list(vec_task_info):
	print task_list_path
	with open(task_list_path, "r") as f:
		data = f.read();
		f.close();
		data = data.decode('utf-8')
		pydata = json.loads(data)

		task_ver = get_task_ver();
		if task_ver > 0:
			pydata["task_version"] = int(task_ver)

		vec_task = pydata["task_list"];
		for t in vec_task:
			name = t["name"];
			if vec_task_info.has_key(name):
				t["md5"] = vec_task_info[name].md5
				t["version"] = vec_task_info[name].ver
				t["url"] = vec_task_info[name].url
				print('name = ' + name + ' ver = ' + vec_task_info[name].ver + ' done');
			else:
				print(t["name"] + ' this task is not in the list!!!!!!!!!!!!!');
	with open(task_list_path, "w") as fw:
		json.dump(pydata, fw, ensure_ascii=False, indent=4)
		fw.close()
	return;


def update_recomtips_info(task_info):
	with open(recomtips_info_path, "r") as f:
		data = f.read();
		f.close();
		data = data.decode('utf-8')
		pydata = json.loads(data)
		t = pydata["recomdata"];
		t["ver"] = task_info.ver;
		t["md5"] = task_info.md5;
		t["url"] = task_info.url;
	with open(recomtips_info_path, "w") as fw:
		json.dump(pydata, fw, ensure_ascii=False, indent=4)
		fw.close()
	return;


if __name__ == "__main__":
	# print get_task_ver();
	# update_task_list();

	vec_task_info = {};
	for file_name in vec_files:
		file_path = os.path.join(base_path, file_name);
		file_ver = get_file_ver(file_path);
		# print(file_name + " " + file_ver);
		zip_file_path, url_path = zip_file(file_path, file_ver);
		zip_md5 = calc_md5(zip_file_path);
		name, ext = os.path.splitext(file_name)
		if name == "RecomTips":
			update_recomtips_info(task_info(file_ver, url_path, zip_md5))
		else:
			vec_task_info[name] = task_info(file_ver, url_path, zip_md5)

	if len(vec_task_info) > 0:
		update_task_list(vec_task_info)
