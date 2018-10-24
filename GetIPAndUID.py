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


def from_this_dir(filename):
	if filename == "":
		return os.path.dirname(os.path.abspath(__file__))
	else:
		return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


FILE = from_this_dir("")
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

# path = r'F:/ip.txt'
path = r'F:/stat/error_log'

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
# fields=country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query,status,message

g_strUrl = "http://ip-api.com/json/{0}?lang=zh-CN&fields=city,isp,as,status"
dict_ip_location = {};
dict_uid_ip = {};
set_ip = set();
list_ips = [];


#
def GetIPLocation(ips):
	for ip in ips:
		time.sleep(0.41)
		url = g_strUrl.format(str.strip(str(ip)))
		req = urllib2.Request(url)
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		pydata = json.loads(res)
		status = pydata["status"];
		if status == "success":
			city = pydata['city'] + '-' + pydata['isp'];
			if city in dict_ip_location:
				dict_ip_location[city] += 1
			else:
				dict_ip_location[city] = 1
			print(city)
		else:
			logger.error(status)
			time.sleep(2)

	ip_location = sorted(dict_ip_location.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
	print(ip_location)


def GetUIDAndIP(file):
	global g_all_cnt
	global g_all_s

	for i in file:
		# g_all_cnt += 1;
		mt = re.match(".*U:([0-9]*).*\((\s*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s*)\)", i, re.IGNORECASE)

		if mt:
			uid = mt.group(1);
			ip = mt.group(2);
			dict_uid_ip[uid] = ip;
			# list_ips.append(ip);
			set_ip.add(ip);

	list_ips = list(set_ip);
	# for ip in dict_uid_ip:
	print(len(dict_uid_ip))
	# print(dict_uid_ip);
	print(len(list_ips));
	GetIPLocation(list_ips);


if __name__ == '__main__':
	fRead = sys.stdin;
	if sys.stdin.isatty() or sys.platform == "win32":
		fRead = codecs.open(path);  # 非重定向则读取指定文件数据
	# GetIPLocation(fRead);
	GetUIDAndIP(fRead);
