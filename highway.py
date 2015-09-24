#-*- coding: UTF-8 -*-
import sys
import urllib2
# import urllib
import json
import datetime
# from retrying import retry
from urllib2 import URLError, HTTPError

reload(sys)
sys.setdefaultencoding('utf-8')

def getHighWay(jsondata):
	# import json data
	jsondata=json.loads(jsondata)
	distance=0.0
	try:
		distance=jsondata['result']['routes'][0]['distance']
	except Exception, e:
		f.open('log.txt','a')
		f.write(datetime.datetime.now()+'In getHighWay Function Throw Exception:'+str(e.reason))
		f.close()
	else:
		pass
	finally:
		distance=distance/float(1000)
		distance=float('%0.2f'%distance)
		return distance

def getDuration(jsondata):
	jsondata=json.loads(jsondata)
	seconds=0.0
	try:
		seconds=jsondata['result']['routes'][0]['duration']
	except Exception, e:
		f.open('log.txt','a')
		f.write(datetime.datetime.now()+'In getDuration Function Throw Exception:'+str(e.reason))
		f.close()
	else:
		pass
	finally:
		minutes=float(seconds)/60
		hours=minutes/60
		hours=float('%0.2f'%hours)
		duration=hours
		return duration

# @retry(URLError, tries=4, delay=3, backoff=2)
def getDistance(origin, destination):
	##
	res={
		 	'distance': 0.0,
		 	'duration': 0.0,
		}
	try:
		url = 'http://api.map.baidu.com/direction/v1?mode=driving&origin='+origin+'&destination='+destination+'&origin_region='+origin+'&destination_region='+destination+'&output=json&ak=R5NpD7z0eUAXBkjN9GUdFXU5'
		# print url
		req=urllib2.Request(url)
		# print origin+'->'+destination
		data = urllib2.urlopen(req, timeout=60).read().decode('utf-8')
		distance=0.0
		duration=0.0
		# print data
		distance=getHighWay(data)
		duration=getDuration(data)
		res['distance']=distance
		res['duration']=duration
	# except urllib2.URLError, e:
	# 	print 'URLError='

	# 	res={
	# 	 	'distance': 0.0,
	# 	 	'duration': 0.0,
	# 	}
	# except urllib2.HTTPError, e:
	# 	print 'HTTPError='
	# 	res={
	# 	 	'distance': 0.0,
	# 	 	'duration': 0.0,
	# 	}
	except Exception, e:
		print 'Exception='+str(e.reason)
		f=open('except.txt','a')
		f.write(origin+'->'+destination)
		f.write('\n')
		f.close()
		f2=open('log.txt','a')
		f2.write(datetime.datetime.now()+'In getDistance Function Throw Exception:'+str(e.reason))
		f2.close()
		url = 'http://api.map.baidu.com/direction/v1?mode=driving&origin='+origin+'&destination='+destination+'&origin_region='+origin+'&destination_region='+destination+'&output=json&ak=R5NpD7z0eUAXBkjN9GUdFXU5'
		# print url
		req=urllib2.Request(url)
		# print origin+'->'+destination
		data = urllib2.urlopen(req, timeout=60).read().decode('utf-8')
		distance=0.0
		duration=0.0
		# print data
		distance=getHighWay(data)
		duration=getDuration(data)
		res['distance']=distance
		res['duration']=duration
	else:
		pass
	finally:
		res=json.dumps(res)
		return res


