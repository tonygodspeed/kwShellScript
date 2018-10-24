# coding:utf-8

""" 
从渠道获取安装信息
"""

import Util
import base64
import json
import urllib
import time

g_strBase64Key = "yeelion "
g_strUrlInstall = "http://ecomconf.kuwo.cn/plugin/ecom/checkRegUserNew?"


# 获取安装信息
def GetInstallInfo(strChannelName):
	strJsonData = "{"
	strJsonData += '"admin" : 0,'
	strJsonData += '"mac" : "A41F726A4243",'
	strJsonData += '"os" : "6.1.7601",'
	strJsonData += '"src" : "MUSIC_8.0.3.0_PQ",'
	# strJsonData += '"srcid" : "MUSIC8030PQ",'
	strJsonData = strJsonData + '"srcid" : "' + strChannelName + '",'
	strJsonData += '"toolver" : "1.0.2.6",'
	strJsonData += '"uac" : 1,'
	strJsonData += '"update" : false,'
	strJsonData += '"x64" : 1,'
	strJsonData += '"tester" : 1'
	strJsonData += '}'

	# 加密请求
	strEncodeJson = Util.KwBase64_encode(strJsonData, g_strBase64Key)
	strPostData = "data=" + urllib.quote(strEncodeJson)

	# 请求数据
	strUrlInstall = g_strUrlInstall + str(time.time())
	strHtmlEncodeData = Util.Http_Post(strUrlInstall, strPostData)
	strLog = strUrlInstall + "&" + strPostData
	Util.LogOut(strLog)

	if len(strHtmlEncodeData) == 0:
		Util.LogOut("http failed")
		return ""

	# 解密返回
	if (list(strHtmlEncodeData)[0]) == '{':
		strHtmlDecodeData = strHtmlEncodeData
	else:
		strHtmlDecodeData = Util.KwBase64_decode(strHtmlEncodeData, g_strBase64Key)

	return strHtmlDecodeData


def main():
	Util.LogOut("==================begin==================")

	# 取渠道名
	# strChannelName = Util.Cmdline_GetChannelName("MUSIC8120BCS49")
	strChannelName = Util.Cmdline_GetChannelName("MUSIC8120BCS50")

	stdInstallInfo = GetInstallInfo(strChannelName)

	Util.LogOut(stdInstallInfo)
	Util.LogOut("\nGetInstall: " + strChannelName + "\n")
	Util.LogOut("==================end==================")


# raw_input()

if __name__ == '__main__':
	main()
	pass
