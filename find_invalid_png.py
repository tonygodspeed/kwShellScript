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


def get_file_list(folder_name, list_png, list_xml):
	try:
		lstFiles = os.listdir(folder_name)
		for item in lstFiles:
			local_path = os.path.join(folder_name, item)

			if os.path.isfile(local_path):  # and os.path.getsize(local_path) > 1*1024:
				if local_path.find(".xml") != -1:
					list_xml.append(local_path);
				elif local_path.find(".png") != -1:
					list_png.add(item.replace(".png", ""))
					print(item);
	except Exception, message:
		print(message.message)
	pass


xml_png = set();
code_png = set();


def read_png_from_xml(path):
	try:
		# print("xml file name = ",path)

		lines = codecs.open(path)
		for line in lines:
			vec = line.split(' ');
			for key in vec:
				res = re.findall('.*image=\"(.*\.png)\"', key, re.IGNORECASE);
				# res = re.findall('.*image=\"(.*\.png)\"', line, re.IGNORECASE);
				for png_name in res:
					name = re.sub("_\d+", "", png_name);
					# print("xml png name = ",name);
					xml_png.add(name)
	finally:
		if lines:
			lines.close()
	print(xml_png);


def read_png_from_code(path):
	try:
		lines = codecs.open(path)
		for line in lines:
			res = re.findall('.*_T\(\"(.*\.png)\"\)', line, re.IGNORECASE);
			for png_name in res:
				name = re.sub("_\d+", "", png_name);
				code_png.add(name)
	finally:
		if lines:
			lines.close()


def read_from_file(path, local_png):
	result = local_png;
	try:
		# print("xml file name = ",path)
		find_png = set();
		lines = codecs.open(path)
		line_num = 0;
		for line in lines:
			line_num += 1;
			for png in local_png:
				if line.find(png) != -1:
					find_png.add(png);
					print(png, path, str(line_num));
				# print()
		# print(len(local_png));
		# print(len(find_png))
		result = local_png - find_png;
	# print(len(result))

	finally:
		if lines:
			lines.close()
	return result;


if __name__ == "__main__":
	# s = "test-1.png"
	# s1 = re.sub("_\d+","",s);

	'''
	list_xml = [];
	local_png = set();
	get_file_list(r"E:\MusicBox-Dev31187\KwResource\debug_resource\skin\base", local_png, list_xml)

	for root, dirs, files in os.walk(r'E:\MusicBox-Dev31187', topdown=False):
		for name in files:
			# print(os.path.join(root, name))
			if name.find('.cpp') != -1 or  name.find('.xml') != -1:
				local_png = read_from_file(os.path.join(root, name),local_png);
	print(len(local_png));
	for i in local_png:
		print(i)
	'''
	read_png_from_xml(r"E:\MusicBox-Dev31187\KwResource\bin\debug\Skin\base\KwConfig.xml");
	'''

	local_png = set();
	list_xml = [];
	get_file_list(r"E:\MusicBox-Dev31187\KwResource\debug_resource\skin\base", local_png, list_xml)


	print ("local png count = ",len(local_png))

	read_png_from_code(r'e:\code_png.txt')
	for xml in list_xml:
		read_png_from_xml(xml)

	all_png = code_png | xml_png;
	#a = all_png.find("DL_Search.png");
	print("png in code count = ",len(code_png))
	print("png in xml count = ",len(xml_png));
	print("png in code and xml count = ", len(all_png))

	invalid_png = local_png.difference(all_png);
	print("invalid png count = ",len(invalid_png))
	for name in invalid_png:
		print(name)
	
'''
