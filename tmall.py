# coding=utf-8
#
# 定义通用函数
# 

import time
import datetime

import numpy as np
import pandas as pd
import statsmodels.api as sm

import sys
sys.dont_write_bytecode = True

import warnings
warnings.filterwarnings("ignore")


# 加载数据
def loadData():
	f = open("./data/data.csv", "r")
	data = []

	line = f.readline()
	while line:
		user_id, brand_id, action_type, month, day = line.strip().split(',')

		# 转换格式
		action_type = int(action_type)
		month = int(month)
		day = int(day)

		data.append( (user_id, brand_id, action_type, month, day) )
		line = f.readline()

	f.close()
	return data


# 对推荐进行检验
def printF1Score(recommend):

	predict_num = 0
	hit_num = 0
	brand = 0

	# 读取实际的购买情况
	f = open("./data/result.txt", "r")
	result = {}
	lines = f.readlines()
	for index, item in enumerate(lines):
		uid, bid = item.strip("\n").split("\t")
		result[uid] = set(bid.split(","))
		brand += len(result[uid])
	f.close()

	# 调整预测结果格式
	R = {}
	for uid, bid in recommend:
		R.setdefault(uid, [])
		if bid not in R[uid]:
			R[uid].append(bid)

	# 计算推荐数量以及命中数量
	for uid, bid_list in R.items():
		predict_num += len(bid_list)

		if uid in result:
			for bid in bid_list:
				if bid in result[uid]:
					hit_num += 1

	# 输出结果
	print(u"执行时间:\t %s" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
	print(u"预测总数:\t %d" % predict_num)
	print(u"命中数量:\t %d" % hit_num)

	if brand == 0 or hit_num == 0:
	 	print(u"F1得分:\t 0")
	else:
		precision = float(hit_num)/predict_num
		recall = float(hit_num)/brand
		print(u"精确度:\t %.2f%%" % round(100*precision, 2))
		print(u"召回率:\t %.2f%%" % round(100*recall, 2))

		print(u"F1得分:\t %.2f%%" % round(100*2*precision*recall/(precision+recall), 2))


# 返回两个日期相差的天数(d2-d1)
def getDiffDay(d1, d2):
	d1 = datetime.date(2015, d1[0], d1[1])
	d2 = datetime.date(2015, d2[0], d2[1])
	day = (d2-d1).days
	return day
