import logging
import datetime

FORMAT = '%(asctime)-15s  %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def getLogger():
	return logger


def getNDayStr2(n):
	now = datetime.datetime.now()
	nDay = datetime.timedelta(n)
	return (now - nDay).strftime("%Y%m%d")
