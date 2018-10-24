# -*- coding: cp936 -*-  

#############################################  
#   Written By Qian_F                        #       
#   2013-08-10                               #  
#   获取文件路径列表，并写入到当前目录生成test.txt #  
#############################################  

import os

import subprocess


def getfilelist(filepath, tabnum=1):
	simplepath = os.path.split(filepath)[1]
	returnstr = simplepath + "目录<>" + "\n"
	returndirstr = ""
	returnfilestr = ""
	filelist = os.listdir(filepath)
	for num in range(len(filelist)):
		filename = filelist[num]
		if os.path.isdir(filepath + "/" + filename):
			returndirstr += "\t" * tabnum + getfilelist(filepath + "/" + filename, tabnum + 1)
		else:
			returnfilestr += "\t" * tabnum + filename + "\n"
	returnstr += returnfilestr + returndirstr
	return returnstr + "\t" * tabnum + "</>\n"


def dealfile(input, output):
	file_object = open(input)
	map_data = {}
	try:
		all_the_text = file_object.read()

		vec_text = all_the_text.split("Microsoft (R) Windows Debugger Version")
		for text in vec_text:
			pos_s = text.find("FAULTING_IP:")
			if pos_s != -1:
				pos_e = text.find("quit", pos_s, -1)
				if pos_e != -1:
					text1 = text[pos_s:pos_e]
					add_s = text.find("Loading Dump File [")
					add_e = text.find("User Mini", add_s)
					add = text[add_s:add_e]
					if map_data.has_key(text1):
						t = map_data[text1]
						map_data[text1] = t + "\r\n" + add
					else:
						map_data[text1] = add
	finally:
		file_object.close()

	file_object = open(output, 'w+')
	for (k, v) in map_data.items():
		print(v)
		print ("------")
		print(k)

		file_object.write(v)
		file_object.write("----------------------\r\n")
		file_object.write(k)
	file_object.close()


def analize_dmp(output, input_dir):
	# path = raw_input("请输入文件路径:")
	usefulpath = input_dir.replace('\\', '/')
	if usefulpath.endswith("/"):
		usefulpath = usefulpath[:-1]
	if not os.path.exists(usefulpath):
		print "路径错误!"
	elif not os.path.isdir(usefulpath):
		print "输入的不是目录!"
	else:
		for dir_path, subpaths, files in os.walk(usefulpath, False):
			for file in files:
				file_path = os.path.join(dir_path, file)
				print(file_path)
				reload_str = ""

				# reload_str=".reload /i KwShellExtDll.dll"

				cmd1 = "f:\\software\\windbg\\cdb.exe -lines " \
				       "-y \"D:\\pdb; C:\\my_symbols\" " \
				       "-loga " + output + " " \
				                           "-z " + "\"" + file_path + "\"" + \
				       " -c \" .symopt + 40 ; " + reload_str + ";!analyze -v;.ecxr;KP; q\""
				print(cmd1)
				retcode = subprocess.call(cmd1, 5)
				print (retcode)


output = "d:\\output\\dmp_res.txt"
analize_dmp(output, r"D:\dmp\9051\disp")
dealfile(output, "d:\\output\\deal.txt")
