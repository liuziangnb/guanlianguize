from apriori import * #导入自行编写的apriori函数
import pandas as pd
user_buy_matrix=pd.read_csv(r'D:\matrix.csv',index_col=0)
# outputfile = 'D:/apriori_rules.xls'
support = 0.005 #最小支持度
confidence = 0.01 #最小置信度
ms = '---' #连接符，默认'--'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符


# find_rule(user_buy_matrix, support, confidence).to_excel('D:/apriori_rules.csv') #保存结果
k=find_rule(user_buy_matrix, support, confidence)
print(k)