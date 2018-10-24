# coding=utf8
__author__ = 'Administrator'

import json
import sys
import os
import string
from urllib import quote
import base64
import urllib
import ConfigParser
# import win32api

reload(sys)
sys.setdefaultencoding("utf-8")

play_all = "&playall=true";


# 推荐歌单
def jump_recom_list():
	s = "8";
	s_id = "2073656918";
	name = "Westlife : 翻唱的作品";
	psrc = "首页->猜你喜欢->";
	csrc = "曲库->首页->个性化推荐->Westlife : 翻唱的作品";

	# 一下是固定部分
	extend = "1";
	param = {};
	param["source"] = s;
	param["sourceid"] = s_id;
	param["name"] = name;
	param["extend"] = extend;
	param["other"] = "|psrc=" + psrc + "|csrc=" + csrc;

	src = "content_gedan.html?source=" + s + "&sourceid=" + s_id + "&name=" + name + "&id=" + s_id + play_all + "&extend=1&other=|psrc=" + psrc + "|csrc=" + csrc;
	b = json.dumps(param)
	p1 = quote(b);
	p2 = quote("ch:10002;name:classify;");
	p3 = quote("url:${netsong}" + src);
	result = "PageJump?param=" + p1 + ";" + p2 + ";" + p3 + "&calljump=true";

	print result;

	result = base64.b64encode(result)
	result = "/PageJump=" + result;
	print("jump_recom_list = " + result)
	return result;


# 热门页
def jump_hot_page():
	s = "51";
	s_id = "5045";
	name = "你的爱豆，我的同学！";

	# 一下是固定部分
	extend = "|MUSIC_COUNT=0|ORIGINAL_TYPE=1|";
	param = {};
	param["source"] = s;
	param["sourceid"] = s_id;
	param["name"] = name;
	param["extend"] = extend;
	param["qkback"] = "true";

	src = "content_hotcolumn.html?sourceid=" + s_id + play_all;
	j = json.dumps(param)
	p1 = quote(j);
	p2 = quote("ch:2;name:songlib;");
	p3 = quote("url:${netsong}" + src);

	result = "PageJump?param=" + p1 + ";" + p2 + ";" + p3 + "&calljump=true";

	result = base64.b64encode(result)
	result = "/PageJump=" + result;
	print("jump_hot_page = " + result)
	return result;


# 专辑
def jump_album():
	# result = '%7B%22source%22%3A%2213%22%2C%22sourceid%22%3A%225382610%22%2C%22name%22%3A%22%25E7%2594%25B5%25E8%25A7%2586%25E5%2589%25A7%25C2%25A0%25E5%2588%259D%25E9%2581%2587%25E5%259C%25A8%25E5%2585%2589%25E5%25B9%25B4%25E4%25B9%258B%25E5%25A4%2596%25C2%25A0OST%22%2C%22id%22%3A%220%22%2C%22extend%22%3A%22%22%2C%22other%22%3A%22%257Cfrom%253Dindex%22%2C%22qkback%22%3A%22true%22%7D;ch%3A10003%3Bname%3Aartist%3B;url%3A%24%7Bnetsong%7Dcontent_album.html%3Fsource%3D13%26sourceid%3D5382610%26name%3D%E7%94%B5%E8%A7%86%E5%89%A7%C2%A0%E5%88%9D%E9%81%87%E5%9C%A8%E5%85%89%E5%B9%B4%E4%B9%8B%E5%A4%96%C2%A0OST%26id%3D0%26other%3D%7Cfrom%3Dindex&calljump=true'
	result = r'{"source":"13","sourceid":"5382610","name":"%E7%94%B5%E8%A7%86%E5%89%A7%C2%A0%E5%88%9D%E9%81%87%E5%9C%A8%E5%85%89%E5%B9%B4%E4%B9%8B%E5%A4%96%C2%A0OST","id":"0","extend":"","other":"%7Cfrom%3Dindex","qkback":"true"}'
	result = quote(result)
	result = result + ';ch' + quote(':10003;name:artist;')
	result = result + ';url' + quote(
		':${netsong}content_album.html?source=13&sourceid=5382610&name=电视剧 初遇在光年之外 OST&id=0&other=|from=index') + r'&calljump=true'

	# print(result)
	result = "PageJump?param=" + result;
	result = '/PageJump=' + base64.b64encode(result);
	print ('jump_album = ' + result)
	return result;


def play_mv():
	play_mv_cmd = "play/?play=MQ==&num=MQ==&musicrid0=TVVTSUNfMjQ5OTg4&name0=aSBtaXNzIHlvdQ==&artist0=QmxpbmstMTgy&album0=QmxpbmstMTgy&artistid0=MTk1OQ==&albumid0=MzgxNQ==&mkvrid0=MTQ4Nzg4&hasecho0=MQ==&mkvnsig10=MjU2NTYwMDQ3MQ==&mkvnsig20=MTc5NTk0MTQ1NA==" + "&media=" + base64.b64encode(
		"mv");
	print ('play_mv=' + play_mv_cmd);
	return play_mv_cmd;


def read_kw_path():
	cfg = ConfigParser.ConfigParser()
	cfg.read(r'C:\ProgramData\kuwodata\kwmusic2013\Conf\User\config.ini')
	path = cfg.get('app', 'homepath');
	path += r"KwMusic.exe";
	return path;


def start_kw(cmdline):
	path = "\"" + read_kw_path() + "\" \"" + cmdline + "\"";
	temp_path = r"F:/cmd.bat";
	f = open(temp_path, "w+");
	f.write(path);
	f.close()
	os.system(temp_path);


def vip_page():
	result = "PageJump?param=%7B%7D;ch%3A10006%3Bname%3Asonglib%3B;url%3Ahttp%3A%2F%2Fvip1.kuwo.cn%2Fvip_adv%2Fvipzone_pc%2Findex.html%23%2Findex.html&calljump=true"
	result = '/PageJump=' + base64.b64encode(result);
	print ('jump_album = ' + result)
	return result;


if __name__ == "__main__":
	# result = base64.b64encode('param=%7B%22sourceid%22%3A%20%225045%22%2C%20%22source%22%3A%20%2251%22%2C%20%22name%22%3A%20%22%5Cu4f60%5Cu7684%5Cu7231%5Cu8c46%5Cuff0c%5Cu6211%5Cu7684%5Cu540c%5Cu5b66%5Cuff01%22%2C%20%22extend%22%3A%20%22%7CMUSIC_COUNT%3D0%7CORIGINAL_TYPE%3D1%7C%22%2C%20%22qkback%22%3A%20%22true%22%7D;ch%3A2%3Bname%3Asonglib%3B;url%3A%24%7Bnetsong%7Dcontent_hotcolumn.html%3Fsourceid%3D5045%26playall%3Dtrue&calljump=true');
	# print result
	# return ;
	# jump_recom_list();
	# jump_hot_page();
	# jump_recom_list();
	# jump_album();
	# cmdline = play_mv()

	# cmdline = jump_hot_page();
	cmdline = vip_page();
	start_kw(cmdline)

	'''
	jump_recom_list()
	jump_hot_page();
	print("play_music = play/?play=MQ==&num=MQ==&musicrid0=TVVTSUNfMjQ5OTg4&name0=aSBtaXNzIHlvdQ==&artist0=QmxpbmstMTgy&album0=QmxpbmstMTgy&artistid0=MTk1OQ==&albumid0=MzgxNQ==&mkvrid0=MTQ4Nzg4&hasecho0=MQ==&mkvnsig10=MjU2NTYwMDQ3MQ==&mkvnsig20=MTc5NTk0MTQ1NA==" +  "&media=" + base64.b64encode("mv") )
	'''
