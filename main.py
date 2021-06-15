import pandas as pd
from tmall import getDiffDay
import datetime

data = pd.read_csv(
    r"new_data.csv",
    header=None,
    names=['user_id', 'item', 'type', 'year', 'month', 'day','datetime','lasttime']
)

month = data['month']
day   = data['day']


data1 = pd.read_csv(
    r"new_data.csv",
    header=None,
    names=['user_id', 'item', 'type', 'year', 'month', 'day']
)

data['datetime'] = pd.to_datetime(data[['year', 'month', 'day']])
# data['datetime'] = datetime.datetime(data['year'], data['month'],data['day'])
del data['year'], data['month'], data['day']

# def to_integer(dt_time):
#     return 10000*dt_time.year + 100*dt_time.month + dt_time.day
a=pd.to_datetime('2015-7-15')
b=a-data['datetime']
lasttime=b.dt.days
data['lasttime']=lasttime
# print(data)

data4=data   #data4有datetime

data4.to_csv(r'D:\new_data_.csv')
# print(data4)
#------------------------------------------------------
#lasttime<20 + click 的时候，click/buy的转化率
# most_user_pv=data4[(data4['type']==0)&(data4['lasttime']<20)].groupby('user_id').count()['item']
# most_user_pv=most_user_pv.sort_values(ascending=False)
#
# most_user_buy=data4[(data4['type']==1)&(data4['lasttime']<20)].groupby('user_id').count()['item']
# most_user_buy=most_user_buy.sort_values(ascending=False)
#
# user_cart_buy=pd.DataFrame(most_user_pv)
# user_cart_buy.columns=['pv']
# user_buy=pd.DataFrame(most_user_buy)
# user_buy.columns=['buy']
# user_cart_buy=user_cart_buy.join(user_buy,how='left')
# #NA变为0
# user_cart_buy=user_cart_buy.fillna({'buy':0})
# user_cart_buy['pv']=user_cart_buy['buy']+user_cart_buy['pv']
# user_cart_buy['buy-pv']=user_cart_buy['buy']/user_cart_buy['pv']
# user_cart_buy=user_cart_buy.sort_values(by='buy-pv',ascending=False)
# user_cart_buy.to_csv(r'D:\userpvbuy-20days.csv')
# print(user_cart_buy)
#----------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------
#整体表格 处理 看整体转化率  <20 day
# most_user_pv=data4[(data4['type']==0)&(data4['lasttime']<20)].groupby('user_id').count()['item']
# most_user_pv=most_user_pv.sort_values(ascending=False)
# most_user_buy=data4[(data4['type']==1)&(data4['lasttime']<20)].groupby('user_id').count()['item']
# most_user_buy=most_user_buy.sort_values(ascending=False)
# # most_user_fav=data4[(data4['type']==2)&(data4['lasttime']<20)].groupby('user_id').count()['item']
# # most_user_fav=most_user_fav.sort_values(ascending=False)
# most_user_cart=data4[(data4['type']==3)&(data4['lasttime']<20)].groupby('user_id').count()['item']
# most_user_cart=most_user_cart.sort_values(ascending=False)
#
# # user_cart_buy=pd.DataFrame(most_user_pv)
# # user_cart_buy.columns=['pv']
# user_buy=pd.DataFrame(most_user_buy)
# user_buy.columns=['buy']
# # user_cart_buy=pd.DataFrame(most_user_fav)
# # user_cart_buy.columns=['fav']
# user_cart_buy=pd.DataFrame(most_user_cart)
# user_cart_buy.columns=['cart']
# user_cart_buy=user_cart_buy.join(user_buy,how='left')
#
# # user_cart_buy=user_cart_buy.fillna({'buy':0})
# # user_cart_buy['pv']=user_cart_buy['buy']+user_cart_buy['pv']
# # user_cart_buy['buy-pv']=user_cart_buy['buy']/user_cart_buy['pv']
# # user_cart_buy=user_cart_buy.sort_values(by='buy-pv',ascending=False)
# user_cart_buy=user_cart_buy.fillna({'buy':0})
# user_cart_buy['cart']=user_cart_buy['buy']+user_cart_buy['cart']
# user_cart_buy['cart-pv']=user_cart_buy['buy']/user_cart_buy['cart']
# user_cart_buy=user_cart_buy.sort_values(by='cart-pv',ascending=False)
# print(user_cart_buy)


# user_cart_buy=user_cart_buy.join(user_buy,how='left')
# #NA变为0
# user_cart_buy=user_cart_buy.fillna({'buy':0})
# user_cart_buy['cart']=user_cart_buy['buy']+user_cart_buy['cart']
# user_cart_buy['percent']=user_cart_buy['buy']/user_cart_buy['cart']
# user_cart_buy=user_cart_buy.sort_values(by='percent',ascending=False)
#
# print(user_cart_buy)

#--------------------------------------------------------------------------



#----------------------------------------------------------------
# 每日活跃量
# DAU=data4.groupby('datetime').count()['user_id']
# print(DAU)
#-------------------------------------------------------------
#网页浏览量
# day_pv=data4[data4['type']==0].groupby('datetime').count()['user_id']
# print(day_pv)
#-----------------------------------------------------------------------

#实际每日购买量
# day_buy=data4[data4['type']==1].groupby('datetime').count()['user_id']
# print(day_buy)
#---------------------------------------------
#网页浏览量
# day_pv=data1[data1['type']==0].count()['user_id']
# print(day_pv)
#--------------------------------------------------
#浏览次数最多的客户行为——2940000
# most_user_pv=data4[data4['type']==0].groupby('user_id').count()['item']
# most_user_pv=most_user_pv.sort_values(ascending=False)
# print(most_user_pv)
# most_user_data=data4[data4['user_id']==2940000].groupby('type').count()['item']
# print(most_user_data)
#-----------------------------------------------
# most_user_pv=data4[data4['type']==0].groupby('item').count()['user_id']
# most_user_pv=most_user_pv.sort_values(ascending=False)4
# print(most_user_pv)
# ------------------------------------------------
#从上到下销量非常好的品牌
# most_user_lovebuy=data4[data['type']==1].groupby('item').count()['user_id']
# most_user_lovebuy.to_csv('D:\most_user_loveby.csv')
# print(most_user_lovebuy)


#-------------------------------------------------------------
#购买次数最多的客户行为——3404000
# most_user_buy=data4[data4['type']==1].groupby('user_id').count()['item']
# most_user_buy=most_user_buy.sort_values(ascending=False)
# # most_user_buy_data=data4[data4['user_id']==3404000].groupby('type').count()['item']
# # print(most_user_buy_data)
# print(most_user_buy)
#----------------------------------------------------
#去重复
# data4.drop_duplicates()
# print(data4)
#--------------------------------
#查看数据类型
# data1.info()
#-----------------------------------------
#查看商品数量
#len(data4['item'].unique())#116848
#--------------------------------------------
#查看种类数量——没用
#len(data4['category'].unique())#4027
#-------------------------------------------
#每个月份同一日活跃量
# DAU=data1.groupby('day').count()['user_id']
# print(DAU)
#-----------------------------------------------
#每个月份活跃量
# DAU=data1.groupby('month').count()['user_id']
# print(DAU)
#-------------------------------------------------------------------
# 浏览商品加入购物车转化率   py代表点击
# most_user_pv=data4[data4['type']==0].groupby('user_id').count()['item']
# most_user_pv=most_user_pv.sort_values(ascending=False)
# #cart
# most_user_cart=data4[data4['type']==3].groupby('user_id').count()['item']
# most_user_cart=most_user_cart.sort_values(ascending=False)
# #py
# user_cart_py=pd.DataFrame(most_user_pv)
# user_cart_py.columns=['py']
#
# user_cart=pd.DataFrame(most_user_cart)
# user_cart.columns=['cart']
#
# user_cart_py=user_cart_py.join(user_cart,how='left')
# #空值赋值为0
# user_cart_py=user_cart_py.fillna({'cart':0})
# user_cart_py['py']=user_cart_py['py']+user_cart_py['cart']
# user_cart_py['percent']=user_cart_py['cart']/user_cart_py['py']
# user_cart_py=user_cart_py.sort_values(by='percent',ascending=False)
#
# #给customer贴标签,根据percent转换成三种类型人，分流分析
# labels=[]
# for i in user_cart_py['percent']:
#     if i>=0.5:
#         a=3
#     elif i>=0.1:
#         a=2
#     elif i>0:
#         a=1
#     else:
#         a=0
#     labels.append(a)
# user_cart_py['usertype']=labels
# print(user_cart_py)
#--------------------------------------------------------------------------
#购物车——购买转化率
# most_user_cart=data4[(data4['type']==3)&(data4['lasttime']<10)].groupby('user_id').count()['item']
# most_user_cart=most_user_cart.sort_values(ascending=False)
#
# most_user_buy=data4[(data4['type']==1)&(data4['lasttime']<10)].groupby('user_id').count()['item']
# most_user_buy=most_user_buy.sort_values(ascending=False)
#
# user_cart_buy=pd.DataFrame(most_user_cart)
# user_cart_buy.columns=['cart']
# user_buy=pd.DataFrame(most_user_buy)
# user_buy.columns=['buy']
# user_cart_buy=user_cart_buy.join(user_buy,how='left')
# #NA变为0
# user_cart_buy=user_cart_buy.fillna({'buy':0})
# user_cart_buy['cart']=user_cart_buy['buy']+user_cart_buy['cart']
# user_cart_buy['percent']=user_cart_buy['buy']/user_cart_buy['cart']
# user_cart_buy=user_cart_buy.sort_values(by='percent',ascending=False)
# user_cart_buy.to_csv(r'D:\cart-buy-10days.csv')
# print(user_cart_buy)
#--------------------------------------------------------------------------------
#点击和购买的转化率
# most_user_pv=data4[data4['type']==0].groupby('user_id').count()['item']
# most_user_pv=most_user_pv.sort_values(ascending=False)
#
# most_user_buy=data4[data4['type']==1].groupby('user_id').count()['item']
# most_user_buy=most_user_buy.sort_values(ascending=False)
#
# user_cart_buy=pd.DataFrame(most_user_pv)
# user_cart_buy.columns=['pv']
# user_buy=pd.DataFrame(most_user_buy)
# user_buy.columns=['buy']
# user_cart_buy=user_cart_buy.join(user_buy,how='left')
# #NA变为0
# user_cart_buy=user_cart_buy.fillna({'buy':0})
# user_cart_buy['pv']=user_cart_buy['buy']+user_cart_buy['pv']
# user_cart_buy['percent']=user_cart_buy['buy']/user_cart_buy['pv']
# user_cart_buy=user_cart_buy.sort_values(by='percent',ascending=False)
# user_cart_buy.to_csv(r'D:\userpvbuy.csv')
# print(user_cart_buy)

#-----------------------------------------------------------------------------
#--------------------------------------------------------------------------
#购物车——购买转化率
# most_user_fav=data4[(data4['type']==2)&(data4['lasttime']<30)].groupby('user_id').count()['item']
# most_user_fav=most_user_fav.sort_values(ascending=False)
#
# most_user_buy=data4[(data4['type']==1)&(data4['lasttime']<30)].groupby('user_id').count()['item']
# most_user_buy=most_user_buy.sort_values(ascending=False)
#
# user_cart_buy=pd.DataFrame(most_user_fav)
# user_cart_buy.columns=['fav']
# user_buy=pd.DataFrame(most_user_buy)
# user_buy.columns=['buy']
# user_cart_buy=user_cart_buy.join(user_buy,how='left')
# #NA变为0
# user_cart_buy=user_cart_buy.fillna({'buy':0})
# user_cart_buy['fav']=user_cart_buy['buy']+user_cart_buy['fav']
# user_cart_buy['percent']=user_cart_buy['buy']/user_cart_buy['fav']
# user_cart_buy=user_cart_buy.sort_values(by='percent',ascending=False)
# user_cart_buy.to_csv(r'D:\fav-buy-30days.csv')
# print(user_cart_buy)
#--------------------------------------------------------------------------------
#筛选buy>=1，自己调节吧
#
# most_user_buy=data4[data4['type']==1].groupby('user_id').count()['item']
# most_user_buy=most_user_buy.sort_values(ascending=False);,lm
#
# item_buy1=most_user_buy[most_user_buy>=1]
# item_buy1=pd.DataFrame(item_buy1)
# item_buy1.columns=['buy1']
# item_buy1=item_buy1.reset_index('user_id')
#
# 进行格式转换成形成购买清单
# for i in item_buy1['user_id']:
#     if i==item_buy1['user_id'][0]:
#         a=data4[data4['user_id']==i]
#         b=a[a['type']==1]
#         c=b['item']
#         d=pd.DataFrame(c)
#         d.columns=[i]
#         d.reset_index(drop=True,inplace=True)
#         d=d.T
#         user_item_buy=d
#     else:
#         a=data4[data4['user_id']==i]
#         b=a[a['type']==1]
#         c=b['item']
#         d=pd.DataFrame(c)
#         d.columns=[i]
#         d.reset_index(drop=True,inplace=True)
#         d=d.T
#         user_item_buy=pd.concat([user_item_buy,d])
# user_item_buy_new=user_item_buy.reset_index()
# print(user_item_buy_new)
#
# #转换成哑变量矩阵
# for i in range(len(user_item_buy)):
#     if i==0:
#         a = user_item_buy.iloc[i,:]
#         b = pd.DataFrame(a)
#         b=b.dropna()
#         b.columns=['item']
#         b[i]=1
#         b.set_index('item', inplace=True)
#         b=b.T
#         b.to_csv(r'd:\da.csv')
#         user_buy_matrix=pd.read_csv(r'd:\da.csv',index_col=0)
#     else:
#         a = user_item_buy.iloc[i,:]
#         b = pd.DataFrame(a)
#         b=b.dropna()
#         b.columns=['item']
#         b[i]=1
#         b.set_index('item', inplace=True)
#         b=b.T
#         b.to_csv(r'd:\da.csv')
#         aa = pd.read_csv(r'd:\da.csv',index_col=0)
#         user_buy_matrix=pd.concat([user_buy_matrix,aa])
# # 将缺失值填补为0
# user_buy_matrix=user_buy_matrix.fillna(0)
# user_buy_matrix.to_csv(r'D:\matrix.csv')