#-*- coding: UTF-8 -*- 
from highway import getDistance
from xlrd import open_workbook
import sys
import urllib2
import urllib
import json
import datetime


def readListFromExcel(excelName):
	#Get one excel
	book = open_workbook(excelName)
	#Get datasheet
	table = book.sheets()[0]
	#Get nums and rows
	nums = table.nrows
	ncols = table.ncols
	#define array which read city 
	#encoding: utf-8
	array = [ 0 for i in range(nums)]
	for i in range(nums):
		# print table.cell(i,0).value
		array[i]=table.cell(i,0).value
		if "新疆" in array[i]:	
			array[i]="乌鲁木齐市"
		if "西藏" in array[i]:
			array[i]="拉萨市"
		if "广西" in array[i]:
			array[i]="南宁市"
		if "宁夏" in array[i]:
			array[i]="银川市"
		if "内蒙古" in array[i]:
			array[i]="呼和浩特市"
		str_split = array[i].split('省')
		str_len = len(str_split)
		array[i]=array[i].strip()
		# array[i-1] = str_split[str_len-1]
		# print array[i-1]
	return array


def writeToFile(array):
	lenth=len(array)
	f=open('distance.txt','w')
	f2=open('duration.txt','w')
	# workbook=xlsxwriter.Workbook('distance.xlsx')
	# worksheet=workbook.add_worksheet()
	# print 'create distance.xlsx'
	# worksheet.write(0,0,"中心城市")
	# for i in range(1,lenth+1):
	# 	worksheet.write(i,0,array[i-1])
	# 	worksheet.write(0,i,array[i-1])
	print 'create cites'
	for x in range(lenth):
		print array[x]
		print datetime.datetime.now()
		for y in range(lenth):
			if y > x:
				res=getDistance(array[x],array[y])
				res=json.loads(res)
				distance=res['distance']
				duration=res['duration']
				print array[x]+'->'+array[y]+':'
				print distance
				print duration
				f.write(str(distance))
				f.write(' ')
				f2.write(str(duration))
				f2.write(' ')
			else:
				f.write('0.0')
				f2.write('0.0')
				f.write(' ')
				f2.write(' ')
			# worksheet.write(x+1, y+1, distance)
		f.write('\n')
		f2.write('\n')

			

def startCalculate(excelName):
	array=readListFromExcel(excelName)
	writeToFile(array)

startCalculate('city.xlsx')