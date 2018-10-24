# coding=utf8
import os
import re

if __name__ == '__main__':
	str_test = '<Button name="btn_new_list" text="新建列表" tooltip="新建列表" textpadding="18,0,0,0" padding="0,19,0,0" width="90" height="28" statusimage="btn_new_list.png"  iconimage="btn_new_list_icon.png" icondest="12,8,26,22"/>'
	# t = 'abcdef'

	p = re.compile('\"gnp\..*?\"');

	print p.findall(str_test[::-1]);

	for i in p.finditer(str_test[::-1]):
		print i.group()[::-1];
