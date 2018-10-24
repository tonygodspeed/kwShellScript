# coding:utf-8

import Util
import base64
import sys
import urllib
import time

"""
下载渠道对应的配置文件
"""

g_strConfigUrl = "http://ecomconf.kuwo.cn/plugin/ecom/configure?1=9"
g_strBase64Key = "yeelion "


def GetConfig(strChannelName):
	# 构造请求头
	chid = "MUSIC8700PQ"  # 'MUSIC8520P2T1' 24
	mac = 'MUSIC8200P2T1'
	cfg_ver = '29'
	is_admin = '0';
	req_data = r'prod=KWSHELLEXT&ver=KWSHELLEXT_1.0.6.9077_' + chid + '&dispver=1.0.6.9077&chid=' \
	           + chid + '&gid=4021&mac=' \
	           + mac + '&admin=' \
	           + is_admin + '&x64=1&uac=0&osdetail=6.1.7601.2_ServicePack1&os=6.1.7601&cfgver=' \
	           + cfg_ver + '&inst_time=1490151834&tester=1'
	strDataEncode = Util.KwBase64_encode(req_data, g_strBase64Key)
	strPostData = "&data=" + urllib.quote(strDataEncode)
	# strPostData = r"m=130;Qi4yPyEqImw8PTEzWEFeDkxLUFxaXzFtLDYsL1FfXRApNEknPjsvczIoKig8Iyt/SEtVQl9BWRBLVUkPBgEISR5eKj9TWkARV1dTXFkTL0QUDAtWWBM2Fk1fVRAkLi0aSVVVL1tWWGJBUFVfFTovY0NVGR4cAQoaSFdRX1laWBJMXg=="

	# 请求数据
	strHtmlEncodeData = Util.Http_Post(g_strConfigUrl, strPostData)

	if len(strHtmlEncodeData) == 0:
		Util.LogOut("http failed")
		return ""
	import json
	print(strHtmlEncodeData)
	pydata = json.loads(strHtmlEncodeData);
	print "cfg_ver : " + str(pydata["cfgver"]);
	strHtmlEncodeData = Util.Http_Get(pydata["cfgurl"]);
	# 解密请求
	if list(strHtmlEncodeData)[0] == '[':
		strHtmlDecodeData = strHtmlEncodeData
	else:
		strHtmlDecodeData = base64.b64decode(strHtmlEncodeData)
	# LogOut(stdHtmlDecodeData)
	return strHtmlDecodeData


def OutFile(strFilePath, strFileData):
	fWrite = open(strFilePath)
	try:
		fWrite.write(strFileData)
		fWrite.flush()
	finally:
		fWrite.close()


def main():
	Util.LogOut("==================begin==================")
	t = 'a';
	print(ord(t))
	# 取渠道名
	strChannelName = Util.Cmdline_GetChannelName("MUSIC8500PT")
	# strChannelName = Util.Cmdline_GetChannelName("MUSIC8200BCS35")

	stdConfig = GetConfig(strChannelName)

	# 输出配置	
	Util.LogOut(stdConfig)

	Util.LogOut("\nGetConfig: " + strChannelName + "\n")
	Util.LogOut("==================end==================")


if __name__ == '__main__':
	main()
