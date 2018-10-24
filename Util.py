# coding:utf-8


import urllib
import base64
import sys


def LogOut(a):
	print a


def Http_Get(strUrl):
	fUrl = urllib.urlopen(strUrl)
	strHtml = fUrl.read(20480)
	strHtml = strHtml.decode("utf-8", "ignore")
	return strHtml


def Http_Post(strUrl, strPostData):
	LogOut("Post:" + strUrl)
	LogOut("Data:" + strPostData)

	fUrl = urllib.urlopen(strUrl, strPostData)
	strHtml = fUrl.read(20480)
	strHtml = strHtml.decode("utf-8", "ignore")
	LogOut(fUrl.info())

	return strHtml


def KwBase64_decode(strData, strKey):
	i = 0
	res = ""
	strD = base64.b64decode(strData)
	while i < len(strD):
		j = 0
		while (i < len(strD) and j < len(strKey)):
			r = ord(list(strD)[i]) ^ ord(list(strKey)[j])
			i = i + 1
			j = j + 1
			res = res + chr(r)
	return res


def KwBase64_encode(strData, strKey):
	i = 0
	res = ""
	while i < len(strData):
		j = 0
		while (i < len(strData) and j < len(strKey)):
			r = ord(list(strData)[i]) ^ ord(list(strKey)[j])
			i = i + 1
			j = j + 1
			res = res + chr(r)
	res = base64.b64encode(res)
	return res


def Cmdline_GetChannelName(strChannelName):
	if len(sys.argv) >= 2:
		strChannelName = sys.argv[1]
	strChannelName = strChannelName.replace(".", "")
	strChannelName = strChannelName.replace("_", "")
	strChannelName = strChannelName.upper()
	return strChannelName


if __name__ == "__main__":
	import requests

	str_url = [
		"http://comment.kuwo.cn/com.s?type=get_rec_comment&uid=0&digest=15&sid=316799&page=1&rows=10&f=web&prod=MUSIC_8.7.5.0_BDS4&devid=15710039",
		"http://comment.kuwo.cn/com.s?type=get_rec_comment&uid=0&digest=15&sid=15249345&page=1&rows=10&f=web&prod=MUSIC_8.7.5.0_BDS4&devid=15710039",
		"http://comment.kuwo.cn/com.s?type=get_rec_comment&uid=0&digest=15&sid=451779&page=1&rows=10&f=web&prod=MUSIC_8.7.5.0_BDS4&devid=15710039"
		]
	session = requests.session()
	for i in range(0, 10):
		# session = requests.session()
		print (session.get(str_url[i % 3]), " index = ", str(i % 3))
