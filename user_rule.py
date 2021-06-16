# coding=utf-8
# 自定义的推荐规则

from copy import copy
from tmall import getDiffDay


# 推荐规则
# 函数可分为两部分
# 1. 计算用户特征
# 2. 根据规则进行筛选
#
# 参数 data: 数组，数组元素为 (user_id, brand_id, action_type, month, day)
# 返回值 R : 数组，数组元素为 (user_id, brand_id)

def getRecommendByRule(data):
	F = {}		# 存储用户特征
	R = []		# 存储推荐结果

	# 所有要进行统计的特征，在这里进行声明并赋予初始值
	item = {
		'click': 0,			# 点击次数
		'buy': 0,			# 购买次数
		'fav': 0,			# 加入收藏夹次数
		'cart': 0,			# 加入购物车次数
		'diff_day': 1000,	# 因为是要推测下一个月的购买情况
							# 显然在最近一段时间有交互的，购买可能性越大
							# 因此将最后一次交互的相差天数也作为一个特征
							# 如我们推测7月15-8月15这一个月的购买情况，用户在7月8号跟7月12号均有交互记录
							# 则diff_day为3（取最近的7月12，计算跟7月15的相差天数）

		                    # 此处可添加其他特征

	}

	# 1. 计算用户特征
	for uid, bid, action_type, month, day in data:
		# 初始化
		F.setdefault(uid, {})
		F[uid].setdefault(bid, copy(item))

		# 新建一个引用，简化代码
		e = F[uid][bid]

		# 基础特征计算
		if action_type == 0:
			e['click'] += 1
		elif action_type == 1:
			e['buy'] += 1
		elif action_type == 2:
			e['fav'] += 1
		elif action_type == 3:
			e['cart'] += 1

		# 时间特征
		diff_day = getDiffDay((month, day), (7, 15))
		if diff_day < e['diff_day']:
			e['diff_day'] = diff_day



	# 2. 根据特征进行筛选
	for uid, bid_list in F.items():
		for bid, e in bid_list.items():
            # # 在此处应用推荐规则，如将最近一个月内有交互，且总点击次数大于10次的，加入到推荐中
			# if e['diff_day'] < 20 and (e['click'] >10 or e['buy']>0) :
			# 	# 加入到推荐列表中，注意加入的是元组 (uid, bid)，有两个括号
			# 	R.append( (uid, bid) )
			# 	if e['diff_day'] < 10 and e['click'] > 3  :
			# 		# 加入到推荐列表中，注意加入的是元组 (uid, bid)，有两个括号
			# 		R.append((uid, bid))

	# if   e['diff_day']<30 and e['click'] >12 :
			# 	# 加入到推荐列表中，注意加入的是元组 (uid, bid)，有两个括号
			# 	R.append((uid, bid))


			#当前问题：PANDAS不知道如何实现多条件——特别是e['click']>3等
			# R.append((uid, 11080))
			# if   e['diff_day']<10 and e['click']>1 and e['buy']>0 and e['click']<11  :
			# 	R.append((uid,bid))
			# if  e['diff_day']<20 and e['click']>3 and e['click']<7 and e['buy']>0  :
			# 	R.append((uid,bid))
			# if  e['diff_day']<30 and e['click']>1  and e['click']<14 and e['buy']>0  :
			# 	R.append((uid,bid))
			# if  e['diff_day']<10 and e['fav']>1 and e['fav']<16 and e['buy']>0 :
			#  	R.append((uid, bid))
			# if  e['diff_day']<20 and e['fav']>1 and e['fav']<12 and e['buy']>0 :
			#  	R.append((uid, bid))
			# if  e['diff_day']<30 and e['fav']>2 and e['fav']<28 and e['buy']>0 :
			#  	R.append((uid, bid))
			# if  e['diff_day']<10 and e['cart']>1 and e['cart']<10 and e['buy']>0 :
			#  	R.append((uid, bid))
			# if e['diff_day']<20 and e['cart']>1 and e['cart']<12 and e['buy']>0:
			# 	R.append((uid, bid))
			# if e['diff_day']<30 and e['cart']>1 and e['cart']<19 and e['buy']>0:
			# 	R.append((uid, bid))
			if   e['diff_day']<8 and e['click']>3  :
				R.append((uid,bid))
			if e['diff_day']<10 and e['click']>1 and e['click']<4 and e['buy']>0:
				R.append((uid,bid))

			if   e['diff_day']<20 and (e['cart']>1 or e['buy']>0) :
				R.append((uid, bid))

			if   e['diff_day']<30 and (e['fav']>1 or e['buy']>2) :
				R.append((uid, bid))


			if  e['diff_day']<40 and e['click'] > 20:
				R.append((uid, bid))

			# if e['diff_day']<10 and e['cart']>1 and e['cart']<10 and e['buy']>0:
			# 	R.append((uid,bid))

			# if   e['diff_day']<20 and (e['cart']>1 or e['buy']>0) :
			# 	R.append((uid, bid))
			#
			# if   e['diff_day']<30 and (e['fav']>3 or e['buy']>2) :
			# 	R.append((uid, bid))
			# if e['click']> :
			# 	R.append((uid,bid))

	# if   e['diff_day']<20 and e['buy']>3  :
	# 	R.append((uid, bid))
	# if   (e['diff_day']<20) and (e['cart']>3 or e['buy']>2 or e['fav']>7) :
	# 	R.append((uid, bid))


			# if	(e['diff_day']<10) and e['fav']>3 :
			# 	R.append((uid, bid))    没有任何影响
			#
            # if  e['click']>80 or e['buy']>12 :
			# 	R.append((uid, bid))

#----------------------------------------------------------
	# #加上这些最高排行商品以及消费很猛的买家也没有用
	# 			if int(bid) == 7868:
	# 				R.append((uid, bid))



				# if int(bid) == 2683:
				# 	R.append((uid, bid))
				# if int(bid) == 27791:
				# 	R.append((uid, bid))
				# if int(bid) == 11196:
				# 	R.append((uid, bid))
				# if int(bid) == 905:
				# 	R.append((uid, bid))
				# if int(bid) == 14261:
				# 	R.append((uid, bid))
				# if int(bid) == 14020:
				# 	R.append((uid, bid))
				# if int(bid) == 3228:
				# 	R.append((uid, bid))
				# if int(bid) == 15584 :
				# 	R.append((uid, bid))
				# if int(uid) == 3404000:
				# 	R.append((uid, bid))
				# if int(bid) == 5780000:
				# 	R.append((uid, bid))
				# if int(bid) == 10628500:
				# 	R.append((uid, bid))
				# if int(bid) == 6874250:
				# 	R.append((uid, bid))
				# if int(bid) == 3228:
				# 	R.append((uid, bid))
				# if int(bid) == 15584 :
				# 	R.append((uid, bid))
				# if int(bid) == 3228:
				# 	R.append((uid, bid))

	return R
