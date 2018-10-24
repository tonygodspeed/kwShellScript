# coding:utf-8

import json
import urllib
import time
import urllib2
import sys
import codecs;
import re
import logging
import datetime
import os
import getopt
from IPAddress import IPAddresss

reload(sys)
sys.setdefaultencoding("utf-8")


def from_this_dir(filename):
	return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


FILE = os.path.dirname(os.path.abspath(__file__))  # from_this_dir("log")
curDay = datetime.datetime.now().strftime("%Y%m%d")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(filename)s <%(process)d> [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y%m%d %H:%M:%S',
                    filename=os.path.join(FILE, curDay + '_log.txt'),
                    filemode='a+')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(filename)s <%(process)d> [line:%(lineno)d] %(levelname)s %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

path = r'F:/ip.txt'

'''
{
as: "AS4134 No.31,Jin-rong Street",
city: "Jinan",
country: "China",
countryCode: "CN",
isp: "China Telecom Shandong",
lat: 36.6683,
lon: 116.9972,
org: "China Telecom Shandong",
query: "113.128.72.197",
region: "SD",
regionName: "Shandong",
status: "success",
timezone: "Asia/Shanghai",
zip: ""
}
'''
g_strUrl = "http://ip-api.com/json/real_ip?lang=zh-CN"
dict_ip_location = {};
QQWRY_PATH = os.getcwd() + "/data/qqwry.dat"


#

def GetIPLocationFromLocal(ips):
	libips = IPAddresss(QQWRY_PATH)
	for ip in ips:
		print(libips.getIpAddr(libips.str2ip(str.strip(str(ip)))))


def GetIPLocation(ips):
	for ip in ips:
		time.sleep(0.41)
		url = g_strUrl.replace("real_ip", str.strip(str(ip)))
		req = urllib2.Request(url)
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		pydata = json.loads(res)
		status = pydata["status"];
		if status == "success":
			city = pydata['city'] + '-' + pydata['as'];
			if city in dict_ip_location:
				dict_ip_location[city] += 1
			else:
				dict_ip_location[city] = 1
			print(city.decode('utf-8'))
		else:
			logger.error(status)
			time.sleep(2)

	ip_location = sorted(dict_ip_location.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
	print(ip_location)


if __name__ == '__main__':
	if (len(sys.argv) == 2 and os.path.exists(sys.argv[1])):
		path = sys.argv[1];
	fRead = sys.stdin;
	# print(sys.getdefaultencoding())
	if sys.stdin.isatty() or sys.platform == "win32":
		fRead = codecs.open(path);  # 非重定向则读取指定文件数据
		print(r"config path = {0}".format(path));
	# GetIPLocation(fRead);
	GetIPLocationFromLocal(fRead)
